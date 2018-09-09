'''
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
'''
本题就是斐波那契数列的变形，对于我们去填充一个大矩形，如果我们第一步选择竖向填充，则等于number - 1的种数，如果第一步
选择横向填充，显然，最终的结果等于number - 2的种数
'''
'''
总结: 递归的关键在于确定怎么一个大问题拆分成若干个小问题，本题的关键在于如何将大问题拆分成若干个小问题，本题的巧妙之处
就在于我们首先看第一步我们怎么弄，然后根据第一步的操作来确定递归的递推公式。
'''

class Solution:
    def rectCover(self, number):
        # if number == 0:
        #     return 0
        # if number == 1:
        #     return 1
        # if number == 2:
        #     return 2
        # return self.rectCover(number - 1) + self.rectCover(number - 2)
        # 非递归
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        table = [0 for i in range(number+1)]
        table[1] = 1
        table[2] = 2
        for i in range(3,number+1):
            table[i] = table[i-1] + table[i-2]
        return table[number]




if __name__ == '__main__':
    s = Solution()
    print(s.rectCover(4))
