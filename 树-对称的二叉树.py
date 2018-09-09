'''
请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
'''
这道题的思路很显然，我们需要采取左中右的中序遍历，以及右中左的中序遍历，然后看这两种的的先序遍历是否一致，如果
一致，说明是对称的，如果不一致，说明不一致。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetrical(self, pRoot):
        curNode1 = pRoot
        curNode2 = pRoot
        stack1 = []
        stack2 = []
        while(curNode1):
            stack1.append(curNode1)
            curNode1 = curNode1.left
        while(curNode2):
            stack2.append(curNode2)
            curNode2 = curNode2.right
        if(len(stack1) != len(stack2)):
            return False
        while(len(stack1) and len(stack2)):
            curNode1 = stack1.pop()
            curNode2 = stack2.pop()
            if curNode1.val != curNode2.val:
                return False
            rightNode = curNode1.right
            while(rightNode):
                stack1.append(rightNode)
                rightNode = rightNode.left
            leftNode = curNode2.left
            while(leftNode):
                stack2.append(leftNode)
                leftNode = leftNode.right
        if len(stack1) or len(stack2):
            return False
        return True

if __name__ == '__main__':
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node1.left = node2
    node3 = TreeNode(4)
    node1.right = node3
    s = Solution()
    print(s.isSymmetrical(node1))
