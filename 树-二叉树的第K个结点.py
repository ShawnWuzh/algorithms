'''
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
'''
'''
本题就是考察二叉树的中序遍历，二叉树的中序遍历即是按照从小到大的顺序进行排序，然后我们就能
按照从小到大的顺序找到第K小的数。本题我们使用非递归的遍历。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthNode(self, pRoot, k):
        i = 0
        stack = []
        curNode = pRoot
        while(curNode):
            stack.append(curNode)
            curNode = curNode.left
        while(len(stack)):
            curNode = stack.pop()
            i += 1
            if(i == k):
                return curNode
            rightNode = curNode.right
            while(rightNode):
                stack.append(rightNode)
                rightNode = rightNode.left
if __name__ == '__main__':
    node = TreeNode(1)
    s = Solution()
    print(s.kthNode(node,1))
