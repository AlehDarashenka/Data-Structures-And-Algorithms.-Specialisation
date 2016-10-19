import Priority_Queue as pq

class Priority_Queue_mod(pq.priority_queue):

    def __init__(self, array):
        pq.priority_queue.__init__(self, array)

    def sift_down(self, i):
        maxindex = i
        self.left_child(i)

        if self.index < self.size and self.heap[self.index][1] < self.heap[maxindex][1]:
            maxindex = self.index
        elif self.heap[self.index][1] == self.heap[maxindex][1] and self.heap[self.index][0] < self.heap[maxindex][0]:
            maxindex = self.index

        self.right_child(i)

        if self.index < self.size and self.heap[self.index][1] < self.heap[maxindex][1]:
            maxindex = self.index
        elif self.heap[self.index][1] == self.heap[maxindex][1] and self.heap[self.index][0] < self.heap[maxindex][0]:
            maxindex = self.index

        if maxindex != i:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            #print i, maxindex
            self.sift_down(maxindex)

    def sift_up(self, ind):
        self.parent(ind)
        while ind > 0 and self.heap[self.index][1] > self.heap[ind][1]:
            self.heap[self.index], self.heap[ind] = self.heap[ind], self.heap[self.index]
            self.parent(ind)



def main():
    n, m = map(int, raw_input().split())
    input = [1 for _ in range(20)]
    queue = Priority_Queue_mod([(i, 0) for i in range(n)])
    print queue.heap

    for i in input:
        values = queue.extract_max()
        queue.insert((values[0], values[1]+i))
        print ' '.join(map(str, values))
    print queue.heap


if __name__ == '__main__':
    main()


'''
#array = [map(int, raw_input().split()) for _ in range(5)]
array = [[1,3],[2,2],[3,5],[0,1],[4,6]]
q = Priority_Queue_mod(array)
q.build_heap()
print q.heap
q.insert([2,1])
print q.heap
print q.extract_max()
print q.heap
'''


