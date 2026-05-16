from datetime import datetime

class FileLogger:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def log(self, message: str) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {message}\n"
        with open(self.filepath, "a", encoding="utf-8") as f:
            f.write(entry)

    def read_logs(self) -> list[str]:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []