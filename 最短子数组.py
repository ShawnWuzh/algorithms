'''
对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
[1,2,10,1,8,9],6
返回：2
5
'''
'''
首先要弄清楚题目的意思，题目中需要我们找出一个数组里面未排序区的长度。然后我们需要知道什么是有序，什么是无序，
有序的意思就是在遍历中，后一个数需要比前一个数大。接下来是怎么确定无序区的起始位置和结束位置。我们从位置0开始进行遍历
如果后一个数比前一个数大，就表示截止当前位置，为有序区，此时我们需要把当前的的最小值更新为当前的这个数，如果后一个数比前一个数小，就表示无序区又增加一个了，
一直进行这样的操作，我们就找到了无序区的结束位置。那么我们找到无序区的起始位置呢，我们从后往前进行逆序遍历，其他操作类似于前面。从而求解出答案。
'''
# written by HighW
class Subsequence():
    def shortestSubsequence(self,A,n):
        min = A[0]
        min_loc = 0
        for i in range(0,n):
            if A[i] < min:
                min_loc = i
            else:
                min = A[i]
        max = A[n-1]
        max_loc = n - 1
        for j in range(n-1,-1,-1):
            if A[j] > max:
                max_loc = j
            else:
                max = A[j]
        if min_loc == 0 and max_loc == n-1:
            return 0
        else:
            return min_loc -max_loc + 1

if __name__ == '__main__':
    A = [1,4,6,5,9,10]
    sub = Subsequence()
    print(sub.shortestSubsequence(A,6))
