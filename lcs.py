'''
给定两个字符串A和B，返回两个字符串的最长公共子序列的长度。例如，A="1A2C3D4B56”，B="B1D23CA45B6A”，”123456"或者"12C4B6"都是最长公共子序列。
给定两个字符串A和B，同时给定两个串的长度n和m，请返回最长公共子序列的长度。保证两串长度均小于等于300。
测试样例：
"1A2C3D4B56",10,"B1D23CA45B6A",12
返回：6
'''
'''
本题又是一道典型的动态规划问题，我们依然还是要找出动态规划的简单状态,我们一直在说的简单状态就是指我们可以通过
简单的if语句判断就能得到的结果。最简单的状态就是其中一个字符串里面只有一个元素，那么我们可以直接在另外一个字符串
里面找到和该元素相等的那个元素，那么该元素之后的元素在dp矩阵均为1.接下来只需要考虑dp[i][j]的可能的来源的值即可。
'''
class LCS:
    def findLCS(self, A, n, B, m):
        if n == 0 or m == 0:
            return 0
        dp = [[0 for i in range(m)] for j in range(n)]
        for i in range(n):
            if A[i] == B[0]:
                while i < n:
                    dp[i][0] = 1
                    i +=1
                break
        for j in range(m):
            if B[j] == A[0]:
                while j < m:
                    dp[0][j] = 1
                    j += 1
                break
        for i in range(1,n):
            for j in range(1, m):
                temp = -1
                if A[i] == B[j]:
                    temp = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i-1][j],dp[i][j-1],temp)    # 这里是本题的关键
        return dp[n-1][m-1]
if __name__ == '__main__':
    A = "1A2C3D4B56"
    B = "B1D23CA45B6A"
    lcs = LCS()
    print(lcs.findLCS(A,10,B,12))
