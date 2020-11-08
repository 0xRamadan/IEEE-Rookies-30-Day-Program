# IEEE_Rookies_task_16_part_02
# name: Mahmoud_Ramadan
# task: operation on linked list


# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


# linked list class
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

        # Counts the no. of occurrences of a node

    def count(self, search_for):
        current = self.head
        count = 0
        while current is not None:
            if current.data == search_for:
                count += 1
            current = current.next
        return count

        # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # Function to insert a new node at a given position

    def insert(self, data, position):
        new = Node(data)
        if position == 0:
            new.next = self.head
            self.head = new
            return self.head
        pointer = self.head
        counter = 1
        while pointer.next is not None:
            if counter == position:
                new.next = pointer.next
                pointer.next = new
                break
            counter += 1
            pointer = pointer.next

        # Function to delete a node

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        if temp is None:
            return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        prev.next = temp.next
        temp = None

        # Utility function to print the linked LinkedList

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    print('''>>Note that linked list here contain some random nummbers.
you can use this as input:
-------------------------
position: 3
data: 6
count of n where n = 1 (e.g)
-------------------------''')
    pos = int(input('enter the position you want to insert a number in: '))
    data = int(input("insert a number: "))

    # creating an object of LinkedList class
    llist = LinkedList()

    # insert some random nodes at the beginning of the linked list
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)

    # insertion at a given position

    llist.insert(data, pos)

    # printing nodes of the linkedlist
    llist.printList()

    # printing count of occurrences of a specific number
    count = int(input('enter a number you want to count the number of Occurrences for: '))
    print("count of {0} is {1}".format(count, llist.count(count)))

    # ask the user to choose a number to delete
    k = int(input('enter a number you want to delete: '))
    llist.deleteNode(k)
    llist.printList()

    input('press enter to exit...')
