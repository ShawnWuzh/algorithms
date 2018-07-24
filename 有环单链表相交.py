'''
如何判断两个有环单链表是否相交？相交的话返回第一个相交的节点，不想交的话返回空。如果两个链表长度分别为N和M，请做到时间复杂度O(N+M)，额外空间复杂度O(1)。
给定两个链表的头结点head1和head2(注意，另外两个参数adjust0和adjust1用于调整数据,与本题求解无关)。请返回一个bool值代表它们是否相交。
'''
'''
本题的思路：先找出两个环入环的节点，然后判断两个环的节点是否相等，如果相等，该问题就变成找头结点到该公共节点(记住此时链表长度就应该是头结点到
该公共节点的长度了)的单链表无环相交点的问题了。那么如果两个环的入环节点不相等，怎么办？那么如果两个环相交，必然相交点在环上，且必然相交点有两个，分别是
两个环的入环点，所以我们以其中一个环的入环点为起始点开始遍历，如果遍历回到该节点都没有找到一个节点与另一个环的入环点相等，说明两个环没有相交。
'''
class ListNode:

    def __init__(self,x):
        self.val = x
        self.next = None

class ChkIntersection:
    def chkInter(self, head1,head2,adjust0,adjust1):
        # find the entering node of the circle for each linked list
        enteringNode1 = self.findEnteringCircle(head1)
        enteringNode2 = self.findEnteringCircle(head2)
        if enteringNode1 == enteringNode2:
            # 利用无环链表找相交点的方式来找，只是此时的循环终止条件不一样了。
            curHead1 = head1
            curHead2 = head2
            n = self.length(head1,enteringNode1)
            m = self.length(head2,enteringNode2)
            while n > m:
                n -= 1
                curHead1 = curHead1.next
            while m > n:
                m -= 1
                curHead2 = curHead2.next
            while n > 0:
                if curHead1 == curHead2:
                    return curHead1
                n -= 1
                curHead1 = curHead1.next
                curHead2 = curHead2.next
            return enteringNode1
        else:
            curNode = enteringNode1.next
            while curNode != enteringNode1:
                if curNode == enteringNode2:
                    return enteringNode1
                curNode = curNode.next
            return None

    def findEnteringCircle(self, head):
        fastPointer = head
        slowPointer = head

        while fastPointer and fastPointer.next and slowPointer:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                break
        slowPointer = head

        while slowPointer != fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        return fastPointer
    def length(self,head,entering):
        curNode = head
        n = 0
        while curNode != entering:
            n += 1
            curNode = curNode.next
        return n
