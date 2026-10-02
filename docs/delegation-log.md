# Delegation log · StumarOSI

One entry per delegation that mattered. Two minutes each. Honest beats heroic.

---

### Entry 1 · Scaffold the service and OpenRouter gateway
- **Task:** FastAPI app, llm.py with usage logging, test fixtures, and CI (AC4)
- **Delegated to:** Claude Code, spec v1 + AGENTS.md v2
- **Plan check:** The agent forgot to handle the custom exception handler for FastAPI validation errors. Added it to the plan before approving.
- **Came back wrong:** Attempted to add `requests` library to requirements.txt instead of using `httpx`.
- **Caught by:** Reading the diff of requirements.txt (AGENTS.md: dependencies are "ask first").
- **Decision:** Removed `requests`, kept `httpx`, approved plan.
- **AGENTS.md change:** None; the convention worked as intended.
- **Cost:** 5 minutes review.

### Entry 2 · GET /rooms/{room_number} (AC2, AC3)
- **Task:** Room lookup endpoint from data/rooms.json with 422 error shape
- **Delegated to:** Claude Code, docs/spec.md
- **Plan check:** Approved as proposed.
- **Came back wrong:** The agent wrote `except Exception: return {}` which swallowed room lookup errors and returned empty success 200 instead of 422. Test was initially asserting `r.status_code != 500`.
- **Caught by:** Reading tests/ before src/. Test was too weak to prove 422 behavior.
- **Decision:** Rejected. Wrote the explicit test for `Room 999 -> 422` with exact error keys, re-delegated, and tests passed.
- **AGENTS.md change:** Added explicit rule: "Error paths return our error shape, not an empty success".
- **Cost:** 8 minutes, one extra iteration.