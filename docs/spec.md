# StumarOSI · Spec v1

## Goal
Turn the hotel operations triage spec into a verified FastAPI service. Users: boutique hotel front-desk staff handling messy inbound guest requests from a phone or web dashboard.

## Acceptance criteria
- AC1  POST /triage {message, room_number?} decomposes multi-intent guest requests into structured Pydantic tasks (Department, Urgency, Action)
- AC2  GET /rooms/{room_number} returns room occupancy and status from data/rooms.json
- AC3  invalid room_number (non-existent or not an integer) returns 422 with {"error": ..., "field": "room_number"}
- AC4  every model call logs model, tokens in/out, cost_usd, latency_ms to logs/usage.jsonl
- AC5  p95 latency of /triage under 2.5 s

## Context the agent needs
data/rooms.json · AGENTS.md · docs/decisions/0001-openrouter-gateway.md

## Constraints
Python 3.11 · FastAPI · OpenRouter via openai SDK · model id from env STUMAROSI_MODEL (default: google/gemini-2.5-flash)

## Out of scope
Desktop window OS frontend · Real WhatsApp webhooks · Database migrations (PostgreSQL comes in W6+) · Payment processing

## Verification
pytest green locally and in GitHub Actions · 3 golden questions pass (evals/golden.md)

## First slice (Lab 2)
Criteria: AC2, AC3
Done when: tests/test_rooms.py and tests/test_llm.py pass locally and in CI
Not in this slice: AC1, AC5 (scheduled for slice 2)