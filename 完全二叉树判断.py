'''
有一棵二叉树,请设计一个算法判断它是否是完全二叉树。
给定二叉树的根结点root，请返回一个bool值代表它是否为完全二叉树。树的结点个数小于等于500。
'''
'''
首先要搞清楚，什么是完全二叉树，就是该二叉树的每一层都应该是满的，除了最后一层可以不满，而且
最后一层所有的结点必须在二叉树的最左边。解决思路就是采用按层遍历的方式进行，如果某一个结点
有右孩子但是没有左孩子，直接返回False, 如果某一个结点有左孩子，但是没有右孩子，那么之后的节点
必须为叶节点，最终，遍历结束之后，返回true。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CheckCompletion:
    def chk(self, root):
        queue = []
        leafFlag = 0
        queue.append(root)
        while len(queue):
            curNode = queue.pop(0)
            if leafFlag:
                if curNode.left or curNode.right:
                    return False
                continue
            if curNode.left:
                if curNode.right:
                    queue.append(curNode.left)
                    queue.append(curNode.right)
                else:
                    leafFlag = 1
            else:
                if curNode.right:
                    return False
        return True
