'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
'''
class Solution:
    def jumpFloor(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        table = []
        table.append(1)
        table.append(2)
        for i in range(2, number):
            table.append(table[i-1] + table[i-2])
        return table[number-1]

if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(5))
