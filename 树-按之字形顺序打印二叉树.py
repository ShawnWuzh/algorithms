'''
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''
第一种思路就是遇到偶数层，先输出，再逆序。第二种思路就是当我们在遍历的过程中的时候，运用堆栈来帮我们实现这个过程。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # version 1
    def Print(self,pRoot):
        if not pRoot:
            return []
        queue = []
        result = [[]]
        curLast = pRoot
        end = pRoot
        queue.append(pRoot)
        i = 1
        while(len(queue)):
            curNode = queue.pop(0)
            if curNode.left:
                queue.append(curNode.left)
                curLast = curNode.left
            if curNode.right:
                queue.append(curNode.right)
                curLast = curNode.right
            if curNode == end:
                end = curLast
                result[-1].append(curNode.val)
                if i % 2 == 0:
                    result[-1].reverse()
                result.append([])
                i += 1
            else:
                result[-1].append(curNode.val)
        return result[:-1]

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.right = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node1.left = node2
    node4 = TreeNode(4)
    node1.right = node4
    root.left = node1
    print(s.Print(root))
