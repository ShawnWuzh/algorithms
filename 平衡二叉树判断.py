'''
有一棵二叉树，请设计一个算法判断这棵二叉树是否为平衡二叉树。

给定二叉树的根结点root，请返回一个bool值，代表这棵树是否为平衡二叉树。
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CheckBalance:
    def check(self, root):
