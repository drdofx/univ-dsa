# Double linked list

class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev=  prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertAtStart(self, data):
        newNode = Node(data, None, None)
        newNode.next = self.head

        if self.head is not None:
            self.head.prev = newNode

        self.head = newNode
        return

    def insertAfter(self, prevNode, data):
        temp = self.head

        while(temp.next is not None):         # get last node
            if temp.data == prevNode:
                prevNode = temp
                break
            temp = temp.next

        if temp.next == None:
            return
        
        newNode = Node(data, None, None)

        newNode.next = prevNode.next

        prevNode.next = newNode

        newNode.prev = prevNode

        if newNode.next is not None:
            newNode.next.prev = newNode

        return

    def insertAtEnd(self, data):
        newNode = Node(data, None, None)
        temp = self.head
        if temp is None:
            return self.insertAtStart(data)

        while(temp.next is not None):         # get last node
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

        return

    def print_list(self):
        # if self.is_empty():
        #     print("Queue is empty")
        #     return

        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def clear(self):
        self.head = None
        self.tail = None


if __name__ == "__main__":
    dll = DoubleLinkedList()
    
    dll.insertAtEnd("A")
    dll.insertAtEnd("C")
    dll.insertAtEnd("D")
    dll.insertAtEnd("F")

    print("Insert pertama: ")
    dll.print_list()
    print("\n")

    dll.insertAfter("A", "B")
    dll.insertAfter("D", "E")

    print("Insert After yaitu menambahkan elemen B dan E: ")
    dll.print_list()

