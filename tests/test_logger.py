from pathlib import Path

import logger


def test_start_log_uses_project_log_directory(tmp_path, monkeypatch):
    monkeypatch.setattr(logger, "LOGS_DIR", tmp_path)

    log_file = logger.start_log()
    path = Path(log_file)

    assert path.parent == tmp_path
    assert path.exists()

    logger.save_message(log_file, "You", "hello")
    assert "You: hello" in path.read_text(encoding="utf-8")
