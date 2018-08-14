'''
一棵二叉树原本是搜索二叉树，但是其中有两个节点调换了位置，使得这棵二叉树不再是搜索二叉树，
请找到这两个错误节点并返回他们的值。保证二叉树中结点的值各不相同。给定一棵树的根结点，请返回两
个调换了位置的值，其中小的值在前。
'''
'''
首先搞清楚搜索二叉树的中序遍历得到的一定是一个升序的序列， 所以一旦这个序列不再是升序的序列，
一定其中有节点的位置出现了错误。也就是说升序序列中间会有局部的降序，但是当我们找到了降序的位置
之后，我们如何确定哪一个是我们的出错的节点了。这就有两种情况了，第一种情况就是，整个序列只有一处
降序，那么此时降序中两个点都是我们出错的节点，也就是相邻的点发生了交换。第二种情况就是，整个
序列中有两处出现了降序，那么就说明调换位置的两个节点并不是相邻的，此时，对第一处降序，大的那个节点
是错误节点， 对于第二处降序，小的那个节点是错误节点。
'''

class FindErrorNode:
    def findError(self, root):
        data = []
        self.inOrder(root,data)
        prev = data[0]
        decrease = []
        for i in range(1,len(data)):
            if data[i] < prev:
                decrease.append((prev,data[i]))
            prev = data [i]
        return decrease[-1][1],decrease[0][0]
    def inOrder(self, root, data):
        if root:
            self.inOrder(root.left,data)
            data.append(root.val)
            self.inOrder(root.right, data)
