'''
有一个有序数组arr，其中不含有重复元素，请找到满足arr[i]==i条件的最左的位置。如果所有位置上的数都不满足条件，返回-1。
给定有序数组arr及它的大小n，请返回所求值。
测试样例：
[-1,0,2,3],4
返回：2
'''
# written by HighW
'''
本题的思路就是先从中间找，如果发现中间这个数arr[middle] < middle, 那么middle前面的数肯定不可能满足条件arr[i] = i, 因为从
middle到middle前面的数，下降幅度肯定>=1,但是index下降幅度恒为1，因为arr[middle] < middle,所以middle之前的数，肯定也小于
它所在的index，因此此时从middle之后开始找。如果说arr[middle] = middle, 那么记录当前的位置，然后在middle之前继续找，如果
还能找到满足条件的，就更新当前位置。最后返回当前位置即为结果。
'''

class Find:
    def findPos(self, arr, n):
        start = 0
        end = n - 1
        result = -1
        while(start <= end):
            middle = (start + end) // 1
            if arr[middle] == middle:
                result = middle
                end = middle - 1
            elif arr[middle] < middle:
                start = middle + 1
            else:
                end = middle - 1
        return result


if __name__ == '__main__':
    arr = [-1,0,2,3]
    find = Find()
    print(find.findPos(arr,4))
