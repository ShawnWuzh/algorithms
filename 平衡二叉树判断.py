'''
有一棵二叉树，请设计一个算法判断这棵二叉树是否为平衡二叉树。

给定二叉树的根结点root，请返回一个bool值，代表这棵树是否为平衡二叉树。
'''
'''
二叉树的很多题目都是用二叉树的遍历的代码进行了改写。平衡二叉树就是左子树和右子树的高度差小于等于1。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CheckBalance:
    def check(self, root):
        if self.checkb(root) == -1:
            return False
        else:
            return True

    def checkb(self, head):
        if not head:
            return 0
        left = self.checkb(head.left)
        right = self.checkb(head.right)
        if left != -1 and right != -1:
            if abs(left - right) > 1:
                return -1
            else:
                return max(left, right) + 1
        return -1
