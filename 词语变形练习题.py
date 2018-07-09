'''
对于两个字符串A和B，如果A和B中出现的字符种类相同且每种字符出现的次数相同，则A和B互为变形词，请设计一个高效算法，检查两给定串是否互为变形词。

给定两个字符串A和B及他们的长度，请返回一个bool值，代表他们是否互为变形词。

测试样例：
"abc",3,"bca",3
返回：true
'''
'''
本题亮点在于先利用一个数组，数组的下标是每一个字符的ASCII值，当在str1上建立起这个数组之后，str2我们就不用再建立了，直接利用str1建立的这个，出现一个字符，将其对应的减1， 如果对应的值为0，就表示str1里面没有出现这个字符或者出现的次数小于了str2。非常巧妙的方法
'''
# written by HighW

class Transform:
    def chkTransform(self, A, lena, B, lenb):
        if lena != lenb:
            return False
        # this is an inefficient algorithm
        # a_dict = {}
        # b_dict = {}
        # for i in range(lena):
        #     if A[i] in a_dict:
        #         a_dict[A[i]] += 1
        #     else:
        #         a_dict[A[i]] = 1
        # for i in range(s):
        # for j in range(lenb):
        #     if B[j] in b_dict:
        #         b_dict[B[j]] += 1
        #     else:
        #         b_dict[B[j]] = 1
        # if len(a_dict) != len(b_dict):
        #     return False
        # flag = True
        # for char in a_dict:
        #     if char in b_dict:
        #         if a_dict[char] != b_dict[char]:
        #             flag = False
        #             break
        map = [0 for i in range(256)]
        for i in range(lena):
            map[ord(A[i])] += 1
        for j in range(lenb):
            if map[ord(B[j])] == 0:
                return False
            else:
                map[ord(B[j])] -= 1
        return True

        return flag
if __name__ == "__main__":
    chk = Transform()
    A = 'abc'
    B = 'bca'
    print(chk.chkTransform(A,3,B,3))
