from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
LOGS_DIR = PROJECT_ROOT / "logs"


def get_log_filename():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"chat_log_{timestamp}.txt"


def save_message(filepath, sender, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {sender}: {message}\n")


def start_log():
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    filepath = LOGS_DIR / get_log_filename()

    with filepath.open("w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("  ShopEase Chatbot — Session Log\n")
        f.write(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")

    print(f"  📝 Chat log started: {filepath}\n")
    return str(filepath)
