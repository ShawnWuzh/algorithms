# written by HighW
# This is the source code for heap sort algorithm
class HeapSort():
    def heapSort(self, A, n):
        '''
        Every time, we swap the root with the last node, the last node is the current largest
        '''
        self.build_max_heap(A, n)
        while(n > 1):
            A[0], A[n-1] = A[n-1], A[0]
            n -= 1
            self.max_heapify(A,n,0)
        return A

    def max_heapify(self, A, size,i):
        '''
        max_heapify is done from top to bottom
        '''
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        max = i
        if left_child < size and A[max] < A[left_child]:
            max = left_child
        if right_child < size and A[max] < A[right_child]:
            max = right_child
        if max != i:
            A[i], A[max] = A[max], A[i]
            self.max_heapify(A,size,max)

    def build_max_heap(self, A, n):
        '''
        the heap is built fron bottom to top
        '''
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(A,n,i)
if __name__ == '__main__':
    sort = HeapSort()
    print(sort.heapSort([1,2,9,7,8,5,3,2],8))
