class Deque:
    def __init__(self):
        self.items = []
    def is_Empty(self):
        return self.items == []
    def add_Rear(self,item):
        self.items.append(item)
    def add_Front(self,item):
        return self.items.insert(0,item)
    def remove_Front(self):
        return self.items.pop(0)
    def remove_Rear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
D = Deque()
print(D.is_Empty())
D.add_Rear(8)
D.add_Rear(5)
D.add_Front(7)
D.add_Front(10)
print(D.size())
print(D.is_Empty())
D.add_Rear(11)
print(D.remove_Rear())
print(D.remove_Front())
D.add_Front(55)
D.add_Rear(45)
print(D.items)