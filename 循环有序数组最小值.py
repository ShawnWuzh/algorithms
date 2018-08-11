'''
对于一个有序循环数组arr，返回arr中的最小值。有序循环数组是指，有序数组左边任意长度的部分放到右边去，右边的部分拿到左边来。比如数组[1,2,3,3,4]，是有序循环数组，[4,1,2,3,3]也是。
给定数组arr及它的大小n，请返回最小值。
测试样例：
[4,1,2,3,3],5
返回：1
'''
'''
本题第一种思路就是采用暴力求解，依次比较，但是时间复杂度较高。有不有一种更高级的思路呢？首先要注意，整个数组是有序的，也可能是无序的，但是这种无序是局部有序的，因为这种无序是在有序的基础上进行变换得来的。本题的关键是要搞清楚有序循环数组的概念，循环有序数组是将一个有序数组切成两段，并交换位置得到引用块内容。性质：将一个循环有序数组一分为二，一定得到一个有序数组和另一个循环有序数组。长度不大于2的循环有序数组其实就是有序数组。
首先，当一个序列的最左值小于最右值的时候，显然这个序列是有序的。如果不满足，说明该序列含有循环数组，找到middle值，如果最左值大于middle值，说明最小值在最左值与middle值之间，如果middle值大于最右值，说明最小值在middle值和最大值之间，如果都不满足，那我们没有办法将该序列划分成两半，从而只能从left到right依次遍历。本题尤其注意循环的终止条件除了left<right外，还有当序列里只有两个值时，即是left = right-1时，此时不再需要划分，因为两个值我们只需要简单做一个大小比较即可找到最小值了。
'''
class MinValue:
    def getMin(self,arr,n):
        left = 0
        right = n - 1
        if n == 1:
            return arr[0]
        while(left < right):
            if left == right - 1:
                break
            if arr[left] < arr[right]:
                return arr[left]
            middle = (left + right) // 2
            if(arr[left] > arr[middle]):
                right = middle
            elif arr[middle] > arr[right]:
                left = middle
            else:
                min_value = arr[left]
                for i in range(left+1, right+1):
                    if arr[i] < min_value:
                        min_value = arr[i]
                return min_value
        return min(arr[left],arr[right])
