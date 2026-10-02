# 0001 · Call models through OpenRouter gateway, model ID from environment

**Date:** Week 2 · **Decided by:** team-stumaros ([Your Name], Mariam, Giorgi)

**Context.** We need to support model routing (e.g. Gemini 2.5 Flash for entity extraction, Jev for fast System-1 triage, Claude for dispute escalation) without rewriting application code. Additionally, every model call must log cost, token usage, and latency.

**Decision.** All model calls go through `src/llm.py` using the OpenAI SDK configured with the OpenRouter base URL. The default model is loaded from the environment variable `STUMAROSI_MODEL` (default: `google/gemini-2.5-flash`).

**Alternatives.** 
1. Using provider-specific SDKs (google-generativeai, anthropic): rejected due to vendor lock-in and duplicate usage logging logic.
2. Hardcoding model strings in business logic: rejected because model prices and versions change frequently.

**Consequences.** Centralized logging and fallback handling in one file. We depend on OpenRouter uptime, which will be mitigated by our Week 10 fallback chain.