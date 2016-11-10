# python2
import random

class priority_queue:

    def __init__(self,  array=None):
        self.size = len(array)
        self.index = 0
        self.heap = [_ for _ in array]

    def left_child(self, i):
        self.index = i*2 + 1

    def right_child(self, i):
        self.index = i*2 + 2

    def parent(self, i):
        self.index = (i-1)/2

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

    def sift_up(self, ind):
        self.parent(ind)
        while ind > 0 and self.heap[self.index] > self.heap[ind]:
            self.heap[self.index], self.heap[ind] = self.heap[ind], self.heap[self.index]
            self.parent(ind)




    def insert(self, value):
        self.heap.append(value)
        self.size = len(self.heap)
        self.sift_up(self.size-1)


    def extract_max(self):
        result = self.heap[0]
        if len(self.heap)>1:
            self.heap[0] = self.heap.pop()
            self.size = len(self.heap)
            self.sift_down(0)
        else:
            self.heap = []
        return result

    def build_heap(self):
        for i in range(self.size/2, 0, -1):
            self.sift_down(i-1)


class Priority_Queue_mod(priority_queue):

    def __init__(self, n):
        priority_queue.__init__(self, [(i, 0) for i in range(n)])

    def sift_down(self, i):
        maxindex = i
        self.left_child(i)
        if self.index <self.size:
            if self.heap[self.index][1] < self.heap[maxindex][1]:
                maxindex = self.index
            elif self.heap[self.index][1] == self.heap[maxindex][1] and self.heap[self.index][0] < self.heap[maxindex][0]:
                maxindex = self.index

        self.right_child(i)

        if self.index <self.size:
            if self.heap[self.index][1] < self.heap[maxindex][1]:
                maxindex = self.index
            elif self.heap[self.index][1] == self.heap[maxindex][1] and self.heap[self.index][0] < self.heap[maxindex][0]:
                maxindex = self.index

        if maxindex != i:
            self.heap[i], self.heap[maxindex] = self.heap[maxindex], self.heap[i]
            #print i, maxindex
            self.sift_down(maxindex)

    def sift_up(self, ind):
        self.parent(ind)
        while ind > 0 and ((self.heap[self.index][1] > self.heap[ind][1]) or (self.heap[self.index][1] == self.heap[ind][1] and self.heap[self.index][0] > self.heap[ind][0])):
            self.heap[self.index], self.heap[ind] = self.heap[ind], self.heap[self.index]
            ind = self.index
            self.parent(ind)

    def write_response(self, input=[]):
        self.my_output = []
        my_input = input
        for i in my_input:
            values = self.extract_max()
            self.insert((values[0], values[1]+i))
            #print self.heap
            self.my_output.append(values)
            #print ' '.join(map(str, values))




# python3

class JobQueue:
    def read_data(self, n=None,m=None, array=[]):
        self.num_workers, m = n,m
        self.jobs = array
        #assert m == len(self.jobs)

    def write_response(self):
        self.default_answer = []

        for i in range(len(self.jobs)):
            self.default_answer.append((self.assigned_workers[i], self.start_times[i]))
            #print self.assigned_workers[i], self.start_times[i]

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = 0
          for j in range(self.num_workers):
            if next_free_time[j] < next_free_time[next_worker]:
              next_worker = j
          self.assigned_workers[i] = next_worker
          self.start_times[i] = next_free_time[next_worker]
          next_free_time[next_worker] += self.jobs[i]

    def solve(self, n=None, m=None , array=None):
        self.read_data(n,m,array)
        self.assign_jobs()
        self.write_response()




def main():
    n, m = map(int, raw_input().split())

    queue = Priority_Queue_mod(n)
    array =  map(int, raw_input().split())
    queue.write_response(array)
    #job_queue = JobQueue()
    #job_queue.solve()
    for i in queue.my_output:
        print i[0], i[1]

    #print job_queue.default_answer


def test():
    while True:
        n, m = random.randint(1,10), random.randint(1,10)
        array = [random.randint(1,100) for _ in range(m)]
        #n,m = 5,9
        #array = [36, 14, 20, 17, 26, 23, 10, 6, 22]
        queue = Priority_Queue_mod(n)
        queue.write_response(array)
        job_queue = JobQueue()
        job_queue.solve(n, m, array)
        if queue.my_output == job_queue.default_answer:
            print queue.my_output
        else:
            print n, m
            print array
            print queue.my_output
            print queue.heap
            print job_queue.default_answer
            break


if __name__ == '__main__':

    #test()
    main()




