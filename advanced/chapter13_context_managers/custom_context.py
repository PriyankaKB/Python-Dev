# custom_context.py
# Examples and explanations for custom context managers

class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with FileOpener('myfile.txt', 'w') as f:
    f.write('Hello from custom context manager!')
