'''
对于一个没有重复元素的整数数组，请用其中元素构造一棵MaxTree，MaxTree定义为一棵二叉树，其中的节点与数组元素一一对应，同时对于MaxTree的每棵子树，它的根的元素值为子树的最大值。现有一建树方法，对于数组中的每个元素，其在树中的父亲为数组中它左边比它大的第一个数和右边比它大的第一个数中更小的一个。若两边都不存在比它大的数，那么它就是树根。请设计O(n)的算法实现这个方法。
给定一个无重复元素的数组A和它的大小n，请返回一个数组，其中每个元素为原数组中对应位置元素在树中的父亲节点的编号，若为根则值为-1。
测试样例：
[3,1,4,2],4
返回：[2,0,-1,2]
'''
'''
本题其实活用了桟，因为每一个数，他左边比他大的第一个数一定是在桟的顶部。
'''

# written by HighW
class MaxTree:
    def buildMaxTree(self, A,n):
        stack1 = []
        stack2 = []
        result = []
        left = [None for i in range(n)]
        right = [None for j in range(n)]
        for i in range(len(A)):
            while(len(stack1) and A[i] > A[stack1[-1]]):
                stack1.pop()
            if(len(stack1) == 0):
                left[i] = -1
            else:
                left[i] = stack1[-1]
            stack1.append(i)
        for j in range(len(A)-1,-1,-1):
            while(len(stack2) and A[j] > A[stack2[-1]]):
                stack2.pop()
            if(len(stack2) == 0):
                right[j] = -1
            else:
                right[j] = stack2[-1]
            stack2.append(j)
        for i in range(len(left)):
            if left[i] == -1 and right[i] == -1:
                result.append(-1)
            elif left[i] == -1:
                result.append(right[i])
            elif right[i] == -1:
                result.append(left[i])
            elif A[left[i]] > A[right[i]]:
                result.append(right[i])
            else:
                result.append(left[i])
        return result
if __name__ == '__main__':
    A = [3,1,4,2]
    maxTree = MaxTree()
    print(maxTree.buildMaxTree(A,4))
