'''
Group 1 - Struktur Data

> Stack with Linked List Implementation + Infix to Postfix and Prefix Conversion Program in Python 3

References:
https://gist.github.com/awadalaa/7ef7dc7e41edb501d44d1ba41cbf0dc6
https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/

Compiled and modified by Daffa Arviano (github.com/drdofx)
'''

# Implement a stack with linked list with Python 3
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

# Class converts infix expression to postfix and prefix expression
class InfixConverter:
    def __init__(self):
        self.stack = LinkedListStack()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]

    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops

    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()

    def isOpenParenthesis(self, ch):
        return ch == '('

    def isCloseParenthesis(self, ch):
        return ch == ')'

    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.stack = LinkedListStack()
        output = ''

        # print(self.stack)

        for c in expr:
            # print(c)
            
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.stack.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.stack.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.stack.pop()              
                else:
                    # print(c)
                    while not self.stack.is_empty() and self.hasLessOrEqualPriority(c,self.stack.top()):
                        output += self.stack.pop()
                    self.stack.push(c)

        while (not self.stack.is_empty()):
            output += self.stack.pop()
        return output
    
    '''
     1. Reverse expression string
     2. Replace open paren with close paren and vice versa
     3. Get Postfix and reverse it
    '''
    def toPrefix(self, expr):
        reverse_expr =''
        for c in expr[::-1]:
            if c == '(':
                reverse_expr += ")"
            elif c == ')':
                reverse_expr += "("
            else:
                reverse_expr += c

        reverse_postfix = self.toPostfix(reverse_expr)

        return reverse_postfix[::-1]


    def convert(self, expr):
        try:
            result = eval(expr)
        except:
            result = expr
        print("""
            Original expr is: {}
            Postfix is: {}
            Prefix is: {}
            Result is: {}
        """.format(expr, self.toPostfix(expr), self.toPrefix(expr), result))

infix = InfixConverter()

while True:
    infix_expr = input("Enter an infix expression: ")
    if infix_expr == '.':
        print("exit")
        break
    infix.convert(infix_expr)
# infix.convert("4 - 2 / 2")
# infix.convert("3+4")