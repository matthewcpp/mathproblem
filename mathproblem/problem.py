from typing import List

class Problem:
    """A generated math problem"""

    def __init__(self):
        self.prompt: str
        self.steps: List[str] = list()
        self.diagram: List[str] = list()
        self.answer: str
        self.level: int = 0
