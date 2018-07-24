'''
给定两个单链表的头节点head1和head2，如何判断两个链表是否相交？相交的话返回true，不想交的话返回false。

给定两个链表的头结点head1和head2(注意，另外两个参数adjust0和adjust1用于调整数据,与本题求解无关)。请返回一个bool值代表它们是否相交。

并不知道这两个单链表是否有环。
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class ChkIntersection:
    def chkInter(self, head1, head2, adjust0, adjust1):
        #先检查两个链表有不有环。
        enteringNode1 = self.checkCircle(head1)
        enteringNode2 = self.checkCircle(head2)
        if enteringNode1 and not enteringNode2:
            return False
        elif enteringNode2 and not enteringNode1:
            return False
        elif not enteringNode1 and not enteringNode2:
            return self.checkNoCircle(head1,head2)
        else:
            if enteringNode1 == enteringNode2:
                return True
            else:
                curNode = enteringNode1.next
                while curNode != enteringNode1:
                    if curNode == enteringNode2:
                        return True
                    curNode = curNode.next
                return False



    def checkCircle(self,head):
        slowPointer = head
        fastPointer = head
        while slowPointer and fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                break
        slowPointer = head
        while slowPointer != fastPointer:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next
        return fastPointer
    def checkNoCircle(self,head1,head2):
        n = self.lengthNoCircle(head1)
        m = self.lengthNoCircle(head2)
        curHead1 = head1
        curHead2 = head2
        while n > m:
            n -= 1
            curHead1 = curHead1.next
        while m > n:
            m -= 1
            curHead2 = curHead2.next
        while curHead1 and curHead2:
            if curHead1 == curHead2:
                return True
            curHead1 = curHead1.next
            curHead2 = curHead2.next
        return False
    def lengthNoCircle(self,head):
        n = 0
        curNode = head
        while curNode:
            n += 1
            curNode = curNode.next
        return n
