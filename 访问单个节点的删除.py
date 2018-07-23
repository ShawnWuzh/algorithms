'''
实现一个算法，删除单向链表中间的某个结点，假定你只能访问该结点。
给定带删除的头节点和要删除的数字，请执行删除操作，返回删除后的头结点。链表中没有重复数字
要求时间复杂度为O(1)。这个题是常考题。
'''

'''
如果不要求时间复杂度的话，我们可以采用从头结点开始遍历的方法，来找出该节点，然后再删除。但是本题
要求时间复杂度，因此我们采用这样的方法，当删除的结点是头节点的时候，我们直接把头节点指向头节点的下一个
节点，当要删除的节点是尾结点的时候，直接把该node删除即可。当该节点是中间的某个结点是，把下一个节点的
值拷贝到该节点中，该节点的下一个节点为下一个节点的下一个节点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Remove:
    def removeNode(self, pHead, delVal):
        # the following code: time complexity O(n)
        cur = pHead
        if cur.val == delVal:
            pHead = cur.next
            return pHead
        while cur:
            if cur.next.val == delVal:
                break
            cur = cur.next
        cur.next = cur.next.next
        return pHead
    def deleteNode(self, node):
        # write your code here
        # the following code, time complexity O(1)
        if node.next == None:
            del node
        else:
            node.val = node.next.val
            node.next = node.next.next
