'''
对于一个给定的字符串数组，请找到一种拼接顺序，使所有小字符串拼接成的大字符串是所有可能的拼接中字典序最小的。

给定一个字符串数组strs，同时给定它的大小，请返回拼接成的串。

测试样例：
["abc","de"],2
"abcde"
'''
'''
这道题其实就是一个字符串的排序问题， 可排序的关键就是我们怎么来排序， 是单独比较两个字符串的大小，这种比较是问题的，
比如str1是AC，str2是ACA， 如果单纯比较AC 和 ACA的话， str1应该放在前面，但是实际情况str1应该在后面，因为ACAAC < ACACA,
所以我们排序的依据不是单个字符串的字典序，而是str1str2和str2str1这两个的字典序，从而来确定str1和str2的顺序。我们这里实现一个
冒泡排序，只是这个冒泡排序的比较和我们常规的比较不一样了。
'''
class Prior:
    def findSmallest(self, strs, n):
        for i in range(n-1, -1, -1):
            flag = False
            for j in range(0,i):
                if strs[j] + strs[j+1] > strs[j+1] + strs[j]:
                    strs[j],strs[j+1] = strs[j+1],strs[j]
                    flag = True
            if not flag:
                break
        return ''.join(strs)
if __name__ == '__main__':
    strs = ["abc","de"]
    prior = Prior()
    print(prior.findSmallest(strs,2))
