from BinaryTree import *
from queue import LifoQueue


class ExpressionTree(BinaryTree):

    def __init__(self, root=None):
        super().__init__(root=root)

    def isOperator(self, c):
        if (c == '+' or c == '-' or c == '*'
                or c == '/' or c == '^'):
            return True
        else:
            return

    def constructTree(self, postfix):
        stack = LifoQueue()

        for char in postfix:

            if not self.isOperator(char):
                t = Node(char)
                stack.put(t)

            else:
                t = Node(char)
                t1 = stack.get()
                t2 = stack.get()

                t.setRight(t1)
                t.setLeft(t2)

                stack.put(t)

        et = stack.get()

        return et

    def evaluateExpressionTree(self, node):
        if node is None:
            return 0

        if not self.isOperator(node.data):
            return int(node.data)

        l = self.evaluateExpressionTree(node.left)
        r = self.evaluateExpressionTree(node.right)

        if node.data == '+':
            return l + r
        elif node.data == '-':
            return l - r
        elif node.data == '*':
            return l * r
        elif node.data == '/':
            if r == 0:
                print("Division by zero")
                return
            return l / r
        elif node.data == '^':
            return l ** r