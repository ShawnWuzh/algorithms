'''
现有两个升序链表，且链表中均无重复元素。请设计一个高效的算法，打印两个链表的公共值部分。

给定两个链表的头指针headA和headB，请返回一个vector，元素为两个链表的公共部分。请保证返回数组的升序。两个链表的元素个数均小于等于500。保证一定有公共值

测试样例：
{1,2,3,4,5,6,7},{2,4,6,8,10}
返回：[2.4.6]

'''
'''
本题的关键在于两个升序链表，升序很关键，利用两个指针的移动，比较大小，当其中一个比另一个小的时候，显然应该移动小的指针，大的那个指针不变，因为首先
链表是升序排列的。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Common:
    def findCommonParts(self, headA, headB):
        common = []
        curNode1 = headA
        curNode2 = headB
        while curNode1 and curNode2:
            if curNode1.val == curNode2.val:
                common.append(curNode1.val)
                curNode1 = curNode1.next
                curNode2 = curNode2.next
            elif curNode1.val < curNode2.val:
                curNode1 = curNode1.next
            else:
                curNode2 = curNode2.next
        return common
