'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        table = [0 for i in range(number+1)]
        table[1] = 1
        table[2] = 2
        for i in range(3, number + 1):
            for j in range(number-1,0,-1):
                table[i] += table[j]
            table[i] += 1
        return table[number]


    
