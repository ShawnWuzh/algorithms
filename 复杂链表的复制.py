'''
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）。

'''
class RandomListNode:

    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None




class Solution:
    def clone(self, pHead):
