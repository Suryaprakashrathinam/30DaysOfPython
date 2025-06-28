class SafeFileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"Opened file: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"Closed file: {self.filename}")
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return False

try:
    with SafeFileHandler("love.txt", "r") as f:
        data = f.read()
        print(data)
except Exception as e:
    print("Handled exception:", e)
