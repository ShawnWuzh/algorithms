'''
现在有一个单链表。链表中每个节点保存一个整数，再给定一个值val，把所有等于val的节点删掉。

给定一个单链表的头结点head，同时给定一个值val，请返回清除后的链表的头结点，保证链表中有不等于该值的其它值。请保证其他元素的相对顺序。

测试样例：
{1,2,3,4,3,2,1},2
{1,3,4,3,1}

'''

# written by HighW
'''
这个题应该没有什么难度，就是一个简单的遍历链表，然后删除链表中的节点，其实就是链表的一些基本操作。第一种思路就是用一个构造一个新链表。第二种思路就是
在原来的链表上操作。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ClearValue:
    def clear(self, head, val):
        #思路一
        # newHead, newTail = None, None
        # curNode = head
        # while curNode:
        #     if curNode.val != val:
        #         if not newHead:
        #             newHead = ListNode(curNode.val)
        #             newTail = newHead
        #         else:
        #             newNode = ListNode(curNode.val)
        #             newTail.next = newNode
        #             newTail = newNode
        #     curNode = curNode.next
        # return newHead
        # 思路二
        while head:
            if head.val != val:
                break
            else:
                head = head.next
        prev = head
        curNode = prev.next
        while curNode:
            if curNode.val == val:
                prev.next = curNode.next
            else:
                prev = curNode
            curNode = curNode.next
        return head

if __name__ == '__main__':
    A = [16,14]
    head = ListNode(A[0])
    curNode = head
    for i in range(1,len(A)):
        newNode = ListNode(A[i])
        curNode.next = newNode
        curNode = newNode
    d = ClearValue()
    head = d.clear(head,16)
    curNode = head
    while curNode:
        print(curNode.val)
        curNode = curNode.next
