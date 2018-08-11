'''
有n级台阶，一个人每次上一级或者两级，问有多少种走完n级台阶的方法。为了防止溢出，请将结果Mod 1000000007
给定一个正整数int n，请返回一个数，代表上楼的方式数。保证n小于等于100000。
测试样例：
1
返回：1
'''
'''
本题是一道典型的动态规划问题，只有一级台阶的时候，只有一种走法，当有两级台阶的时候，有两种走法到达当前
的位置。 到达的第i级台阶的时候，f(i) = f(i-1) + f(i-2)，这个就是动态规划的状态方程。动态规划的题都是
这样，先去找出最简单的状态的答案，然后后面的状态可以由前面的状态来推出来。   
'''

class GoUpstairs:
    def countWays(self,n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            table = [0 for i in range(n+1)]
            table[0] = 1
            table[1] = 1
            table[2] = 2
            for i in range(3, n+1):
                table[i] = table[i-1] + table[i-2]
            return table[n]

if __name__ == '__main__':
    go = GoUpstairs()
    print(go.countWays(1))
