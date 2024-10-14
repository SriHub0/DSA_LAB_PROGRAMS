class Stack:
    def __init__(self):
        self.S = []

    def push(self, element):
        self.S.append(element)

    def is_empty(self):
        return len(self.S) == 0

    def pop(self):
        if not self.is_empty():
            return self.S.pop()
        else:
            return "Cannot pop from an empty stack."

    def size(self):
        return len(self.S)

    def top(self):
        if not self.is_empty():
            return self.S[-1]
        else:
            return "Empty stack"


def is_matched(expr):
    lefty = '({['

    righty = ')}]'

    S = Stack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.is_empty():
                return False
            if righty.index(c) != lefty.index(S.pop()):
                return False
    return S.is_empty()


expr = '(a *{[b + c]/123})'
print(is_matched(expr))