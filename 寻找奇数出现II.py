'''
给定一个整型数组arr，其中有两个数出现了奇数次，其他的数都出现了偶数次，找到这两个数。要求时间复杂度为O(N)，额外空间复杂度为O(1)。
给定一个整形数组arr及它的大小n，请返回一个数组，其中两个元素为两个出现了奇数次的元素,请将他们按从小到大排列。
测试样例：
[1,2,4,4,2,1,3,5],8
返回：[3,5]
'''
'''
本题思路，先用异或，我们找到了两个出现奇数次的元素的异或值result，显然该结果不为0， 接着我们找出
该结果中为1的那一位，记为K，接着重新用异或的方法，但是这次我们只对那些在K位上为1的数进行异或，
最后得到的结果显然就为其中的一个奇数次元素，记为b，然后我们用b与result进行异或，得到a。最后得到的
值就是我们的a和b.
'''
class OddAppearance:
    def findOdds(self, arr, n):
        result1 = 0
        for i in range(len(arr)):
            result1 = result1 ^ arr[i]

        for i in range(32):
            if(1<<i & result1 != 0):
                one_pos = i
                break
        result2 = 0
        for j in range(n):
            if (1<<one_pos & arr[j] != 0):
                result2 = result2 ^ arr[j]
        result3 = result1 ^ result2
        if result2 < result3:
            return [result2,result3]
        else:
            return [result3,result2]
