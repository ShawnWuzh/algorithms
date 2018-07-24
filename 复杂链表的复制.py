'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点)。要求不借助额外数据结构。
'''
'''
本题的难点在于random指针的复制。记住链表的题目一定要考虑特殊情况，链表为空，链表长度为1。还要在遍历过程中，一定要注意这种情况：
a = curNode.next, 当curNode为None的时候，是会报错的。思路不清晰的时候就要画图，然后注意循环的终止条件。
'''
class RandomListNode:
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def clone(self, pHead):

        # 特殊情况的判定
        if not pHead:
            return None
        if not pHead.next:
            return RandomListNode(pHead.label)
        # copy previous node
        curNode = pHead
        while curNode:
            next = curNode.next
            copyNode = RandomListNode(curNode.label)
            curNode.next = copyNode
            copyNode.next = next
            curNode = next

        # copy random pointer
        prev = pHead
        while prev:
            curNode = prev.next
            if prev.random:
                curNode.random = prev.random.next
            prev = curNode.next

        # split the linked list into two parts
        copyHead = pHead.next
        curNode = pHead
        while curNode.next:
            next = curNode.next
            curNode.next = next.next
            curNode = next
        return copyHead
