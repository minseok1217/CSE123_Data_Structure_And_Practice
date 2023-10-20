from Lab03 import Stack, StackApp
def useStackApp():
    sa = StackApp()
    sa.converBase(126)
    sa.converBase(1026)
    expr = 'dsdkl(jaskfjl{pp[sdkjflsdf}'
    print("Brackets are Balaneced? ", sa.checkBrackets(expr))
    expr1 = '2+(4+3*2+1)/3'
    print(sa.Infix2Postfix(expr1))
    expr2 = "2432*+1+3/+"
    print("Postfix Evaluation = {:.2f}".format(sa.evalPostfix(expr2)))
def useStack():
    odd = Stack()
    even = Stack()
    print("Even Stack", even)
    print("odd Stack", odd)
    for i in range(20):
        if i % 2 == 0:  #짝수면even에 삽입 홀수이면odd에 삽입
        even.push(i)
    else:
        odd.push(i)
        print("Even Stack",even)
        print("odd Stack",odd)
        print(even.peek())
        print(odd.peek())
        print(even.pop())
        print(odd.pop())
        print("Even Stack", even)
        print("odd Stack", odd)
        print(odd.size())
        print(len(odd))
        lst = [3, 4, 5, 6]
        for i in lst:
            print(i)
def main():
    useStack()
    useStackApp()


if __name__ == "__main__":main()