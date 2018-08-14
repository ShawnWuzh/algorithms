'''
对于两个字符串A和B，我们需要进行插入、删除和修改操作将A串变为B串，定义c0，c1，c2分别为三种操作的代价，请设计一个高效算法，求出将A串变为B串所需要的最少代价。
给定两个字符串A和B，及它们的长度和三种操作代价，请返回将A串变为B串所需要的最小代价。保证两串长度均小于等于300，且三种代价值均小于等于100。
测试样例：
"abc",3,"adc",3,5,3,100
返回：8
'''
'''
本题的关键在于确定dp[i][j]的可能的来源，然后从可能的来源里面选择最小的那一个。
'''
class MinCost:
    def findMinCost(self,A,n,B,m,c0,c1,c2):
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        dp[0][0] = 0
        for i in range(1,m+1):
            dp[0][i] = c0 * i
        for j in range(1,n+1):
            dp[j][0] = c1 * j
        # now dp[i][j]
        for i in range(1,n+1):
            for j in range(1,m+1):
                temp = -1
                if A[i-1] == B[j-1]:
                    temp = dp[i-1][j-1]
                else:
                    temp = dp[i-1][j-1] + min(c0 + c1, c2)
                dp[i][j] = min(dp[i-1][j] + c1, dp[i][j-1] + c0, temp)
        return dp[n][m]

if __name__ == '__main__':
    A = "abc"
    n = 3
    B = "adc"
    m = 3
    c0,c1,c2 = 5,3,100
    mincost = MinCost()
    print(mincost.findMinCost(A,n,B,m,c0,c1,c2))
