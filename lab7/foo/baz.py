b=58

class NotAnIntegerListException(Exception):
    pass

class Baz:
    def __init__(self, items):
        for item in items:
            if type(item) != int: raise NotAnIntegerListException("NotAnIntegerList")
        self.items = items[1:-1]
    def sum(self):
        return sum(self.items) + b
