from ll_stack import LinkedListStack

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
            result is: {}
        """.format(expr, self.toPostfix(expr), self.toPrefix(expr), result))

infix = InfixConverter()

while True:
    infix_expr = input("Enter an infix expression: ")
    if infix_expr == '.':
        break
    infix.convert(infix_expr)
# infix.convert("4 - 2 / 2")
# infix.convert("3+4")