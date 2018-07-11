'''
如果对于一个字符串A，将A的前面任意一部分挪到后边去形成的字符串称为A的旋转词。比如A="12345",A的旋转词有"12345","23451","34512","45123"和"51234"。对于两个字符串A和B，请判断A和B是否互为旋转词。

给定两个字符串A和B及他们的长度lena，lenb，请返回一个bool值，代表他们是否互为旋转词。

测试样例：
"cdab",4,"abcd",4
返回：true
'''


'''
本题的思路就是将两个A合为一个大字符串，然后利用KMP算法在这个大字符串里寻找字符串B。这道题的解法非常
tricky， 因为如果两个字符串互为旋转词，那么一定另一个字符串是另一个字符串的大字符串的一个子串。
'''
# written by HighW
import string
class Rotation:
    def chkRotation(self, A, lena, B, lenb):
        if lena != lenb:
            return False
        big_string = A + A
        if big_string.find(B) != -1:
            return True
        else:
            return False
