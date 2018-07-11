'''
请设计一个高效算法，判断数组中是否有重复值。必须保证额外空间复杂度为O(1)。
给定一个int数组A及它的大小n，请返回它是否有重复值。
测试样例：
[1,2,3,4,5,5,6],7
返回：true
'''
# written by HighW
'''
思路就是先进行排序，然后从开始到结尾遍历这个数组。题目中需要保证额外空间复杂度为O(1)。冒泡排序的空间复杂的为O(1),
选择排序的空间复杂度为O(1),插入排序的空间复杂度为O(1)，快速排序的空间复杂度为O(1), 归并排序的空间复杂度为O(n)，堆排序的
空间复杂度为O(1)。从空间复杂度上，我们已经可以排除掉归并排序了，然后考虑到时间复杂度，我们选用heapsort，选用快速排序会超时
'''
class Checker:

    def checkDuplicate(self, a, n):
        # sorted = self.quickSort(A, n)
        if n <= 1:
            return False
        self.heapSort(a,n)
        print(a)
        for i in range(n-1):
            if a[i] == a[i+1]:
                return True
        return False

    def heapSort(self, A, n):
        self.buildHeap(A,n)
        while(n > 1):
            A[0],A[n-1] = A[n-1], A[0]
            n -= 1
            self.maxHeapify(A,n,0)
        return A


    def buildHeap(self, A, n):
        for i in range(n // 2 - 1,-1,-1):
            self.maxHeapify(A,n,i)

    def maxHeapify(self, A,n,i):
        left = 2 * i + 1
        right = 2 * i + 2
        max_loc = i
        if left < n and A[left] > A[max_loc]:
            max_loc = left
        if right < n and A[right] > A[max_loc]:
            max_loc = right
        if max_loc != i:
            A[i], A[max_loc] = A[max_loc], A[i]
            self.maxHeapify(A,n,max_loc)

    def quickSort(self, A, n):
        self.pivotSplit(A,0,n-1)
        return A
    def pivotSplit(self, A, start, end):
        if start > end:
            return
        pivot_loc = start
        for i in range(start+1,end+1):
            if A[i] < A[pivot_loc]:
                j = i-1
                temp = A[i]
                while(j >= pivot_loc):
                    A[j+1] = A[j]
                    j -= 1
                A[pivot_loc] = temp
                pivot_loc += 1
        self.pivotSplit(A,start,pivot_loc-1)
        self.pivotSplit(A,pivot_loc + 1, end)

if __name__ == '__main__':
    check = Checker()
    A = []
    print(check.checkDuplicate(A,0))
