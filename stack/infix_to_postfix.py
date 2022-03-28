from arr_stack import ArrayStack

def isOperand(char):
    return char.isalpha()

def precedence(char):
    if char == '+' or char == '-':
        return 1
    elif char == '*' or char  == '/':
        return 2
    elif char == '^':
        return 3
    else:
        return -1

def notGreater(stack, i):
        try:
            a = precedence(i)
            b = precedence(stack.top())
            return True if a <= b else False
        except KeyError:
            return False

def infixToPostfix(exp, stack):
    postfix = []
    # Iterate over the expression for conversion
    for i in exp:
        # If the character is an operand,
        # add it to output
        if isOperand(i):
           postfix.append(i)

        # If the character is an '(', push it to stack
        elif i == '(':
            stack.push(i)

        # If the scanned character is an ')', pop and
        # output from the stack until and '(' is found
        elif i  == ')':
            while((not stack.is_empty()) and
                    stack.top() != '('):
                a = stack.pop()
                postfix.append(a)
            if (not stack.is_empty() and stack.top() != '('):
                return -1
            else:
                stack.pop()

        # An operator is encountered
        else:
            while(not stack.is_empty() and notGreater(stack, i)):
                    # this is to pass cases like a^b^c
                # without if ab^c^
                # with if abc^^
                if i == "^" and stack.array[-1] == i:
                    break
                postfix.append(stack.pop())
            stack.push(i)

    # pop all the operator from the stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    return " ".join(postfix)

myExp = "(4+5)*(6-3)"
print('Infix:',' '.join(myExp))
theStack = ArrayStack()
print('Postfix:',infixToPostfix(myExp, theStack))

