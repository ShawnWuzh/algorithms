'''
如何判断一个单链表是否有环？有环的话返回进入环的第一个节点的值，无环的话返回-1。如果链表的长度为N，请做到时间复杂度O(N)，额外空间复杂度O(1)。
给定一个单链表的头结点head（注意另一个参数adjust为加密后的数据调整参数，方便数据设置，与本题求解无关)，请返回所求值。
'''
'''
第一种思路就是，每一个节点，我都遍历他之前，如果发现他之前也出现了该节点，那么说明该节点就是入环的第一个节点， 但是该方法的时间复杂度太高，为O(N^2)如果没有空间复杂度的限制的话，我们可以用一个Hash表来表示，这样很轻松地就可以找到入环的第一个节点值。但是本题有空间复杂度的限制
因此不能使用hash表。第三种思路就是用两个指针，一快一慢，快指针一次移两步，慢指针一次移一步，那么如果有环的话，他们必然会在环内相遇。然后把慢指针移动到开始的位置，快指针从相遇的位置开始移动，但此时以慢指针的速度移动，最终相遇的点就是第一次入环的点，本题画图思路会很清晰。特别注意，由于是单链表，所以环一定是处于链表的尾部。
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class ChkLoop:
    def chkLoop(self,head,adjust):
        if not head:
            return -1
        fastPointer = head
        slowPointer = head
        flag = -1
        while fastPointer.next and slowPointer:
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
            if fastPointer == slowPointer:
                flag = 0
                meetPoint = fastPointer
                break
        if flag == -1:
            return flag
        else:
            slowPointer = head
            fastPointer = meetPoint
            while slowPointer and fastPointer:
                if fastPointer == slowPointer:
                    return fastPointer.val
                slowPointer = slowPointer.next
                fastPointer = fastPointer.next
