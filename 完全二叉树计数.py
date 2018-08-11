'''
给定一棵完全二叉树的根节点root，返回这棵树的节点个数。如果完全二叉树的节点数为N，请实现时间复杂度低于O(N)的解法。
给定树的根结点root，请返回树的大小。
'''
'''
首先搞清楚完全二叉树的定义，若设二叉树的深度为h，除第h层外，其他各层的结点数都达到最大个数，第h层所有的结点都连续
集中在最左边。首先根据树的最左边的结点确实出树的高度，然后，找到根节点的右子树的最左结点，如果该结点所在的高度等于了树的高度，
就意味着左边那棵树一定是排满了，所以可以由树的高度算出左边那棵树的结点数，然后再加上根节点，然后对右子树进行同样的递归操作。
如果根结点的右子树的最左结点的高度小于了树的高度，那么就表示，右边这颗树一定是排满了，根据右边这颗树的高度可以算出，然后加上
根节点，然后递归地对左子树进行相同的操作。
这里再补充一下树的高度和深度的区别：深度：对于任意节点n, n的深度为从根到n的唯一路径长，根的深度为0。高度：对于任意节点n,n的高度为
从n到一片树叶的最长路径长，所有树叶的高度为0。高度是从下往上数，深度是从上往下数。
已知一棵满二叉树的深度为n，结点总数为2^(n+1) - 1
'''
# written by HighW
'''
本题为什么能利用二分搜索？本题就是通过右子树的最左结点来进行分割，从而只需要对另一半进行递归。记住二分搜索就是找到一个条件，将原来的
数据分成两个部分，然后只在其中一部分进行操作。本题的时间复杂度为(LogN)^2。对数进行递归的时候，一定要注意边界条件，比如根节点为空，或者
树里面只有一个结点。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CountNodes:
    def count(self,root):
        if not root:
            return 0
        elif not root.left and not root.right:   # 当树里面只有一个结点的时候，当然就可以直接返回了啊
            return 1
        else:
            treeHeight = 0
            curNode = root.left
            while(curNode):
                treeHeight += 1
                curNode = curNode.left
            # check the right tree
            rightHeight = 0
            curNode = root.right
            while(curNode):
                rightHeight += 1
                curNode = curNode.left
            if rightHeight == treeHeight:
                numOfNodes_left = 2 ** (treeHeight) - 1
                return numOfNodes_left + 1 + self.count(root.right)
            elif rightHeight < treeHeight:
                numOfNodes_right = 2 ** (rightHeight) - 1
                return numOfNodes_right + 1 + self.count(root.left)
