__all__ = "Mumbo"


class Mumbo:
    def __init__(self, name):
        self.name = name
        self.samples = []

    def __repr__(self):
        return f"Mumbo({self.name})"
