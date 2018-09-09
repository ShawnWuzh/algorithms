'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
'''
Fibonacci sequence 0 1 1 2 3 5 8 13........
'''
class Solution:
    def Fibonacci(self,n):
        # 这种方式带来的后果就是，我们会重复计算很多项，最终带来的后果
        # 就是时间开销太大。
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # return self.Fibonacci(n-1) + self.Fibonacci(n-2)
        # 所以我们现在改写成循环的形式,对于每一个数，我们计算出来之后，我们需要
        # 把他给保存下来。
        table = []
        if n == 0:
            return 0
        if n == 1:
            return 1
        table.append(0)
        table.append(1)
        for i in range(2,n+1):
            table.append(table[i-1] + table[i-2])
        return table[n]

if __name__ == '__main__':
    s = Solution()
    print(s.Fibonacci(7))
