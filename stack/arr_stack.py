# Implementing a stack using an array with Python 3
class ArrayStack:
    def __init__(self, limit=10):
        self.stack = [] # Create an empty array when the stack object is created
        self.limit = limit

    def __str__(self):
        return ', '.join([str(i) for i in self.stack])

    def __len__(self):
        return(len(self.stack)) # Return the length of the stack

    def is_empty(self):
        return(len(self.stack) == 0) # Return True if the stack is empty else False

    def push(self, item):
        if len(self.stack) >= self.limit:
            return "Stack Overflow"
        self.stack.append(item) # Add an item to the top of the stack

    def top(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1] # Return the top item of the stack (the last element in array)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

theStack = ArrayStack()

for i in range(10):
    theStack.push(i)

print(theStack)

print(theStack.top())
# theStack.pop()

# theStack.top()
# while not theStack.is_empty():
#     print(theStack.pop())

# theStack.is_empty()
# print(len(theStack))