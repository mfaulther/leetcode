#https://leetcode.com/problems/design-circular-queue
class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.L = k*[0]
        self.front = 0
        self.rear = -1 
        self.size = 0 

        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if (self.isFull()):
            return False
        self.rear = (self.rear + 1) % len(self.L)
        self.L[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if (self.isEmpty()):
            return False
        self.front += 1
        self.size -= 1
        return True
        
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if (self.isEmpty()):
            return -1
        return self.L[self.front]
        
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.L[self.rear]
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == len(self.L)
