'''
请用非递归方式实现二叉树的先序、中序和后序的遍历打印。
给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToSequence:

    def convert(self, root):
        data = [[] for i in range(3)]
        self.preOrder(root, data[0])
        self.inOrder(root, data[1])
        self.postOrder(root, data[2])
        return data

    def preOrder(self, root, result):
        stack = []
        stack.append(root)
        while len(stack):
            curNode = stack.pop()
            result.append(curNode.val)
            if curNode.right:
                stack.append(curNode.right)
            if curNode.left:
                stack.append(curNode.left)

    def inOrder(self, root, result):
        stack = []
        curNode = root
        while(curNode):
            stack.append(curNode)
            curNode = curNode.left
        while(len(stack)):
            curNode = stack.pop()
            result.append(curNode.val)
            rightTree = curNode.right
            curNode = rightTree
            while(curNode):
                stack.append(curNode)
                curNode = curNode.left

    def postOrder(self, root, result):
        # version1, use two stacks to do this
        # 后续遍历的顺序是左右根，其实我们可以把它看成根右左的逆序，如果我们把根右左实现了，对他进行逆序就是左右根了啊
        stack1 = []
        stack2 = []
        stack1.append(root)
        while(len(stack1)):
            curNode = stack1.pop()
            stack2.append(curNode)
            if curNode.left:
                stack1.append(curNode.left)
            if curNode.right:
                stack1.append(curNode.right)
        while(len(stack2)):
            result.append(stack2.pop().val)
