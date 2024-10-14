class Queue():
    def __init__(self,size):
        self.max_size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self,data):
        if(self.rear == self.max_size-1):
            print("the queue is full \n")
        elif(self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = self.rear +1
            self.queue[self.rear]= data
    def dequeue(self):
        if(self.front == -1):
            print("the queue is empty \n")
        else:
            temp = self.queue[self.front]
            self.front = self.front + 1
            return temp
    def printQueue(self):
        if(self.front == -1):
            print("No element in the queue")
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end = " ")
Q = Queue(5)
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
