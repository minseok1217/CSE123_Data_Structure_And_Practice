from math import sqrt, pi, pow

class Function:
    def getFactorial(self, n): # 재귀함수, n!구하기
        if n == 1:
            return 1
        else:
            return n * self.getFactorial(n - 1)

    def getTriples(self, bound): # bound 이하의 피타고라스 구하기
        print("triples within {} ".format(bound))
        for a in range(1, bound):
            for b in range(1, bound):
                for c in range(1, bound):
                    if (a * a + b * b == c * c):
                        print("{} {} {}".format(a, b, c))

    def drawTriangles(self, lines):
        for line in range(1, lines + 1):
            print(" " * (line - 1), end="")
            print("*" * (2 * lines + 1 - 2 * line))

        for line in range(lines, 0, -1):
            print(" " * (line - 1), end="")
            print("*" * (2 * lines + 1 - 2 * line))

class Complex:
    def __init__(self, x=0.0, y=0.0):
        self.re = x
        self.im = y

    def re(self):
        return self.re

    def im(self):
        return self.im

    def __str__(self):
        return '({}, {}i)'.format(self.re, self.im)

    def __repr__(self):
        return '(re={},im={}i)'.format(self.re, self.im)

    def __add__(self, other):
        x = self.re + other.re
        y = self.im + other.im
        return Complex(x, y)

    def __mul__(self, other):
        x = self.re * other.re - self.im * other.im
        y = self.re * other.im + self.im * other.re
        return Complex(x, y)

    def __abs__(self):
        return sqrt(self.re * self.re + self.im * self.im)

    def __eq__(self, other):
        self.re == other.re and self.im == other.im

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

class Point3D:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return 'Point3D(x={}, y={}, z={})'.format(self.x, self.y, self.z)

    def __repr__(self):
        return 'Point3D(x={}, y={}, z={})'.format(self.x, self.y, self.z)
        # repr은 str보다 공식적으로 사용되고 있으며 str이 정의되지 않았을 경우 repr에서 정의된 것을 사용해준다.
        # 또, 흔히 repr은 공식적이며 str은 비공식적이라고 말한다.

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def distance(self, p):
        d1 = (self.x - p.x) * (self.x - p.x)
        d2 = (self.y - p.y) * (self.y - p.y)
        d3 = (self.z - p.z) * (self.z - p.z)
        return sqrt(d1 + d2 + d3)

    def translate(self, a, b, c):
        self.x += a
        self.y += b
        self.z += c

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point3D(x, y, z)

    def __gt__(self, other):
        return self.length() > other.length()

    def __le__(self, other):
        return not self.__gt__(other)