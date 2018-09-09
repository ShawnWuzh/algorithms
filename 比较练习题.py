'''
对于两个32位整数a和b，请设计一个算法返回a和b中较大的。但是不能用任何比较判断。若两数相同，返回任意一个。

给定两个整数a和b，请返回较大的数。

测试样例：
1,2
返回：2
'''
'''
我们首先用a - b 得到一个差值，但是由于不能用任何的比较判断，但是我们怎么来判断差值的正负呢，
我们可以通过提取出符号位，然后利用符号位，符号位*a + 符号位的反 * b就是我们的结果。
'''
class Compare:
    def getMax(self, a, b):
        c = a - b
        sign = (c >> 31) & 1
        flip_sign = sign ^ 1
        return sign * b + flip_sign * a
        # 上面这个方法有个问题，就是有可能会造成溢出，如果a是正数， b是负数，a-b就有可能溢出
        # 因此我们最好判断一下 a和b的符号。
        signA = a >> 31 & 1
        signB = b >> 31 & 1
        c = a - b
        signC = c >> 31 & 1
        diffAB = signA ^ signB
        sameAB = diffAB ^ 1
        returnA = diffAB * signA + signC * sameAB   # 符号相同，则取决于差值的符号，符号不同，则取决于A的符号
        returnB = returnA ^ 1    # 异或就是相同为0，不相同为1
        return a * returnB + b * returnA   
