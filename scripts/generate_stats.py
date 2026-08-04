#!/usr/bin/env python3
"""Render GitHub profile stat cards to static SVG files committed into the repo."""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API = "https://api.github.com/graphql"
LOGIN = os.environ.get("GH_LOGIN", "TheDeadcoder")
TOKEN = os.environ.get("GH_TOKEN", "")
OUT = Path(os.environ.get("OUT_DIR", "assets"))
TOP_LANGS = 6

THEMES = {
    "light": {
        "bg": "#ffffff", "border": "#d1d9e0", "title": "#1f2328",
        "value": "#1f2328", "muted": "#59636e", "accent": "#0969da",
        "track": "#eaeef2",
    },
    "dark": {
        "bg": "#0d1117", "border": "#3d444d", "title": "#f0f6fc",
        "value": "#f0f6fc", "muted": "#9198a1", "accent": "#4493f8",
        "track": "#21262d",
    },
}

FONT = ("ui-sans-serif,-apple-system,BlinkMacSystemFont,'Segoe UI',"
        "Noto Sans,Helvetica,Arial,sans-serif")


def gql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        API, data=body,
        headers={"Authorization": f"bearer {TOKEN}",
                 "Content-Type": "application/json",
                 "User-Agent": "profile-stats"},
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                payload = json.load(r)
            if "errors" in payload:
                raise RuntimeError(payload["errors"])
            return payload["data"]
        except urllib.error.HTTPError as e:
            if e.code in (403, 502, 503) and attempt < 4:
                time.sleep(2 ** attempt)
                continue
            raise
    raise RuntimeError("graphql request failed")


PROFILE_Q = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    createdAt
    followers { totalCount }
    pullRequests { totalCount }
    issues { totalCount }
    repositoriesContributedTo(
      contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, PULL_REQUEST_REVIEW]
    ) { totalCount }
    repositories(
      ownerAffiliations: OWNER, isFork: false, first: 100, after: $cursor
    ) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 20, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}
"""

CONTRIB_Q = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def collect():
    cursor, stars, langs = None, 0, {}
    base = None
    repo_count = 0
    while True:
        data = gql(PROFILE_Q, {"login": LOGIN, "cursor": cursor})["user"]
        base = base or data
        repos = data["repositories"]
        repo_count = repos["totalCount"]
        for node in repos["nodes"]:
            stars += node["stargazerCount"]
            for edge in node["languages"]["edges"]:
                name = edge["node"]["name"]
                entry = langs.setdefault(
                    name, {"size": 0, "color": edge["node"]["color"] or "#8b949e"})
                entry["size"] += edge["size"]
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]

    start = datetime.fromisoformat(base["createdAt"].replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    commits, contributions, days = 0, 0, {}
    window = start
    while window < now:
        end = min(window.replace(year=window.year + 1), now)
        cc = gql(CONTRIB_Q, {
            "login": LOGIN,
            "from": window.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": end.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })["user"]["contributionsCollection"]
        commits += cc["totalCommitContributions"]
        cal = cc["contributionCalendar"]
        contributions += cal["totalContributions"] + cc["restrictedContributionsCount"]
        for week in cal["weeks"]:
            for day in week["contributionDays"]:
                days[day["date"]] = max(
                    days.get(day["date"], 0), day["contributionCount"])
        window = end

    return {
        "stars": stars,
        "commits": commits,
        "contributions": contributions,
        "prs": base["pullRequests"]["totalCount"],
        "issues": base["issues"]["totalCount"],
        "repos": repo_count,
        "followers": base["followers"]["totalCount"],
        "contributed_to": base["repositoriesContributedTo"]["totalCount"],
        "streak": streak(days),
        "languages": langs,
    }


def streak(days):
    if not days:
        return 0
    today = datetime.now(timezone.utc).date()
    cursor = today
    if days.get(cursor.isoformat(), 0) == 0:
        cursor -= timedelta(days=1)
    run = 0
    while days.get(cursor.isoformat(), 0) > 0:
        run += 1
        cursor -= timedelta(days=1)
    return run


def human(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M".replace(".0M", "M")
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;")
             .replace(">", "&gt;").replace('"', "&quot;"))


def shell(t, w, h, title, body):
    return f"""<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" fill="none"
     xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{esc(title)}">
  <style>
    .f {{ font-family: {FONT}; }}
    .t {{ font-size: 13px; font-weight: 600; fill: {t['accent']}; letter-spacing: .01em; }}
    .n {{ font-size: 21px; font-weight: 600; fill: {t['value']}; }}
    .l {{ font-size: 10px; font-weight: 500; fill: {t['muted']};
         letter-spacing: .07em; text-transform: uppercase; }}
    .s {{ font-size: 10.5px; fill: {t['muted']}; }}
    .k {{ font-size: 11.5px; font-weight: 500; fill: {t['value']}; }}
  </style>
  <rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="10"
        fill="{t['bg']}" stroke="{t['border']}"/>
  <g class="f">
    <text x="24" y="32" class="t">{esc(title)}</text>
    <line x1="24" y1="44" x2="{w - 24}" y2="44" stroke="{t['border']}"/>
{body}
  </g>
</svg>
"""


def overview_card(t, s):
    w, h = 440, 210
    cells = [
        ("Contributions", s["contributions"]), ("Stars Earned", s["stars"]),
        ("Commits", s["commits"]), ("Pull Requests", s["prs"]),
        ("Repositories", s["repos"]), ("Day Streak", s["streak"]),
    ]
    rows = []
    for i, (label, value) in enumerate(cells):
        x = 24 + (i % 3) * 134
        y = 82 + (i // 3) * 56
        rows.append(f'    <text x="{x}" y="{y}" class="n">{human(value)}</text>')
        rows.append(f'    <text x="{x}" y="{y + 15}" class="l">{esc(label)}</text>')
    rows.append(
        f'    <text x="24" y="{h - 20}" class="s">'
        f'{s["followers"]} followers · {s["contributed_to"]} repositories '
        f'contributed to</text>')
    return shell(t, w, h, "GitHub Activity", "\n".join(rows))


def language_card(t, s):
    w, h = 440, 210
    total = sum(v["size"] for v in s["languages"].values()) or 1
    ranked = sorted(s["languages"].items(), key=lambda kv: -kv[1]["size"])
    top = ranked[:TOP_LANGS]
    rest = sum(v["size"] for _, v in ranked[TOP_LANGS:])
    segments = [(n, v["size"] / total * 100, v["color"]) for n, v in top]
    if rest:
        segments.append(("Other", rest / total * 100, t["muted"]))

    bar_w, bar_x, bar_y = w - 48, 24, 66
    parts, cursor = [], float(bar_x)
    for _, pct, color in segments:
        seg = bar_w * pct / 100
        parts.append(
            f'    <rect x="{cursor:.2f}" y="{bar_y}" width="{max(seg, 0.6):.2f}" '
            f'height="9" fill="{color}"/>')
        cursor += seg
    parts.insert(0, f'    <mask id="bar"><rect x="{bar_x}" y="{bar_y}" '
                    f'width="{bar_w}" height="9" rx="4.5" fill="#fff"/></mask>')
    parts[1:] = [f'  <g mask="url(#bar)">'] + parts[1:] + ['  </g>']

    legend = []
    for i, (name, pct, color) in enumerate(segments):
        x = 24 + (i % 2) * 200
        y = 108 + (i // 2) * 26
        legend.append(f'    <circle cx="{x + 4}" cy="{y - 4}" r="4.5" fill="{color}"/>')
        legend.append(f'    <text x="{x + 16}" y="{y}" class="k">{esc(name)}</text>')
        legend.append(f'    <text x="{x + 176}" y="{y}" class="s" '
                      f'text-anchor="end">{pct:.1f}%</text>')
    return shell(t, w, h, "Language Distribution", "\n".join(parts + legend))


MOCK = {
    "stars": 36, "commits": 1480, "contributions": 2317, "prs": 21,
    "issues": 8, "repos": 22, "followers": 48, "contributed_to": 5, "streak": 14,
    "languages": {
        "Python": {"size": 2_400_000, "color": "#3572A5"},
        "Jupyter Notebook": {"size": 900_000, "color": "#DA5B0B"},
        "TypeScript": {"size": 610_000, "color": "#3178c6"},
        "Svelte": {"size": 320_000, "color": "#ff3e00"},
        "JavaScript": {"size": 240_000, "color": "#f1e05a"},
        "C++": {"size": 150_000, "color": "#f34b7d"},
        "Shell": {"size": 40_000, "color": "#89e051"},
        "HTML": {"size": 30_000, "color": "#e34c26"},
    },
}


def main():
    stats = MOCK if "--mock" in sys.argv else collect()
    OUT.mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        (OUT / f"overview-{name}.svg").write_text(overview_card(theme, stats))
        (OUT / f"languages-{name}.svg").write_text(language_card(theme, stats))
    print(json.dumps({k: v for k, v in stats.items() if k != "languages"}, indent=2))


if __name__ == "__main__":
    main()
