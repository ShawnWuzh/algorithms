'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''
本题考查的是二叉树的中序非递归遍历。思路就是我们用一个变量在中序遍历中保存上一个遍历的结点，对于每一个现在遍历到的结点，
如果之前的结点等于我们要找的下一个节点，该结点就是我们要找的中序遍历的结点。但是本题有一个问题，我们只知道我们要找的那
一个结点，并不知道这棵树的根节点，当然我们可以一直往上查找，找到根节点，这种方法效率太低。其实我们可以这样考虑，当给出
的这个结点的右子树不为空的时候，则下一个结点必定为右子树的最左结点。那如果右子树为空的话，就会有两种情况，第一种，给出
的结点是他父节点的左子树的时候，下一个结点必定为父节点，如果是父节点的右子树的时候，说明父节点的左子树，右子树，以及父
节点都打印完了，这个时候我们需要继续往上找，检查父节点是不是父节点的父节点的左子树，如果是。返回父节点的父节点，如果不
是，继续往上遍历，知道找到一个父节点是其父节点的左子树。
'''
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None # 这个是指向父节点的指针。

class Solution:
    def GetNext(self, pNode):
        # 方法1
        # 找到根节点
        # curNode = pNode
        # while(curNode.next):
        #     curNode = curNode.next
        # root = curNode
        # # 对二叉树进行中序遍历
        # prev = None
        # result = []
        # stack = []
        # curNode = root
        # while(curNode):
        #     stack.append(curNode)
        #     curNode = curNode.left
        # while(len(stack)):
        #     curNode = stack.pop()
        #     result.append(curNode)
        #     rightNode = curNode.right
        #     while(rightNode):
        #         stack.append(rightNode)
        #         rightNode = rightNode.left
        # for i in range(len(result)-1):
        #     if result[i] == pNode:
        #         return result[i+1]
        # return None
        # 方法二
        if not pNode:
            return None
        curNode = pNode.right
        if curNode:
            while curNode.left:
                curNode = curNode.left
            return curNode
        # 右子树为空，这种情况下需要我们去找到他的父节点
        parent = pNode.next
        curNode = pNode
        while(parent and parent.left != curNode):
            curNode = parent
            parent = parent.next
        return parent 
