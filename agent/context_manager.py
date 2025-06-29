import os
import json
from typing import List

CONTEXT_FILE = '/workspace/context.json'
MAX_CONTEXT_SIZE = 1000000  # 1M tokens (approx chars)

class ContextManager:
    def __init__(self, context_file=CONTEXT_FILE):
        self.context_file = context_file
        self.context: List[dict] = []
        self.load()

    def load(self):
        if os.path.exists(self.context_file):
            with open(self.context_file, 'r') as f:
                self.context = json.load(f)
        else:
            self.context = []

    def save(self):
        with open(self.context_file, 'w') as f:
            json.dump(self.context, f)

    def add(self, entry: dict):
        self.context.append(entry)
        self.prune()
        self.save()

    def prune(self):
        # Prune oldest entries if context is too large
        while self.size() > MAX_CONTEXT_SIZE:
            self.context.pop(0)

    def size(self):
        return sum(len(json.dumps(e)) for e in self.context)

    def get_context(self):
        return self.context 