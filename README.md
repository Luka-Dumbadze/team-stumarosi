# StumarOSI

**AI-Native Hotel Web Operating System for Autonomous Guest Triage & Task Management.**  
CS6920 capstone · Fall 2026 · team-stumaros · Luka Dumbadze, Mariam, Giorgi

> Status: Week 2 · First Slice (Room Lookup & LLM Gateway) operational

## The problem
Front-desk staff at boutique hotels are overwhelmed by unstructured, multi-intent guest requests across multiple channels. Manual triage leads to lost maintenance tickets, delayed housekeeping, and high operational burnout.

## Run it
```bash
# Setup virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run test suite
pytest -q
```

## How it works
- **System 1 Fast Triage:** Non-autoregressive decision classification (TypeSafe Jev) for sub-100ms emergency and chatter filtering.
- **System 2 Structured Extraction:** Gemini 2.5 Flash / GPT-4o-mini via OpenRouter gateway (`src/llm.py`) extracting validated Pydantic work orders.
- **Room Registry:** Local JSON-backed room and occupancy verification (`data/rooms.json`).

Key architectural decisions: [docs/decisions/](docs/decisions/)

## Does it work? (evidence)
| What we measure | Result | Where |
|---|---|---|
| Unit tests | 4 passed | tests/ |
| Model usage logging | tokens in/out, latency_ms, cost_usd | logs/usage.jsonl |
| Error shape | {"error": ..., "field": ...} | src/app.py |

## Team and how we work
- Luka Dumbadze (Repo keeper)
- Mariam (Spec keeper)
- Giorgi (Eval keeper)

Rules: [docs/TEAM-REPO.md](docs/TEAM-REPO.md) · Spec: [docs/spec.md](docs/spec.md) · Delegation log: [docs/delegation-log.md](docs/delegation-log.md) · Contract: [TEAM-CONTRACT.md](TEAM-CONTRACT.md)
