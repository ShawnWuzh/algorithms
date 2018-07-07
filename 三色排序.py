'''
有一个只由0，1，2三种元素构成的整数数组，请使用交换、原地排序而不是使用计数进行排序。

给定一个只含0，1，2的整数数组A及它的大小，请返回排序后的数组。保证数组大小小于等于500。

测试样例：
[0,1,1,0,2,2],6
返回：[0,0,1,1,2,2]
要求： 额外空间复杂度为O(1)
'''

'''
这道题的思想就是， 因为不能有额外的空间复杂度，所以类似于桶排序这种方法就不能使用了。因为我们只有三个数，不难
想到我们可以在最左边维持一个0的序列， 最右边维持一个2的序列，中间的显然就是1了。遍历过程中，我们采用交换的方式
来帮助我们把对应的元素交换到它应该属于的那一个集合里。简单来说，用两个变量分别保存当前最晚放进集合的0和2的位置，然后遍历
当需要交换时进行交换，记住千万不要本身与本身进行交换。
'''

# written by HighW
class ThreeColor():
    def sortThreeColor(self, A, n):
        last_zero = -1
        last_two = n
        i = 0
        while(i < last_two):
            if A[i] == 0:
                last_zero += 1
                if i != last_zero:
                    A[last_zero],A[i] = A[i], A[last_zero]
                else:
                    i += 1
            elif A[i] == 2:
                last_two -= 1
                A[last_two], A[i] = A[i], A[last_two]
            else:
                i += 1
        return A
if __name__ == '__main__':
    tc = ThreeColor()
    A = [0,1,1,0,2,2]
    print(tc.sortThreeColor(A,6))
