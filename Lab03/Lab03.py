class StackApp:
    def evalPostfix(self, expr):
        s = Stack()
        for term in expr:
            if term in "+-*/":
                value1 = s.pop()
                value2 = s.pop()
                if term == "+":
                    s.push(value1 + value2)
                elif term == "-":
                    s.push(value1 - value2)
                elif term == "*":
                    s.push(value1 * value2)
                elif term == "/":
                    s.push(value1 / value2)
                else:
                    s.push(float(term))
        return s.pop()
    def converBase(self,num):
        s = Stack()
        while(num != 0):r = num % 2
        s.push(r)
        num = num//2
        print(num, "is Conversion into base 2")
        while (s.isEmpty() == False):
            print(s.pop(), end = "")
            # def checkBrackets(self, statement):
    def checkBrackets(self, expr):
        s = Stack()
        for ch in expr:
            if ch in ('(', '{', '['):
                s.push(ch)
            elif ch in (')', '}', ']'):
                if s.isEmpty():return False
                else:
                    cb = s.pop()
                if (ch == ')' and cb != '(') or (ch == '}' and cb != '{') or (ch == ']' and cb != '['):return False
        return s.isEmpty()
    def Evaluate_postfix_expressions(self, expr):
        s = Stack()
        for term in expr:
            if term in "+-*/":
                value1 = s.pop()
                value2 = s.pop()
                if term == "+":
                    s.push(value1 + value2)
                elif term == "-":s.push(value1 - value2)
                elif term == "*":s.push(value1 * value2)
                elif term == "/":s.push(value1 / value2)
                else:s.push(float(term)) return s.pop()
    def Infix2Postfix(self, expr):
        s= Stack()
        output = []
        for term in expr:
            if term in '(':s.push('(')
            elif term in ')':
                while not s.isEmpty():
                    op = s.pop()
                    if op =='(':breakoutput.append(op)
                    elif term in "+-*/":
                        while not s.isEmpty():op = s.peek()
                        if(self.precedence(term) <= self.precedence(op)):
                            output.append(op)
                            s.pop()
                        else:breaks.push(term)
                    else:
                        output.append(term)
                        while not s.isEmpty():output.append(s.pop())
        return output
    def precedence(self,op):
        if op == '(' or ')' : return 0
        elif op == '+' or '-' : return 1
        elif op == '*' or '/' : return 2
        else:return -1
class Stack:
    def __init__(self):self.top = []
    def __str__(self):
        # return str(self.top[::1])
        return str(self.top)

    def __len__(self):
        return len(self.top)
    def __contains__(self, item):
        return item in self.top
    def push(self, item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:print("Stack is Empty ...")
        exit()
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            ("Stack is Empty ...")
        exit()
    def size(self):
        return len(self.top)
    def display(self):return str(self.top[::1])
    def isEmpty(self):return len(self.top) == 0
    def clear(self):self.top = []