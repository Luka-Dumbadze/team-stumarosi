# AGENTS.md · StumarOSI
AI-native triage and operational engine for boutique hotels. Spec: docs/spec.md

## Commands
install:  pip install -r requirements.txt
run:      uvicorn src.app:app --reload
test:     pytest -q

## Conventions
- Model selected via STUMAROSI_MODEL, default google/gemini-2.5-flash
- Every model call goes through src/llm.py and logs token usage and latency
- Times are ISO 8601 with timezone offset (+04:00 for Asia/Tbilisi)
- Error shape is always {"error": "<message>", "field": "<field_name>"}
- Every new endpoint ships with a unit test in tests/

## Always
- Run the test command before saying you are done, and paste the result

## Ask first
- Adding a dependency
- Changing a public response shape
- Editing CI configuration

## Never
- Read or write .env, or print an API key
- Delete, skip, or weaken a test to make it pass
- Overwrite or mutate data/rooms.json directly from an agent