'''
首先我们介绍二叉树先序序列化的方式，假设序列化的结果字符串为str，初始时str等于空字符串。先序遍历二叉树，如果遇到空节点，就在str的末尾加上“#!”，“#”表示这个节点为空，节点值不存在，当然你也可以用其他的特殊字符，“!”表示一个值的结束。如果遇到不为空的节点，假设节点值为3，就在str的末尾加上“3!”。现在请你实现树的先序序列化。
给定树的根结点root，请返回二叉树序列化后的字符串。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeToString:
    def toString(self, root):
        # this is the version for preOrder
        stack = []
        stack.append(root)
        string = ''
        while(len(stack)):
            curNode = stack.pop()
            if curNode:
                string += str(curNode.val) + '!'
                stack.append(curNode.right)
                stack.append(curNode.left)
            else:
                string += '#!'
        return string

        # this is the version for inOrder
        '''
        stack = []
        curNode = root
        while(True):
            stack.append(curNode)
            if curNode:
                curNode = curNode.left
            else:
                break
        string = ''
        while(len(stack)):
            curNode = stack.pop()
            if not curNode:
                string += '#!'
            else:
                string += str(curNode.val) + '!'
                curNode = curNode.right
                if not curNode:
                    stack.append(curNode)
                else:
                    while(True):
                        stack.append(curNode.left)
                        if(curNode.left):
                            curNode = curNode.left
                        else:
                            break
        '''
