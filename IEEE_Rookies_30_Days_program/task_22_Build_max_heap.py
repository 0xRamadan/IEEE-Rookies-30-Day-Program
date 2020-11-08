# IEEE_Rookies_task_22
# name: Mahmoud_Ramadan
# task: Build Max Heap

class MaxHeap:
    def __init__(self, elements=[]):
        self.heap = [0]
        for i in elements:
            self.heap.append(i)
            self.floatUp(len(self.heap) -1)

    def push(self, data):
        self.heap.append(data)
        self.floatUp(len(self.heap) - 1)

    def peek(self):
        if self.heap[1]:
            return self.heap
        else:
            return False

    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max_elem = self.heap.pop()
            self.bubble_down(1)

        elif len(self.heap) == 2:
            max_elem = self.heap.pop()
        else:
            max_elem = False
        return max_elem

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def floatUp(self, index):
        parent = index // 2
        if index <=1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.floatUp(parent)

    def bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.swap(index, largest)
            self.bubble_down(largest)


if __name__ == '__main__':

    l = list(map(int, input().split()))
    print(MaxHeap(l))


