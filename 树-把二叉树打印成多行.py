'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #返回二维列表
    def Print(self, pRoot):
        result = [[]]
        queue = []
        if not pRoot:
            return []
        queue.append(pRoot)
        curLast = pRoot
        end = pRoot
        while(len(queue)):
            curNode = queue.pop(0)
            if curNode.left:
                queue.append(curNode.left)
                curLast = curNode.left
            if curNode.right:
                queue.append(curNode.right)
                curLast = curNode.right
            if curNode == end:
                result[-1].append(curNode.val)
                result.append([])
                end = curLast
            else:
                result[-1].append(curNode.val)
        return result[:-1]
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    s= Solution()
    print(s.Print(root))
