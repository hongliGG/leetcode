class MyCircularQueue:
    
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [""] * k
        self.max_length = k
        self.start = -1
        self.end = -1


    def enQueue(self, value: int):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        插入元素时，如果是第一个元素，那么start end 都变成 0

        如果不是第一个元素，队尾延长，end + 1，注意是循环的队列所以需要%最大长度

        如果队列已经满了，就返回False
        """
        if not self.isFull():
            if self.start == -1:
                self.start, self.end = 0, 0
            else:
                self.end = (self.end + 1) % self.max_length
            self.queue[self.end] = value
            return True
        else:
            return False
            

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        
        如果是最后一个元素，那么start end 都变成-1

        如果不是最后一个元素，队头出队，start + 1， 同样注意循环

        如果队列是空的，就返回Flase
        """
        if not self.isEmpty():
            if self.start == self.end:
                self.start, self.end == -1, -1
            else:
                self.start = (self.start + 1) % self.max_length
            return True
        else:
            return False        
        

    def Front(self):
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.queue[self.start]
        

    def Rear(self):
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.queue[self.end]
        

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        """
        return self.start == -1 and self.end == -1
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        如果end的下一位是start，就代表已经full
        """
        return (self.end + 1) % self.max_length == self.start


circularQueue = MyCircularQueue(3); 
res1 = circularQueue.enQueue(1);
print(res1) 
res2 = circularQueue.enQueue(2); 
print(res2)
res3 = circularQueue.enQueue(3); 
print(res3)
res4 = circularQueue.enQueue(4); 
print(res4)
res5 = circularQueue.Rear();  
print(res5)
res6 = circularQueue.isFull();  
print(res6)
res7 = circularQueue.deQueue();  
print(res7)
res8 = circularQueue.enQueue(4);  
print(res8)
res9 = circularQueue.Rear(); 
print(res9)