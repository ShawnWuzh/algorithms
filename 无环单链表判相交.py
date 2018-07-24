'''
现在有两个无环单链表，若两个链表的长度分别为m和n，请设计一个时间复杂度为O(n + m)，额外空间复杂度为O(1)的算法，判断这两个链表是否相交。
给定两个链表的头结点headA和headB，请返回一个bool值，代表这两个链表是否相交。保证两个链表长度小于等于500。
'''
'''
第一种思路依然是采用hash表，先根据第一个链表把hash表构建出来，然后再在第二个链表上表示，如果发现有重复值，则说明相交，这个点即为第一个相交的
节点。但是本题要求额外空间复杂度为O(1)，所以排除该种思路。第二种思路，首先我们要搞清楚什么叫相交，相交的意思就是从相交的节点开始到最后一个节点
两个链表都是公用的,(why? 因为是单链表，所以每个节点只有一个next指针，当找到一个相交节点，则必然该节点之后的节点都必须是相同的)所以，如果两个链表相交，
则必然他们的最后一个节点是相同的。我们先让长的链表先走短链表的长度步，然后长链表和短链表开始一起走，一发现相同的节点，该节点即为相交部分的第一个节点，如
果一直到两个链表的最后位置，都没有发现相同的节点，则表示不相交。第三种思路就是，把其中一个链表A的尾指针指向另一个链表B的头指针，然后判断B链表是否有环。
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class CheckIntersect:
    def chkIntersect(self, headA, headB):
        n = 0
        m = 0
        curNode = headA
        while curNode:
            n += 1
            curNode = curNode.next
        curNode = headB
        while curNode:
            m += 1
            curNode = curNode.next
        curNodeA = headA
        curNodeB = headB
        while n > m:
            n -= 1
            curNodeA = curNodeA.next
        while m > n:
            m -= 1
            curNodeB = curNodeB.next
        while curNodeA and curNodeB:
            if curNodeA == curNodeB:
                return True
            curNodeA = curNodeA.next
            curNodeB = curNodeB.next
        return False
