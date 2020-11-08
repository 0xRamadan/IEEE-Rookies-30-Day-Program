# IEEE_Rookies_task_16_part_02
# name: Mahmoud_Ramadan
# task: Ring Buffer / circular queue

"""
Circular queue is linear data structure (FIFO)
Operations on Circular Queue:

Front: Get the front item from queue.
Rear: Get the last item from queue.
enQueue(value): This function is used to insert an element into the circular queue.
                In a circular queue, the new element is always inserted at Rear position.
deQueue(): This function is used to delete an element from the circular queue.
            In a circular queue, the element is always deleted from front position.
display(): display the element inside the queue.

"""


class CircularQueue:

    # constructor
    def __init__(self, size):
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

        # function to check if the queue is full

    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True

        # function to check if the queue is empty

    def isEmpty(self):
        if self.front == -1:
            return True

    def enqueue(self, data):

        if CircularQueue.isFull(self):
            print("\nQueue is Full\n")

            # condition for empty queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:

            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if CircularQueue.isEmpty(self):
            print("\nQueue is Empty\n")

            # condition for only one element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):

        # condition for empty queue
        if self.front == -1:
            print("\nQueue is Empty")

        elif self.rear >= self.front:
            print("\nElements in queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")

        else:
            print("\nElements in Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        if (self.rear + 1) % self.size == self.front:
            print("\nQueue is Full")


if __name__ == '__main__':

    n = int(input('enter the size of Queue: '))

    ob = CircularQueue(n)
    while True:
        while not ob.isFull():
            ob.enqueue(int(input('push a number inside the queue: ')))
        ob.display()

        while not ob.isEmpty():
            p = input('\npop element(y/n): ')
            if p == 'y':
                ob.dequeue()
                ob.display()
            elif p == 'n':
                break
        if p == 'n':
            ob.display()
            break
