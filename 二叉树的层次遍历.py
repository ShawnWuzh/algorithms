'''
有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。
给定二叉树的根结点root，请返回打印结果，结果按照每一层一个数组进行储存，所有数组的顺序按照层数从上往下，且每一层的数组内元素按照从左往右排列。保证结点数小于等于500。
'''
'''
本题的思路就是用两个变量，一个last保存当前层的最后一个node, nlast保存下一层的最后一个node。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreePrinter:
    def printTree(self, root):
        data = []
        queue = []
        last = root
        nlast = None
        curNode = root
        queue.append(curNode)
        level = []
        while(len(queue)):
            curNode = queue.pop(0)
            level.append(curNode.val)
            if curNode.left:
                queue.append(curNode.left)
                nlast = curNode.left
            if curNode.right:
                queue.append(curNode.right)
                nlast = curNode.right
            if last == curNode:
                data.append(level)
                level = []
                last = nlast
        return data
