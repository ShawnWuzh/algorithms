'''
已知一个几乎有序的数组，几乎有序是指，如果把数组排好顺序的话，每个元素移动的距离可以不超过k，并且k相对于数组来说比较小。请选择一个合适的排序算法针对这个数据进行排序。
给定一个int数组A，同时给定A的大小n和题意中的k，请返回排序后的数组。
测试样例：
[2,1,4,3,6,5,8,7,10,9],10,2
返回：[1,2,3,4,5,6,7,8,9,10]
'''
# written by HighW
# 首先看到这道题目， 冒泡，选择排序是不用考虑的了， 因为这两类排序和原始数据是否有序没有关系，都是n^2的时间复杂度。
# 剩下的就是快速排序，归并排序，插入排序和堆排序了，其中归并排序与原始的数据是否有序也没有关系，雷打不动N*LogN，
# 快速排序也是还是要把所有的数分割在pivot的两边，堆排序的原理貌似与原始数据是否有序也没有关系，先等一下，因为待会会有其他的东西出现
# 那么现在剩下的就只有插入排序了。因为每个元素的距离可以不超过K，而插入排序的时间复杂度，主要就是因为元素的移动带来的,时间复杂度为O(N*K)，
# 现在我们再次回到堆排序，我们刚刚说堆排序与原始数据是否有序没有关系是在堆的高度一定下说的，但是本题已经说了，每个元素移动的距离可以不超过
# K，意味着，最小的元素一定在0到k-1之间，因为最小的元素移动到第一位不能超过K位，这就意味着，我们最小堆的高度可以变成logK了，这样整个时间
# 复杂度就可以变成O(N*LogK)了。

'''
这道题的亮点在于，我们不再建立一个和原始数据大小一样的heap， 而是建立一个更小的，size为K的heap了。
'''

class ScaleSort:
    def scaleSort(self, A, n, k):
        minHeap = self.buildMinHeap(A,k)
        i = k
        j = 0
        while(i<n):
            A[j] = minHeap[0]
            minHeap[0] = A[i]
            self.minHeapify(minHeap,0,k)
            i += 1
            j += 1
        while(k):
            A[j] = minHeap[0]
            minHeap[0] = minHeap[k-1]
            k -= 1
            j += 1
            self.minHeapify(minHeap,0,k)
        return A

    def minHeapify(self,A,i,k):
        min_loc = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < k and A[left] < A[min_loc]:
            min_loc = left
        if right < k and A[right] < A[min_loc]:
            min_loc = right
        if min_loc != i:
            A[i],A[min_loc] = A[min_loc],A[i]
            self.minHeapify(A,min_loc,k)

    def buildMinHeap(self,A,size):
        minHeap = []
        for i in range(size):
            minHeap.append(A[i])
        for i in range(size // 2 - 1,-1,-1):
            self.minHeapify(minHeap,i,size)
        return minHeap

if __name__ == '__main__':
    sort = ScaleSort()
    A = [2,1,4,3,6,5,8,7,10,9]
    print(sort.scaleSort(A,10,2))
