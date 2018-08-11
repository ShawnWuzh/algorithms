'''
如果更快的求一个整数k的n次方。如果两个整数相乘并得到结果的时间复杂度为O(1)，得到整数k的N次方的过程请实现时间复杂度为O(logN)的方法。
给定k和n，请返回k的n次方，为了防止溢出，请返回结果Mod 1000000007的值。
测试样例：
2,3
返回：8
'''
'''
这道题的思路是这样的，比如我要计算K的n次方，那么首先我先用二进制把n写成二进制的形式，比如K=6，n=12，那么二进制形式就为：1100，依次计算
6^1, 6^2 = 6^1 * 6^1, 6^4=6^2 * 6^2,....其实幂就是对应的二进制的位数，然后我们的目的是把6^12分解成6^(8+4) = 6^8 * 6^4，也就是二进制
形式里面为1的位数的乘积。相当于二进制天然的就把原始的12次幂划分成了另外两个数的成绩，然后另外两个数分别又是另外4个数的乘积。本题要记住这种
巧妙的方法，就是利用了二进制这种天然划分的功能。
'''
# written by HighW

class QuickPower:
    def getPower(self, k, N):
        # 将N转换成二进制形式
        binaryCode = bin(N)[2:]
        digit = 0
        index = -1
        result = 1
        while(digit < len(binaryCode)):
            if digit == 0:
                temp = k
            else:
                temp = temp * temp
            temp = temp % 1000000007
            if binaryCode[index] == '1':
                result *= temp
                result %= 1000000007
            digit += 1
            index -= 1
        return result

if __name__ == "__main__":
    quick = QuickPower()
    k = 2
    N = 100
    print(quick.getPower(k,N))
