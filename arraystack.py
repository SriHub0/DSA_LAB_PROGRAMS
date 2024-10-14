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
ST = Stack()
ST.push(0)
ST.push(1)
ST.push(2)
ST.push(3)
ST.push(4)
print("Stack size: ",ST.size())
print("Top Element: ",ST.top())
popped_item = ST.pop()
print("\n Popped item:",popped_item)
print("\n Stack size:",ST.size())
print("Top element:",ST.top())