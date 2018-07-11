'''
对于一个字符串，请设计一个算法，将字符串的长度为len的前缀平移到字符串的最后。

给定一个字符串A和它的长度，同时给定len，请返回平移后的字符串。

测试样例：
"ABCDE",5,3
返回："DEABC"
'''
'''
类似于关于字符串逆序的题，通常都是利用字符串局部逆序和字符串全局逆序的结合的方法，具体怎么结合根据题目分析。
'''
class Translation:
    def stringTranslation(self, A, n, len):
        A = list(A)
        self.reverse(A, 0, len-1)
        self.reverse(A, len, n-1)
        self.reverse(A, 0 , n-1)
        return ''.join(A)
    def reverse(self, A, start, end):
        while(start < end):
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
if __name__ == '__main__':
    A = 'ABCDE'
    translation = Translation()
    print(translation.stringTranslation(A,5,3))
