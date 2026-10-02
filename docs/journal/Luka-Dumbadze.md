# Pattern Journal · [Your Name]

## Week 1 · Context as Budget
Applied in StumarOSI triage engine model selection. Delegated token and cost estimation across OpenRouter models (Claude 3.5 Sonnet vs Gemini 2.5 Flash) for 600 daily hotel requests. Verified by calculating monthly cost differences ($3.16/mo vs $70+/mo) and choosing Flash to preserve margin while staying within latency constraints.

## Week 2 · Spec Before Code
Applied in defining First Slice for Lab 2 (AC2 and AC3 room lookup). Delegated the implementation to an agent using plan-first mode. Caught that the agent attempted to swallow room not found errors with an empty 200 JSON; verified the fix by writing `test_nonexistent_room_returns_422_with_error_shape` before re-delegating the code.

## Week 3 · Uncertainty-Aware UX

## Week 4 · Grounded Generation