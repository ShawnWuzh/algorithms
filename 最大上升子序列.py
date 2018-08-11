'''
这是一个经典的LIS(即最长上升子序列)问题，请设计一个尽量优的解法求出序列的最长上升子序列的长度。
给定一个序列A及它的长度n(长度小于等于500)，请返回LIS的长度。
测试样例：
[1,4,2,5,3],5
返回：3
'''
'''
首先要搞清楚最长上升子序列不一定是一个连续的的序列，该序列是在原来的序列中选出来的。如上面的例子中，
1 2 3也就是一个上升子序列。该动态规划的最简单的状态就是序列中只有一个元素，此时的最长上升子序列的
长度为1，那么后面的状态就可以由该状态推导出来。
'''
class LongestIncreasingSubsequence:
    def getLIS(self, A, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        maxSequence = 1
        dp = [0 for i in range(n)]
        dp[0] = 1
        for i in range(1,n):
            maxMin = -1
            for j in range(0,i):
                if A[j] < A[i]:
                    if dp[j] > maxMin:
                        maxMin = dp[j]
            if maxMin == -1:
                dp[i] = 1
            else:
                dp[i] = maxMin + 1
            if dp[i] > maxSequence:
                maxSequence = dp[i]
        return maxSequence

if __name__ == '__main__':
    lis = LongestIncreasingSubsequence()
    A = [1,4,2,5,3]
    print(lis.getLIS(A,5))
