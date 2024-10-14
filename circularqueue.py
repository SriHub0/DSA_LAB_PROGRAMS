class MyCircularQueue():
    def __init__(self, size):
        self.max_size = size
        self.queue = [None] * self.max_size
        self.front = self.rear = -1

    def enqueue(self, data):
        if((self.rear +1) % self.max_size == self.front):
            print("the circular queue is full \n")
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear +1) % self.max_size
            self.queue[self.rear] = data
    def dequeue(self):
        if(self.front == -1):
            print("the circular queue is empty \n")
        elif(self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front +1) % self.max_size
            return temp
    def printQueue(self):
        if(self.front == -1):
                print("no element in the circular queue")
        elif(self.rear >= self.front):
            for i in range(self.front,self.rear + 1):
                print(self.queue[i],end = " ")
            print()
        else:
            for i in range(self.front,self.max_size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear + 1):
                print(self.queue[i],end = " ")
            print()
Q = MyCircularQueue(5)
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(5)
print("initial queue")
Q.printQueue()
Q.dequeue()
print("after removing an element from the queue")
Q.printQueue()