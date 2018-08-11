'''
请用递归方式实现二叉树的先序、中序和后序的遍历打印。
给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)。
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreePrinter:
    def printTree(self, root):
        data = [[] for i in range(3)]
        self.preOrder(root,data[0])
        self.inOrder(root,data[1])
        self.postOrder(root,data[2])
        return data
    def preOrder(self, root,result):
        if root:
            result.append(root.val)
            self.preOrder(root.left,result)
            self.preOrder(root.right,result)
    def inOrder(self, root,result):
        if root:
            self.inOrder(root.left,result)
            result.append(root.val)
            self.inOrder(root.right,result)
    def postOrder(self, root,result):
        if root:
            self.postOrder(root.left,result)
            self.postOrder(root.right, result)
            result.append(root.val)
