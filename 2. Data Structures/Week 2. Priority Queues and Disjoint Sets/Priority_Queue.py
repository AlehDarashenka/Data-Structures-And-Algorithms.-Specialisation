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

    def extract_max(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size -= 1
        self.sift_down(0)
        return result

    def build_heap(self):
        for i in range(self.size/2, 0, -1):
            self.sift_down(i-1)