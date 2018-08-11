'''
一个背包有一定的承重cap，有N件物品，每件都有自己的价值，记录在数组v中，也都有自己的重量，记录在数组w中，每件物品只能选择要装入背包还是不装入背包，要求在不超过背包承重的前提下，选出物品的总价值最大。给定物品的重量w价值v及物品数n和承重cap。请返回最大总价值。
测试样例：
[1,2,3],[1,2,3],3,6
返回：6
'''
class Backpack:
    # 递归写法
    def maxValue(self,w,v,n,cap):
        # return self.findMax(w,v,0,cap)
        return self.dpmaxValue(w,v,n,cap)
    def findMax(self,w,v,start,remain):
        if start >= len(w):
            return 0
        if remain <= 0:
            return 0
        return max(self.findMax(w,v,start+1,remain), v[start] + self.findMax(w,v,start+1, remain-w[start]))

    # 动态规划写法。
    def dpmaxValue(self,w,v,n,cap):
        dp = [[0 for i in range(cap+1)] for j in range(n)]
        for i in range(1,cap+1):
            if w[0] <= i:
                dp[0][i] = v[0]
        for i in range(1,n):
            for j in range(1,cap+1):
                if w[i] <= j:
                    dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]] + v[i])
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n-1][cap]


if __name__ == '__main__':
    w = [1,2,3]
    v = [1,2,3]
    b = Backpack()
    print(b.maxValue(w,v,3,6))
