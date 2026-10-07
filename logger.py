import os
from datetime import datetime


def get_log_filename():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"chat_log_{timestamp}.txt"


def save_message(filepath, sender, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {sender}: {message}\n")


def start_log():
    os.makedirs("logs", exist_ok=True)
    filepath = os.path.join("logs", get_log_filename())
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write(f"  ShopEase Chatbot — Session Log\n")
        f.write(f"  Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n\n")
    print(f"  📝 Chat log started: {filepath}\n")
    return filepath