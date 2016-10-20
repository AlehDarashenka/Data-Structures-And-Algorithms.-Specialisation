#Uses Python2
'''
The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the
way, did you know that algorithms based on Heaps are widely used for external sort, when you need
to sort huge files that don’t fit into memory of a computer?
Your task is to implement this first step and convert a given array of integers into a heap. You will
do that by applying a certain number of swaps to the array. Swap is an operation which exchanges
elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap
using only O(n) swaps, as was described in the lectures. Note that you will need to use a min-heap
instead of a max-heap in this problem.

'''

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


def main():

    n = int(raw_input())
    array = map(int, raw_input().split())
    q = priority_queue(array)
    q.build_heap()
    if array == q.heap:
        print 0


main()




