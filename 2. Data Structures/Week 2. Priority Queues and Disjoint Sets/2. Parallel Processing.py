#Uses Python2
'''
You have a program which is parallelized and uses n independent threads to process the given list
of m jobs. Threads take jobs in the order they are given in the input. If there is a free thread,
it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t
interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list
simultaneously, the thread with smaller index takes the job. For each job you know exactly how long
will it take any thread to process this job, and this time is the same for all the threads. You need to
determine for each job which thread will process it and when will it start processing.
'''

import Priority_Queue as pq

class Priority_Queue_mod(pq.priority_queue):

    def __init__(self, array):
        pq.priority_queue.__init__(self, array)

    def sift_down(self, i):
        maxindex = i
        self.left_child(i)
        if self.index <self.size:
            if self.index < self.size and self.heap[self.index][1] < self.heap[maxindex][1]:
                maxindex = self.index
            elif self.heap[self.index][1] == self.heap[maxindex][1] and self.heap[self.index][0] < self.heap[maxindex][0]:
                maxindex = self.index

        self.right_child(i)

        if self.index <self.size:
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
    input = map(int, raw_input().split())
    queue = Priority_Queue_mod([(i, 0) for i in range(n)])

    for i in input:
        values = queue.extract_max()
        queue.insert((values[0], values[1]+i))
        print ' '.join(map(str, values))



if __name__ == '__main__':
    main()




