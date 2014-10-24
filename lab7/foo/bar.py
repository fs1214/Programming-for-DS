a=5

class Bar:
    def __init__(self, items):
        self.items = items[1:-1]
    def sum(self):
        return sum(self.items)
