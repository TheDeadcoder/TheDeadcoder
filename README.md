<h1 align="center">Nazmus Sakib</h1>

<p align="center">
  <b>Reinforcement Learning for LLM Post-Training · RL Environment Design · Applied AI Systems</b>
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

I work on reinforcement learning for language model post-training — reward design, GRPO and its
variants, and the custom environments that make verifiable RL possible in domains where no
benchmark exists yet. My interest is in the part of the problem that is usually skipped: building
the simulator, the verifier, and the reward signal, then measuring honestly whether RL earned its
compute over supervised fine-tuning.

Alongside that, I build production AI systems — retrieval pipelines, agentic backends, and
inference stacks — and I care about low-resource language evaluation, particularly Bengali.

CSE, BUET (CGPA 3.82/4.00). Based in Dhaka, open to remote research collaboration.

---

## Research Focus

| Area | What I work on |
|---|---|
| **RL post-training** | GRPO and variants (DAPO, Dr. GRPO, GSPO, RLOO); multi-signal reward design; measuring RL headroom over SFT |
| **RL environments** | Physics-grounded simulators, verifiable reward harnesses, OpenEnv-compatible environments |
| **Reliability & systems agents** | Fault-injection scenarios, incident-resolution benchmarks, agents that operate infrastructure |
| **Low-resource evaluation** | Adversarial safety datasets and cross-lingual failure analysis for Bengali |

---

## Publication

**MemAgent: A Cache-Inspired Framework for Augmenting Conversational Web Agents with Task-Specific Information**
*N. Sakib, P. Barai, S. I. Parisa, A. Iqbal* — WOA 2025, 26th Workshop *From Objects to Agents*, Trento, Italy.
[CEUR-WS Vol-4028, Paper 8](https://ceur-ws.org/Vol-4028/paper8.pdf)

A cache-inspired Memory Cache Bank with time-based expiration that decouples information gathering
from task execution in web agents. Reduces average conversation turns by 22.4% (5.00 → 3.88) across
150 Mind2Web tasks; a 15-participant study showed a 58% reduction in completion time for recurring tasks.

---

## Selected Repositories

### Reinforcement Learning & LLM Post-Training

| Repository | Description | Stack |
|---|---|---|
| **[dc_ops_environment](https://github.com/TheDeadcoder/dc_ops_environment)** | Physics-grounded datacenter RL environment — RC thermal networks and continuous multi-objective rewards, built on OpenEnv | OpenEnv · Physics sim |
| **[dc_ops_training](https://github.com/TheDeadcoder/dc_ops_training)** | Teacher-distilled SFT → GRPO pipeline on AMD MI300X. Multi-signal reward (physics, scenario heuristics, anti-looping, format) drove +188% composite reward and a 10× per-step gain on hard multi-fault scenarios | GRPO · TRL · Unsloth · vLLM · ROCm |
| **[GeoQL-4B](https://github.com/TheDeadcoder/GeoQL-4B)** | Text-to-OverpassQL via SFT → GRPO on Qwen3-4B, with a documented negative result on reward redundancy in reference-based reward design | GRPO · Qwen3 · vLLM |
| **[medical-cot-assistant](https://github.com/TheDeadcoder/medical-cot-assistant)** | Clinical chain-of-thought fine-tuning of a 20B model with QAT and LLM-as-a-Judge evaluation; INT4 + GGUF export for local inference | Unsloth · QAT · llama.cpp |

### Applied Deep Learning

| Repository | Description | Stack |
|---|---|---|
| **[bd-prescription-medicine-recognize](https://github.com/TheDeadcoder/bd-prescription-medicine-recognize)** | ResNet50–CRNN for 78-class handwritten medicine-name recognition on Bangladeshi prescriptions. Hash-grouped StratifiedGroupKFold + SWA ensemble reached 92.53% test accuracy / 0.9234 macro-F1 (+6.44 pt over baseline) | PyTorch · CRNN · SWA · MLflow · Grad-CAM |

### Agentic AI & Retrieval Systems

| Repository | Description | Stack |
|---|---|---|
| **[civilmate-backend](https://github.com/TheDeadcoder/civilmate-backend)** | Agentic GraphRAG over building codes; compares design drawings against site imagery to generate technical logs | Neo4j · Qdrant · FastAPI |
| **[InsightAI-python-backend](https://github.com/TheDeadcoder/InsightAI-python-backend)** | Microservices EdTech platform — quiz/flashcard generation from PDFs and video, plus CLIP-based multimodal product search | LlamaIndex · Qdrant · CLIP · FastAPI |
| **[Tokkhok-Backend](https://github.com/TheDeadcoder/Tokkhok-Backend)** | Personalised RAG chatbot for "Banglish" (romanised Bengali) with a custom transliteration pipeline and configurable personas | FastAPI · Qdrant · PostgreSQL |
| **[sust-backend](https://github.com/TheDeadcoder/sust-backend)** | Bebsha AI service layer — RAG product search, description generation, background removal | Flask · RAG |

### Systems & Reliability

| Repository | Description | Stack |
|---|---|---|
| **[SREGym](https://github.com/TheDeadcoder/SREGym)** | Contributed fault-injection scenarios to an incident-resolution benchmark for AI agents — Kafka poison-pill head-of-line blocking, CFS throttling brownout, and oscillating config corruption | Kubernetes · Kafka · Chaos engineering |

### Full-Stack Products

| Repository | Description | Stack |
|---|---|---|
| **[nerdherd2ndrun](https://github.com/TheDeadcoder/nerdherd2ndrun)** | Collaborative productivity platform — shared notes, video calls, real-time quizzes, AI assistant | SvelteKit · Firebase |
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
| Lecturer, CSE | **BRAC University** · 2025– | Machine Learning, Operating Systems, Software Engineering, System Analysis & Design |
| Founding Engineer (Backend & AI) | **Intellesphere** · 2024–25 | Banking RAG with hybrid indexing, CLIP multimodal search, multimodal civil-engineering automation |
| Founding Engineer (Backend & AI) | **Oleyn** · 2024 | Bengali ASR with NeMo diarization, AI CRM, legal research assistant |
| Software Engineer (Backend) | **Priyo** · 2024 | Django support agent at concurrency, warehousing APIs, campaign infrastructure |
| Software Engineer Intern | **Yobo** · 2024 | Text-to-SQL chat interface on LangChain and FastAPI |

---

## Technical Stack

| Domain | Tools |
|---|---|
| **Languages** | Python · C++ · Java · TypeScript · JavaScript · SQL |
| **Training & Inference** | PyTorch · TRL · Unsloth · PEFT/LoRA · vLLM · llama.cpp · ROCm · Transformers · NeMo |
| **RL** | GRPO family (DAPO, Dr. GRPO, GSPO, RLOO) · reward design · custom environments · OpenEnv |
| **LLM Systems** | RAG · GraphRAG · LangChain · LlamaIndex · agentic pipelines · evaluation harnesses |
| **Backend** | FastAPI · Django · Spring Boot · Express · AWS Lambda · Firebase Functions |
| **Data** | PostgreSQL · MySQL · Redis · Qdrant · ChromaDB · Neo4j · Supabase |
| **Infrastructure** | Docker · Kubernetes · Terraform · AWS · GCP · Modal · Nginx · GitHub Actions |
| **Frontend** | Next.js · React · SvelteKit · Flutter · Tailwind CSS |

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

<p align="center"><sub>Rendered nightly by a GitHub Action and committed to this repository — no third-party service, no rate limits.</sub></p>

---

## Selected Honours

| Award | Event | Year |
|---|---|---|
| Champion | IUT 11th National ICT Fest — OpenAPI Hackathon | 2024 |
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
