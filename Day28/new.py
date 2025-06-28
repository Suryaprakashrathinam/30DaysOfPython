from pathlib import Path
from typing import Optional

class SafeFileHandler:
    """
    Context manager for safe file operations with automatic open/close and error handling.
    """

    def __init__(self, filename: str | Path, mode: str = "r", encoding: Optional[str] = "utf-8"):
        self.filename = Path(filename)
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            return self.file
        except Exception as e:
            print(f"[ERROR] Failed to open file '{self.filename}': {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            try:
                self.file.close()
            except Exception as e:
                print(f"[ERROR] Failed to close file '{self.filename}': {e}")
        if exc_type:
            print(f"[ERROR] Exception during file handling: {exc_val}")
        return False  # Reraise the exception if occurred

try:
    with SafeFileHandler("love.txt", "r") as f:
        data = f.read()
        print(data)
except Exception as e:
    print("[Handled Exception]", e)
