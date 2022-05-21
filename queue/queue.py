import os

def clear_terminal():
    os.system('clear')

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev=  prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.count += 1

    def dequeue(self):
        if self.count == 1:
            temp = self.head
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1

        print("Dequeued: " + str(temp.data))

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print(self.head.data)
        return self.head.data

    def is_empty(self):
        return self.count == 0

    def size(self):
        print("Number of element in queue: " + str(self.count))
        return self.count

    def print_queue(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None
        self.count = 0


if __name__ == "__main__":
    q = Queue()
    
    def print_menu():
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Size")
        print("5. Print")
        print("6. Clear")
        print("7. Exit Program")
    
    while True:
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data: "))
            q.enqueue(data)
        elif choice == 2:
            q.dequeue()
        elif choice == 3:
            q.peek()
        elif choice == 4:
            q.size()
        elif choice == 5:
            q.print_queue()
        elif choice == 6:
            q.clear()
        else:
            break
        input("\nEnter any key to continue...")
        clear_terminal()
    print("\nExit!")

