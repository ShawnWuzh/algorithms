'''
定义局部最小的概念。arr长度为1时，arr[0]是局部最小。arr的长度为N(N>1)时，如果arr[0]<arr[1]，那么arr[0]是局部最小；如果arr[N-1]<arr[N-2]，那么arr[N-1]是局部最小；如果0<i<N-1，既有arr[i]<arr[i-1]又有arr[i]<arr[i+1]，那么arr[i]是局部最小。 给定无序数组arr，已知arr中任意两个相邻的数都不相等，写一个函数，只需返回arr中任意一个局部最小出现的位置即可。
'''

'''
本题就是二分搜索的一个应用，本题尤其highlight了一个点，二分搜索不一定需要原始序列有序，只要我们能够通过二分搜索排除掉另一半，然后再利用剩下一半即可。
本题注意两个点，第一点：首尾检测过的点就不需要再检查了，所以后面的待检测序列只有1到size-2。第二点就是注意white循环的条件。
'''
class Solution:
    def getLessIndex(self,A):
        if len(A) == 0:
            return -1
        elif len(A) == 1:
            return 0
        else:
            if A[0] < A[1]:
                return 0
            elif A[-1] < A[-2]:
                return len(A) - 1
            else:
                left = 1
                right = len(A) - 2
                while left <= right:
                    middle = (left + right) // 2
                    if A[middle] < A[middle-1] and A[middle] < A[middle+1]:
                        return middle
                    elif A[middle] > A[middle-1]:
                        right = middle - 1
                    else:
                        left = middle + 1
                return -1

if __name__ == '__main__':
    s = Solution()
    A = [3,2,9,2,1,4,0,10,9,0,8,3,5,6,7,1,9,2,4,0,7]
    print(s.getLessIndex(A))
