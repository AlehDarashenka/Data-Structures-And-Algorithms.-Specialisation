class priority_queue:

    def __init__(self,  array):
        self.size = len(array)
        self.index = 0
        self.heap = array

    def left_child(self, i):
        self.index = (i+1)*2-1

    def right_child(self, i):
        self.index = (i+1)*2


    def sift_down(self, i):
        maxindex = i
        left = self.left_child(i)
        print left
        if left<self.size and self.heap[left]>self.heap[maxindex]:
            maxindex = left

        right = self.right_child(i)
        if right<self.size and self.heap[right]>self.heap[maxindex]:
            maxindex = right

        if maxindex != i:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex] ,self.heap[i]
            self.sift_down(maxindex)

    def build_heap(self, array):
        for i in range:
            print i
            self.sift_down(i)

q = priority_queue([5,4,3,2,1])
q.build_heap([5,4,3,2,1])
print q.heap





