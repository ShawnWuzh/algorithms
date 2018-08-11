'''
有一个矩阵map，它每个格子有一个权值。从左上角的格子开始每次只能向右或者向下走，最后到达右下角的位置，路径上所有的数字累加起来就是路径和，返回所有的路径中最小的路径和。
给定一个矩阵map及它的行数n和列数m，请返回最小路径和。保证行列数均小于等于100.
测试样例：
[[1,2,3],[1,1,1]],2,3
返回：4
'''

'''
先初始化一个DP矩阵，和map矩阵的一样的大小，然后是找到简单状态的结果，显然DP矩阵的第一行和第一列就是我们本题
的简单状态。why？因为第一行的所有状态只可能通过左边的路径向右达到， 而第一列的所有状态只能通过上边的路径
向下达到。可以看出动态规划的问题关键是确定简单状态的结果，然后通过状态转移方程由简单状态推导出后面状态的结果。
'''
class MinimumPath:
    def getMin(self,mmap,n,m):
        dp = [[-1 for i in range(m)] for j in range(n)]
        dp[0][0] = mmap[0][0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0] + mmap[i][0]
        for j in range(1,m):
            dp[0][j] = dp[0][j-1] + mmap[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if dp[i-1][j]< dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + mmap[i][j]
                else:
                    dp[i][j] = dp[i][j-1] + mmap[i][j]
        return dp[n-1][m-1]

if __name__ == '__main__':
    mini = MinimumPath()
    mmap = [[1,2,3],[1,1,1]]
    print(mini.getMin(mmap,2,3))
