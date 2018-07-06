'''
对于一个数组，请设计一个高效算法计算需要排序的最短子数组的长度。

给定一个int数组A和数组的大小n，请返回一个二元组，代表所求序列的长度。(原序列位置从0开始标号,若原序列有序，返回0)。保证A中元素均为正整数。

测试样例：
[1,4,6,5,9,10],6
返回：2
'''
# written by HighW
class Subsequence():
    def shortestSubsequence(self,A,n):
