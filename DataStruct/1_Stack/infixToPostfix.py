import string


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixList = []

    tokenList = infixexpr.split()
    for token in tokenList:
        if token in string.ascii_uppercase:
            postfixList.append(token)
        elif token == '(':
            opstack.push(token)
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.is_empty()) and (prec[opstack.peek()] >= prec[token]):
                postfixList.append(opstack.pop())
            opstack.push(token)
    while not opstack.is_empty():
        postfixList.append(opstack.pop())
    return " ".join(postfixList)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, operand1, operand2):
    if op == '*':
        return operand1 * operand2
    elif op == '/':
        return operand1 / operand2
    elif op == '+':
        return operand1 + operand2
    elif op == '-':
        return operand1 - operand2


if __name__ == "__main__":
    print(infixToPostfix(" ( A + B ) * ( C + D ) * ( E + F ) "))
    print(infixToPostfix(" ( A + B ) * C"))
    print(infixToPostfix(" A + B * C "))
    print(postfixEval("7 8 + 3 2 + /"))
