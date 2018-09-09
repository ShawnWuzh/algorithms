'''
请实现两个函数，分别用来序列化和反序列化二叉树
'''
'''
本题我们使用前序遍历对二叉树进行序列化，反序列化的时候依然采用前序遍历。如果结点为空，
用#代替，一个结点的结尾用!表示。反序列化关键就是利用递归，因为我们知道字符串的一个数
一定是根节点，那么剩下的字符串的第一个数就是子树的根节点。
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, root):
        string = ''
        stack = []
        stack.append(root)
        while(len(stack)):
            curNode = stack.pop()
            if not curNode:
                string += '#,'
            else:
                string += str(curNode.val) + ','
                stack.append(curNode.right)
                stack.append(curNode.left)
        return string
    def Deserialize(self, s):
        nodes = s.split(',')
        root = self.decode(nodes)
        return root
    def decode(self, nodes):
        root_val = nodes.pop(0)
        if root_val == '#':
            return None
        root = TreeNode(int(root_val))
        root.left = self.decode(nodes)
        root.right = self.decode(nodes)
        return root

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node1.left = node2
    node4 = TreeNode(4)
    node1.right = node4
    root.left = node1
    string = s.Serialize(root)
    print(s.Deserialize(string).left.left.val)

 #    1
 #  2
 # 3  4
123##4##3
