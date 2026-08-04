<h1 align="center">Nazmus Sakib</h1>

<p align="center">
  <b>AI Engineer &amp; Researcher</b>
</p>

<p align="center">
  RL post-training · Agentic systems · Full-stack AI products
</p>

<p align="center">
  <a href="https://portfolio.nazmus-sakib-touhid.app/"><img src="https://img.shields.io/badge/Portfolio-1f2328?style=flat-square&logo=readdotcv&logoColor=white" alt="Portfolio"></a>
  <a href="https://ceur-ws.org/Vol-4028/paper8.pdf"><img src="https://img.shields.io/badge/Publication-1f2328?style=flat-square&logo=googlescholar&logoColor=white" alt="Publication"></a>
  <a href="https://huggingface.co/Melikshah"><img src="https://img.shields.io/badge/Hugging%20Face-1f2328?style=flat-square&logo=huggingface&logoColor=FFD21E" alt="Hugging Face"></a>
  <a href="https://linkedin.com/in/nazmus-sakib-touhid-a43533205"><img src="https://img.shields.io/badge/LinkedIn-1f2328?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://codeforces.com/profile/melikshah"><img src="https://img.shields.io/badge/Codeforces-1f2328?style=flat-square&logo=codeforces&logoColor=white" alt="Codeforces"></a>
  <a href="mailto:sakibbuet2k19@gmail.com"><img src="https://img.shields.io/badge/Email-1f2328?style=flat-square&logo=maildotru&logoColor=white" alt="Email"></a>
</p>

---

## About

I build language-model systems end to end - the reinforcement learning that trains a policy, the
agent architecture that puts it to work, and the product it ships inside.

My research is in RL post-training: reward design, GRPO and its variants, and the custom environments
that make verifiable RL possible in domains where no benchmark exists yet. I'm drawn to the part
usually skipped - building the simulator, the verifier and the reward signal, then measuring
honestly whether RL earned its compute over supervised fine-tuning.

The engineering half is agentic. Memory architectures that let agents carry context across sessions
(the subject of my WOA 2025 paper), tool calling and multi-step orchestration, graph and hybrid
retrieval, and the adversarial testing that shows where those tool chains break. Around all of it
sits the ordinary work that decides whether a model ever reaches a user: inference services, vector
search, auth, payments, realtime web and mobile clients, and the CI that ships them. I also care
about low-resource language evaluation, particularly Bengali.

CSE, BUET. Based in Dhaka, open to remote research collaboration.

---

## What I Work On

| Layer | Focus |
|---|---|
| **Research - RL post-training** | GRPO and variants (DAPO, Dr. GRPO, GSPO, RLOO) · multi-signal reward design · physics-grounded and verifiable environments · measuring RL headroom over SFT |
| **Agentic systems** | Agent memory architectures · tool calling and multi-step orchestration · GraphRAG and hybrid retrieval · structured output and evaluation harnesses · adversarial testing of agent tool chains |
| **Full-stack delivery** | Inference services and quantised local deployment · vector search · auth, payments and background jobs · Next.js / SvelteKit / Flutter clients · Docker and GitHub Actions |
| **Reliability & evaluation** | Fault-injection scenarios for incident-resolution benchmarks · adversarial safety datasets for Bengali and other low-resource languages |

---

## Publication

**MemAgent: A Cache-Inspired Framework for Augmenting Conversational Web Agents with Task-Specific Information**
*N. Sakib, P. Barai, S. I. Parisa, A. Iqbal* - WOA 2025, 26th Workshop *From Objects to Agents*, Trento, Italy.
[CEUR-WS Vol-4028, Paper 8](https://ceur-ws.org/Vol-4028/paper8.pdf)

An agent memory architecture: a Memory Cache Bank with time-based expiration that decouples
information gathering from task execution, so an agent stops re-asking users for details it has
already learned. Reduces average conversation turns by 22.4% (5.00 → 3.88) across 150 Mind2Web
tasks; a 15-participant study showed a 58% reduction in completion time for recurring tasks.

---

## Selected Repositories

### Reinforcement Learning & LLM Post-Training

| Repository | Description | Stack |
|---|---|---|
| **[dc_ops_environment](https://github.com/TheDeadcoder/dc_ops_environment)** | Physics-grounded datacenter RL environment - RC thermal networks and continuous multi-objective rewards, built on OpenEnv | OpenEnv · Physics sim |
| **[dc_ops_training](https://github.com/TheDeadcoder/dc_ops_training)** | Teacher-distilled SFT → GRPO pipeline on AMD MI300X. Multi-signal reward (physics, scenario heuristics, anti-looping, format) drove +188% composite reward and a 10× per-step gain on hard multi-fault scenarios | GRPO · TRL · Unsloth · vLLM · ROCm |
| **[GeoQL-4B](https://github.com/TheDeadcoder/GeoQL-4B)** | Text-to-OverpassQL via SFT → GRPO on Qwen3-4B, with a documented negative result on reward redundancy in reference-based reward design | GRPO · Qwen3 · vLLM |
| **[medical-cot-assistant](https://github.com/TheDeadcoder/medical-cot-assistant)** | Clinical chain-of-thought fine-tuning of a 20B model with QAT and LLM-as-a-Judge evaluation; INT4 + GGUF export for local inference | Unsloth · QAT · llama.cpp |

### Agentic Systems & Retrieval

| Repository | Description | Stack |
|---|---|---|
| **[civilmate-backend](https://github.com/TheDeadcoder/civilmate-backend)** | Agentic GraphRAG over building codes - plans multi-step lookups across a code graph, then compares design drawings against site imagery to generate technical logs and blocker alerts | Neo4j · Qdrant · FastAPI |
| **[InsightAI-python-backend](https://github.com/TheDeadcoder/InsightAI-python-backend)** | Microservices AI platform - tool-routed generation of quizzes and flashcards from PDFs and video, enforced structured output, and CLIP-based multimodal product search | LlamaIndex · Qdrant · CLIP · FastAPI |
| **[Tokkhok-Backend](https://github.com/TheDeadcoder/Tokkhok-Backend)** | Personalised RAG chatbot for "Banglish" (romanised Bengali) with a custom transliteration pipeline, few-shot inference and configurable agent personas | FastAPI · Qdrant · PostgreSQL |
| **[sust-backend](https://github.com/TheDeadcoder/sust-backend)** | Bebsha AI service layer - RAG product search, description generation, background removal | Flask · RAG |

### Applied Deep Learning

| Repository | Description | Stack |
|---|---|---|
| **[bd-prescription-medicine-recognize](https://github.com/TheDeadcoder/bd-prescription-medicine-recognize)** | ResNet50–CRNN for 78-class handwritten medicine-name recognition on Bangladeshi prescriptions. Hash-grouped StratifiedGroupKFold + SWA ensemble reached 92.53% test accuracy / 0.9234 macro-F1 (+6.44 pt over baseline) | PyTorch · CRNN · SWA · MLflow · Grad-CAM |

### Systems & Reliability

| Repository | Description | Stack |
|---|---|---|
| **[SREGym](https://github.com/TheDeadcoder/SREGym)** | Contributed fault-injection scenarios to an incident-resolution benchmark for AI agents - Kafka poison-pill head-of-line blocking, CFS throttling brownout, and oscillating config corruption | Kubernetes · Kafka · Chaos engineering |

### Full-Stack Products

| Repository | Description | Stack |
|---|---|---|
| **[nerdherd2ndrun](https://github.com/TheDeadcoder/nerdherd2ndrun)** | Collaborative productivity platform - shared notes, video calls, real-time quizzes, AI assistant | SvelteKit · Firebase |
| **[coderhub](https://github.com/TheDeadcoder/coderhub)** | Developer community platform with blogging, skill-based search, and project management | SvelteKit · Vercel |
| **[yobofrontend](https://github.com/TheDeadcoder/yobofrontend)** | Frontend for YoboSQL, a text-to-SQL conversational interface | TypeScript · SvelteKit |

### Engineering Templates

| Repository | Description | Stack |
|---|---|---|
| **[django-init-template](https://github.com/TheDeadcoder/django-init-template)** | Production-ready Django REST scaffold with PostgreSQL and Supabase auth | Django · DRF · Supabase |
| **[nodejs-init](https://github.com/TheDeadcoder/nodejs-init)** | Express + TypeScript service scaffold with Helmet, Swagger, and Supabase auth | TypeScript · Express |

---

## Open Models & Datasets

Published on [Hugging Face @Melikshah](https://huggingface.co/Melikshah).

| Artifact | Description |
|---|---|
| **GPT-OSS-20B-Clinical-CoT (GGUF)** | 4-bit quantised 20B model fine-tuned for clinical chain-of-thought reasoning, optimised for local inference |
| **dc_ops_grpo_lora** | GRPO-trained LoRA adapter for the datacenter operations environment |
| **qwen3.5-4b-base-blindspots** | Adversarial evaluation set probing architectural and logical failure modes of Qwen3.5-4B-Base |
| **Shajgoj & General Products** | 20,000+ item multimodal datasets for image–text retrieval |
| **Prothom Alo News** | Large-scale Bengali news corpus for low-resource NLP research |

---

## Experience

| Role | Organisation | Focus |
|---|---|---|
| Lecturer, CSE | **BRAC University** · present | Machine Learning, Operating Systems, Software Engineering, System Analysis & Design |
| Founding Engineer (Backend & AI) | **Intellesphere** · 2024–25 | Banking RAG with hybrid indexing and Keycloak-secured access, CLIP multimodal search, multimodal civil-engineering automation |
| Founding Engineer (Backend & AI) | **Oleyn** · 2024 | Bengali ASR with NeMo speaker diarization, agentic CRM and campaign system, legal research assistant |
| Software Engineer (Backend) | **Priyo** · 2024 | Django support agent at concurrency, warehousing REST APIs, campaign and analytics infrastructure |
| Software Engineer Intern | **Yobo** · 2024 | Text-to-SQL chat interface on LangChain, FastAPI and SvelteKit |

---

## Technical Stack

| Domain | Tools |
|---|---|
| **Languages** | Python · C++ · Java · TypeScript · JavaScript · SQL |
| **Training & Inference** | PyTorch · TRL · Unsloth · PEFT/LoRA · vLLM · llama.cpp · ROCm · Transformers · NeMo · scikit-learn · MLflow |
| **Reinforcement Learning** | GRPO family (DAPO, Dr. GRPO, GSPO, RLOO) · reward design · custom verifiable environments · OpenEnv |
| **Agentic Systems** | Tool calling · agent memory · multi-step orchestration · LangChain · LlamaIndex · Genkit · RAG · GraphRAG · hybrid retrieval · structured output · eval harnesses |
| **Backend & APIs** | FastAPI · Django · Spring Boot · Express · Firebase Cloud Functions · Nginx · Keycloak · Stripe |
| **Frontend & Mobile** | Next.js · React · SvelteKit · Flutter · Tailwind CSS |
| **Data & Vector Stores** | PostgreSQL · MySQL · Redis · Qdrant · ChromaDB · Neo4j · Supabase · Turso |
| **Infrastructure** | Docker · Kubernetes · AWS · GCP · Vercel · Modal · GitHub Actions · PostHog |

---

## GitHub Activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TheDeadcoder/TheDeadcoder/main/assets/overview-dark.svg">
    <img alt="GitHub activity overview" src="https://raw.githubusercontent.com/TheDeadcoder/TheDeadcoder/main/assets/overview-light.svg" width="49%">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/TheDeadcoder/TheDeadcoder/main/assets/languages-dark.svg">
    <img alt="Language distribution" src="https://raw.githubusercontent.com/TheDeadcoder/TheDeadcoder/main/assets/languages-light.svg" width="49%">
  </picture>
</p>

<p align="center"><sub>Rendered nightly by a GitHub Action and committed to this repository - no third-party service, no rate limits.</sub></p>

---

## Selected Honours

| Award | Event | Year |
|---|---|---|
| Champion | IUT 11th National ICT Fest - OpenAPI Hackathon | 2024 |
| Champion | CodeCrafters Dev Sprint Hackathon, BUET | 2024 |
| Champion | SUST CSE Carnival Hackathon | 2024 |
| Runner-Up | Gen-Dev Hackathon, Acme AI | 2024 |
| Honourable Mention | Bangladesh Blockchain Olympiad (BCOLBD) · IDSOL World Finalist | 2024 |
| Champion | Cefalo ITverse Project Showcase | 2023 |

---

<p align="center">
  <sub>
    <a href="https://portfolio.nazmus-sakib-touhid.app/projects">Projects</a> ·
    <a href="https://huggingface.co/Melikshah">Models</a> ·
    <a href="mailto:sakibbuet2k19@gmail.com">Get in touch</a>
  </sub>
</p>
