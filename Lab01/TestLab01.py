from Point3D import Function, Complex, Point3D
def useFunction():
    f1 = Function()
    # n=5
    # print("Factorial of {} is {} ".format(n,f1.getFactorial(n)))
    # f1.getTriples(50)
    f1.drawTriangles(7)


def useComplex():
    z1 = Complex(1.5, 5.6)
    z2 = Complex(4.0, 3.7)
    print('1')
    print(z1)
    print(z2)
    z3 = z1 + z2
    print('{} = {} + {}'.format(z3, z1, z2))


def usePoint3D():
    p1 = Point3D()
    p2 = Point3D(3.6, 2.3, 1.2)
    print(p1)
    print(p2)
    p1.setCord(4.6, 6.7, 9.0)
    p3 = p1 + p2
    print("p3 : ", p3)
    print(p1)
    print('{:.2f}'.format(p2.length()))
    print(p1.distance(p2))


def main():
    # usePoint3D()
    # useComplex()
    useFunction()


if __name__ == "__main__":
    main()