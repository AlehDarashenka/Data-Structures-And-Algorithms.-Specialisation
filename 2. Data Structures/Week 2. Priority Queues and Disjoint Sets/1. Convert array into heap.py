#Uses Python2
class priority_queue:

    def __init__(self,  array):
        self.size = len(array)
        self.index = 0
        self.heap = [_ for _ in array]

    def left_child(self, i):
        self.index = i*2 + 1

    def right_child(self, i):
        self.index = i*2 + 2


    def sift_down(self, i):
        maxindex = i
        self.left_child(i)

        if self.index < self.size and self.heap[self.index] < self.heap[maxindex]:
            maxindex = self.index

        self.right_child(i)

        if self.index < self.size and self.heap[self.index] < self.heap[maxindex]:
            maxindex = self.index

        if maxindex != i:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            print i, maxindex
            self.sift_down(maxindex)

    def build_heap(self):
        for i in range(self.size/2, 0, -1):
            self.sift_down(i-1)


def main():

    n = int(raw_input())
    array = map(int, raw_input().split())
    q = priority_queue(array)
    q.build_heap()
    if array == q.heap:
        print 0


if __name__ == '__main__':
    main()




