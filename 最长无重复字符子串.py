'''
对于一个字符串,请设计一个高效算法，找到字符串的最长无重复字符的子串长度。

给定一个字符串A及它的长度n，请返回它的最长无重复字符子串长度。保证A中字符全部为小写英文字符，且长度小于等于500。

测试样例：
"aabcb",5
返回：3

'''
# written by HighW
'''
本题还是相当tricky的， 思路就是我们要知道字符串的最长无重复子串的长度，如果我们能够利用前一个字符的最长无重复子串的信息，然后
我们利用一个数组保存每一个字符上一次出现的位置，如果该字符是首次出现，那么该字符以及他之前的最长无重复子串的长度为前一个字符的最长无重复子串的
长度+1， 如果该字符不是首次出现，这个时候就要比较该字符上次出现的位置l1和上一个字符最长无重复子串的起始位置l2之间的关系，如果l1在l2之前，那么
该字符的最长无重复子串最远只能达到l2,反之，只能达到l1.类似于这种下一个状态决定于上一个状态的，首先要定义好初始状态。
'''
class DistinctSubstring:
    def longestSubstring(self, A, n):
        map = [None for i in range(256)]
        length = [1 for j in range(n)]
        map[ord(A[0])] = 0
        for i in range(1,n):
            if map[ord(A[i])] == None:
                length[i] = length[i-1] + 1
            else:
                if map[ord(A[i])] < i - 1 - length[i-1] + 1:
                    length[i] = length[i-1] + 1
                else:
                    length[i] = i - map[ord(A[i])]
            map[ord(A[i])] = i
        max = -1
        for i in range(n):
            if length[i] > max:
                max = length[i]
        return max

if __name__ == "__main__":
    A = 'aabcb'
    substring = DistinctSubstring()
    print(substring.longestSubstring(A,5))
