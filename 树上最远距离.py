'''
从二叉树的节点A出发，可以向上或者向下走，但沿途的节点只能经过一次，当到达节点B时，路径上的节点数叫作A到B的距离。对于给定的一棵二叉树，求整棵树上节点间的最大距离。

给定一个二叉树的头结点root，请返回最大距离。保证点数大于等于2小于等于500.
'''

'''
二叉树的很多题目其实都是对前序，中序，后序遍历的代码进行改写，所以要对前序，中序，后序的递归掌握得非常熟练，一定要
理解到递归的本质。本题最大距离可能有三种来源，第一种就是左子树里的节点最大距离，第二种就是右子树的节点最大距离，第三种
就是左子树里面的离左子树的根节点最远的距离 + 右子树里面的离右子树的根节点的最远的距离 + 1， 最大距离就是这三种的最大值。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class LongestDistance:
    def findLongest(self, root):
        result = self.postOrder(root)
        return result[0]
    def postOrder(self, root):
        if root:
            lMax1, lMax2 = self.postOrder(root.left)
            rMax1, rMax2 = self.postOrder(root.right)
            hmax2 = max(lMax2, rMax2) + 1
            hmax1 = max(lMax1, rMax1, lMax2 + rMax2 + 1)
            return hmax1, hmax2
        else:
            return 0,0
