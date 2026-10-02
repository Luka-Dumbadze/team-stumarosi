import json
import logging
from types import SimpleNamespace
from src import llm

def test_every_model_call_logs_usage(monkeypatch, caplog):  # AC4
    fake_resp = SimpleNamespace(
        usage=SimpleNamespace(prompt_tokens=450, completion_tokens=120),
        choices=[SimpleNamespace(message=SimpleNamespace(content="Task extracted successfully."))],
    )
    fake_client = SimpleNamespace(chat=SimpleNamespace(completions=SimpleNamespace(create=lambda **kw: fake_resp)))
    monkeypatch.setattr(llm, "client", lambda: fake_client)

    with caplog.at_level(logging.INFO, logger="stumarosi.llm"):
        answer, usage = llm.chat("system prompt", "guest message")

    assert answer == "Task extracted successfully."
    assert len(caplog.records) > 0
    logged = json.loads(caplog.records[-1].getMessage().split("model_call ", 1)[1])
    assert set(logged) == {"model", "tokens_in", "tokens_out", "cost_usd", "latency_ms"}
    assert logged["tokens_in"] == 450
    assert logged["tokens_out"] == 120
    assert logged["cost_usd"] == round((450 * llm.PRICE_IN_PER_M + 120 * llm.PRICE_OUT_PER_M) / 1_000_000, 6)