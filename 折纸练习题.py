'''
请把纸条竖着放在桌⼦上，然后从纸条的下边向上⽅对折，压出折痕后再展 开。此时有1条折痕，突起的⽅向指向纸条的背⾯，这条折痕叫做“下”折痕 ；突起的⽅向指向纸条正⾯的折痕叫做“上”折痕。如果每次都从下边向上⽅ 对折，对折N次。请从上到下计算出所有折痕的⽅向。

给定折的次数n,请返回从上到下的折痕的数组，若为下折痕则对应元素为"down",若为上折痕则为"up".

测试样例：
1
返回：["down"]
'''
'''
折完纸的结果其实就是一棵二叉树，而且就是一颗满二叉树，该二叉树的根节点是下折痕，然后每一棵子树
的左结点是上折痕，右结点是下折痕。构建出这颗二叉树之后，然后按照右中左的顺序打印这颗二叉树，就是
将折痕从上到下打印出来的结果。
'''


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class FoldPaper:
    def foldPaper(self, n):
        queue = []
        root = TreeNode('down')
        queue.append(root)
        i = 2
        while i <= n:
            lastLevel = 2 ** ((i-1) - 1)
            while lastLevel:
                curNode = queue.pop(0)
                curNode.left = TreeNode('up')
                curNode.right = TreeNode('down')
                queue.append(curNode.left)
                queue.append(curNode.right)
                lastLevel -= 1
            i += 1
        # result = []
        # queue = []
        # curNode = root
        # queue.append(curNode)
        # while(len(queue)):
        #     curNode = queue.pop(0)
        #     result.append(curNode.val)
        #     if curNode.left:
        #         queue.append(curNode.left)
        #     if curNode.right:
        #         queue.append(curNode.right)
        stack = []
        result = []
        curNode = root
        while curNode:
            stack.append(curNode)
            curNode = curNode.right
        while(len(stack)):
            curNode = stack.pop()
            result.append(curNode.val)
            leftNode = curNode.left
            while leftNode:
                stack.append(leftNode)
                leftNode = leftNode.right
        return result
if __name__ == '__main__':
    fold = FoldPaper()
    n = 2
    print(fold.foldPaper(n))
