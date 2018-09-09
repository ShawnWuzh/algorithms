'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''
'''
对应于数据流，对应的算法就应该是在线算法。一道很经典的题目就是在一亿个数中找到最大的前100个数，这是一道堆应用题，我们先拿出100个数构建出
一个最小堆，每次来一个元素，我们都与堆顶元素进行比较，如果来的元素比堆顶元素大的话，就将堆顶元素替换为新来的元素。然后对堆进行调整。建堆的
复杂度为mlogm. 如果单纯地把所有元素都放到一个数组里，有两种情况: 第一种就是：插入的时候直接插入到数组里，插入的时间复杂度为O(1)，该数组
是无序的，然后在用其他算法在该无序数组去找中位数，找中位数的时间复杂度为O(N)。第二种就是：插入的时候先让数组有序，此时的时间复杂度取决于
排序算法的时间复杂度，排序的时间复杂度最好就是O(N)，然后是直接从有序数组中取中位数，这时候的时间复杂度为O(1)。其实这两种的时间复杂度都一样。
那我们有不有一种更好的方法，我们想到了平衡二叉搜索树非常适合这种情况，为什么？平衡二叉搜索树两边的高度差不超过1，而且是一颗搜索树，那么树的
顶部就是我们就是我们要找的中位数，这样插入的时间复杂度为O(logn)，取中位数的时间复杂度O(1)。但是问题是平衡二叉树的代码非常复杂，有不有一种
更简单的一种方法呢？我们可以借用一个Min Heap和一个Max Heap的。Min Heap用来保存大的那一半的数，max heap用来保存小的那一半的数。如果两个
heap的大小相同，中位数就是两个heap的堆顶的平均值，如果不相同，中位数是数量多的那一个的堆顶。
'''
class Solution:

    # version 1
    # def __init__(self):
    #     self.num = 0
    #     self.minHeap = []
    #
    # def Insert(self, num):
    #     self.minHeap.append(num)
    #     self.num += 1
    #
    # def GetMedian(self):
    #     for i in range(self.num // 2 - 1, -1,-1):
    #         self.minHeapify(i,self.num)
    #     # get the min
    #     if self.num % 2 == 0:
    #         loc = self.num // 2
    #         i = 1
    #         size = self.num
    #         while(i < loc):
    #             self.minHeap[0], self.minHeap[size-1] = self.minHeap[size-1], self.minHeap[0]
    #             size -= 1
    #             self.minHeapify(0,size)
    #             i += 1
    #         val1 = self.minHeap[0]
    #         if self.num == 1:
    #             val2 = self.minHeap[0]
    #         elif self.num == 2:
    #             val2 = self.minHeap[1]
    #         else:
    #             if self.minHeap[1] < self.minHeap[2]:
    #                 val2 = self.minHeap[1]
    #             else:
    #                 val2 = self.minHeap[2]
    #         return float(val1 + val2) / 2
    #     else:
    #         loc = self.num // 2 + 1
    #         i = 1
    #         size = self.num
    #         while(i < loc):
    #             self.minHeap[0], self.minHeap[size-1] = self.minHeap[size-1], self.minHeap[0]
    #             size -= 1
    #             self.minHeapify(0,size)
    #             i += 1
    #         return self.minHeap[0]
    # def minHeapify(self,index,size):
    #     left = 2 * index + 1
    #     right = 2 * index + 2
    #     min_index = index
    #     min_value = self.minHeap[min_index]
    #     if left < size and self.minHeap[left] < min_value :
    #         min_index = left
    #         min_value = self.minHeap[left]
    #     if right < size and self.minHeap[right] < min_value:
    #         min_index = right
    #         min_value = self.minHeap[right]
    #     if min_index != index:
    #         self.minHeap[index], self.minHeap[min_index] = self.minHeap[min_index],self.minHeap[index]
    #         self.minHeapify(min_index, size)
    # version 2
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.minSize = 0
        self.maxSize = 0

    def Insert(self, num):
        # insert 我们需要确定就是要insert进哪一个heap
        # 是min heap还是max heap。关键的一点就是我们必须要
        # 确保min heap里的所有数必须大于max heap里的所有数。
        # 而且我们还要确保一点，两个堆的的数量之差不能超过1，
        # 如果不确保这一点，中位数就一定不是堆顶的元素。
        if (self.minSize + self.maxSize) % 2 == 0:
            # 说明这两个堆各自的数量都是相等的。我们这里统一规定
            # 奇数个元素的时候，我们将新元素放到右边的最小堆里。
            # 现在问题来了，我们如何确保插入到右边最小堆的值是一定大于
            # 左边最大堆的每一个值呢？ 这就是tricky的地方，我们先把
            # 该元素与左边最大堆得堆顶元素比较，如果大于，这可以直接将
            # 该元素插入到右边的最小堆中，如果小于，则交换左边最大堆的
            # 堆顶元素与该元素，并把堆顶元素插入到右边的最小堆中的最后面，
            # 然后进行堆的调整，最后对左边的最大堆进行堆的调整。
            if self.maxSize == 0:
                self.insertToMinHeap(num)
            else:
                if num >= self.maxHeap[0]:
                    self.insertToMinHeap(num)
                else:
                    temp = self.maxHeap[0]
                    self.maxHeap[0] = num
                    self.insertToMinHeap(temp)
                    self.maxHeapify(0)
        else:
            # 此时说明左边的最大堆的数量是小于右边的最小堆的数量。为了确保
            # 两边的数量差不超过1，我们现在需要把新数据插入到左边的最大堆里面。
            # 现在同样的问题出现了， 我们怎么确保插入左边的最大堆里的元素是
            # 小于右边最小堆的所有元素？trick来了，我们先与右边最小堆的堆顶
            # 比较，如果小于，则直接将新元素插入到左边的最大堆，如果大于，则
            # 将右边最小堆的堆顶元素与新元素交换，并调整最小堆，将交换过的元素
            # 插入到左边的最大堆中。
            if num < self.minHeap[0]:
                self.insertToMaxHeap(num)
            else:
                temp = self.minHeap[0]
                self.minHeap[0] = num
                self.insertToMaxHeap(temp)
                self.minHeapify(0)
    def insertToMaxHeap(self, num):
        self.maxHeap.append(num)
        self.maxSize += 1
        for i in range(self.maxSize // 2 - 1, -1, -1):
            self.maxHeapify(i)
    def insertToMinHeap(self, num):
        self.minHeap.append(num)
        self.minSize += 1
        for i in range(self.minSize // 2 - 1, -1, -1):
            self.minHeapify(i)
    def minHeapify(self,i):
        left = 2 * i + 1
        right = 2 * i + 2
        min_index = i
        min_value = self.minHeap[i]
        if left < self.minSize and self.minHeap[left] < min_value:
            min_index = left
            min_value = self.minHeap[left]
        if right < self.minSize and self.minHeap[right] < min_value:
            min_index = right
            min_value = self.minHeap[right]
        if min_index != i:
            self.minHeap[i], self.minHeap[min_index] = self.minHeap[min_index], self.minHeap[i]
            self.minHeapify(min_index)
    def maxHeapify(self,i):
        left = 2 * i + 1
        right = 2 * i + 2
        max_index = i
        max_value = self.maxHeap[i]
        if left < self.maxSize and self.maxHeap[left] > max_value:
            max_index = left
            max_value = self.maxHeap[left]
        if right < self.maxSize and self.maxHeap[right] > max_value:
            max_index = right
            max_value = self.maxHeap[right]
        if max_index != i:
            self.maxHeap[i], self.maxHeap[max_index] = self.maxHeap[max_index],self.maxHeap[i]
            self.maxHeapify(max_index)
    def GetMedian(self):
        if (self.maxSize + self.minSize) % 2 == 0:
            return (self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return self.minHeap[0]

if __name__ == '__main__':
    s = Solution()
    data = [5,2,3,4,1,6,7,0,8]
    for d in data:
        s.Insert(d)
        print(s.GetMedian())
