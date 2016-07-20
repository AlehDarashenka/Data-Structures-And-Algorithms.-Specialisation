import sys
import functools
import time



class TreeHeight:
    def __init__(self):
        self.n = None
        self.parent = None
        self.cache = None

    def test_read(self, n, values):
        self.n = n
        self.parent = values
        self.cache = [0]*n

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.cache = [0]*n


    def path(self, vertex):
        parent = self.parent[vertex]
        if parent == -1:
            return 1
        if self.cache[vertex]:
            return self.cache[vertex]

        self.cache[vertex] = 1 + self.path(self.parent[vertex])
        return self.cache[vertex]

    def height(self):
        return max([self.path(i) for i in range(self.n)])

def timed(func):
    @functools.wraps(func)
    def inner(*args):
        start = time.clock()
        func(*args)
        print (func.__name__, ':', time.clock()-start)
        return time.clock()-start
    return inner


@timed
def test():
    sys.setrecursionlimit(10 ** 7)  # max depth of recursion
    '''Test with bound values. Checking the maximum time execution'''
    n = 100000
    values = [i-1 for i in range(n)]
    tree = TreeHeight()
    tree.test_read(n, values)

    print 'depth:',tree.height()


def main():
    #listik = [4,-1,4,1,1]
    tree = TreeHeight()
    tree.read()
    print tree.height()


if __name__ == '__main__':

    test()
