'''
对于一个有序数组arr，再给定一个整数num，请在arr中找到num这个数出现的最左边的位置。
给定一个数组arr及它的大小n，同时给定num。请返回所求位置。若该元素在数组中未出现，请返回-1。
测试样例：
[1,2,3,3,4],5,3
返回：2
'''
'''
本题应该就是一个原汁原味的二分查找，在有序序列里查找元素。思路就是二分查找到元素之后，我们还需要确定，该元素之前还有不有该元素，如果有的话
我们需要更新该元素的位置，因为我们想要找到该元素出现的哦最左位置。
'''
class LeftMostAppearance:
    def findPos(self,arr,n,num):
        res = -1
        left = 0
        right = n - 1
        while(left <= right):
            middle = (left + right) / 2
            if arr[middle] == num:
                res = middle
                right = middle - 1
            elif arr[middle] < num:
                left = middle + 1

            else:
                right = middle - 1
        return res
