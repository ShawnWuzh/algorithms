'''
对于一个字符串，请设计一个算法，只在字符串的单词间做逆序调整，也就是说，字符串由一些由空格分隔的部分组成，你需要将这些部分逆序。

给定一个原字符串A和他的长度，请返回逆序后的字符串。

测试样例：
"dog loves pig",13
返回："pig loves dog"
要求空间复杂度为O(1)
'''
'''
类似于这种逆序的问题， 一定要巧用整体逆序和部分逆序的方法，结合起来进行求解。但是要注意一点Python里的字符串是不可更改的哦
'''
class Reverse:
    def reverseSentence(self, A, n):
        A = list(A)
        self.localReverse(A,0,n-1)
        # 下面这种代码其实就是在硬编码，我们需要避免这种情况的发生。首先要思路清晰的想清楚算法，然后再去写代码。不要硬去凑代码。
        i = 0
        start = 0
        while(i < n):
            if A[i] == ' ':
                end = i-1
                self.localReverse(A,start,end)
                start = end + 2
            i += 1
        self.localReverse(A,start,i-1)
        return ''.join(A)
    def localReverse(self, A, start, end):
        while(start < end):
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1

if __name__ == '__main__':
    A = "dog loves pig"
    reverse = Reverse()
    print(reverse.reverseSentence(A,13))
