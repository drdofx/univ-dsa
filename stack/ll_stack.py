#implement a stack with linked list Python 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.is_empty():
            return "Stack Underflow"

        data = ""
        temp = self.head
        while(temp):
            data += f"{temp.data} -> "
            temp = temp.next
        return data
    # Method to check if stack is empty
    def is_empty(self):
        return self.head == None
    
    # Method to push an element to the stack
    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # Method to pop an element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        poppedNode = self.head
        self.head = poppedNode.next
        poppedNode.next = None
        return poppedNode.data
    
    # Method to return the top element of the stack
    def top(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.head.data

# theStack = LinkedListStack()

# data = [21, 3, 54, 12, 45, 78, 9, 0, -1]

# for i in data:
#     theStack.push(i)

# print(theStack)
# print(theStack.top())
# print(theStack.pop())
# print(theStack.top())
# print(theStack)