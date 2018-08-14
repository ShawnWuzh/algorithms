'''
有一棵二叉树，其中所有节点的值都不一样,找到含有节点最多 的搜索二叉子树,并返回这棵子树的头节点.

给定二叉树的头结点root，请返回所求的头结点,若出现多个节点最多的子树，返回头结点权值最大的。
'''
'''
本题其实依然是二叉树遍历代码的一个改写。本题需要用到二叉树的后序遍历，对于一颗二叉树，最大搜索树
有两种来源，第一种就是如果二叉树的左子树和右子树都是搜索树，然后左子树的最大节点小于头结点，右子树的
最小节点大于头结点，此时最大搜索树就是该头结点的二叉树。如果不满足上述条件，就是第二种情况，以左子树为
头结点的最大搜索树和以右子树为头结点的最大搜索树中结点数最多的一个就是最大搜索二叉树，如果结点数相等，
则取结点权值最大的那个为我们的结果。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MaxSubtree:
    def getMax(self, root):
        return self.postOrder(root)[0]
    def postOrder(self, root):
        if root.left and root.right:
            lhead, lnumNodes,lMin,lMax = self.postOrder(root.left)
            rhead, rnumNodes,rMin,rMax = self.postOrder(root.right)
            if lhead == root.left and rhead == root.right:
                if lMax < root.val and rMin > root.val:
                    return (root, lnumNodes + rnumNodes + 1, lMin, rMax)
            if lnumNodes > rnumNodes:
                return (lhead,lnumNodes,lMin, lMax)
            elif lnumNodes < rnumNodes:
                return (rhead,rnumNodes,rMin,rMax)
            else:
                if lhead.val < rhead.val:
                    return (rhead,rnumNodes,rMin,rMax)
                else:
                    return (lhead,lnumNodes,lMin,lMax)
        elif root.left and not root.right:
            lhead, lnumNodes, lMin, lMax = self.postOrder(root.left)
            if lhead == root.left:
                if lMax < root.val:
                    return (root,lnumNodes + 1, lMin, root.val)
            return(lhead,lnumNodes, lMin, lMax)
        elif root.right and not root.left:
            rhead, rnumNodes, rMin, rMax = self.postOrder(root.right)
            if rhead == root.right:
                if rMin > root.val:
                    return (root,rnumNodes + 1, root.val, rMax)
            return(rhead,rnumNodes, rMin, rMax)
        else:
            return (root,1,root.val,root.val)
