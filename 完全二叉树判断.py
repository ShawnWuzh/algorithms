'''
有一棵二叉树,请设计一个算法判断它是否是完全二叉树。

给定二叉树的根结点root，请返回一个bool值代表它是否为完全二叉树。树的结点个数小于等于500。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CheckCompletion:
    def chk(self, root):
