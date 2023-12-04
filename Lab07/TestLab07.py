from Node import *

def DFS():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    a.setRight(c); a.setDown(b)
    b.setUp(a); b.setRight(d)
    c.setLeft(a); c.setDown(d); c.setRight(e)
    d.setLeft(b); d.setUp(c); d.setRight(f)
    e.setRight(g); e.setDown(h)
    f.setLeft(d)
    g.setLeft(e); g.setRight(h)
    h.setUp(e); h.setLeft(g)


if __name__ == "__main__":
    pass