'''
有一个单链表，请设计一个算法，使得每K个节点之间逆序，如果最后不够K个节点一组，则不调整最后几个节点。例如链表1->2->3->4->5->6->7->8->null，K=3这个例子。调整后为，3->2->1->6->5->4->7->8->null。因为K==3，所以每三个节点之间逆序，但其中的7，8不调整，因为只有两个节点不够一组。给定一个单链表的头指针head,同时给定K值，返回逆
序后的链表的头指针。
'''
'''
思路一就是利用一个桟来进行逆序。逆序其实很容易联想到使用桟来解决。构建链表通常的思路就是，用一个flag来表示当前的节点是不是头节点，然后用一个tail来表示尾结点，方便后面
添加节点。思路二就是不使用额外的数据结构，直接在链表上操作。这种思路非常考验代码实现的能力，常在面试当中考到。这里考虑使用两种方式，一种是迭代的方法，另一种是递归的方法。
再次提醒，写算法题，先要想清楚整体思路，比如用几个变量来表示，大概的步骤是怎样的，不要考虑太多的细节。本题的步骤其实就是两步：第一步就是怎么把一个子链表逆序，第二步就是
如何把这些子链表串起来。然后我需要保存逆序过后的子链表的结尾，那我就用一个变量来保存就行了。
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class KInverse:
    def inverse(self, head, k):
        # 思路一的代码
        # stack = []
        # curNode = head
        # newHead,tail = None, None
        # hasHead = False
        # n = 0
        # while curNode:
        #     stack.append(curNode.val)
        #     n += 1
        #     if n == k:
        #         while n > 0:
        #             newNode = ListNode(stack.pop())
        #             if not hasHead:
        #                 newHead = newNode
        #                 tail = newHead
        #                 hasHead = True
        #             else:
        #                 tail.next = newNode
        #                 tail = newNode
        #             n -= 1
        #     curNode = curNode.next
        # if len(stack):
        #     newStack = []
        #     while(len(stack)):
        #         newStack.append(stack.pop())
        #     while(len(newStack)):
        #         newNode = ListNode(newStack.pop())
        #         tail.next = newNode
        #         tail = newNode
        # return newHead:
        # 思路二的代码(循环实现)
        n = 0
        curNode = head
        prev,subHead,next,subTail = None, None, None, None
        newHead, newTail = None, None
        hasHead = False
        while curNode:
            n += 1
            if n == 1:
                subTail = curNode
            elif n == k:
                subHead = subTail
                # the following is to reverse K nodes
                while n > 0:
                    next = subHead.next
                    subHead.next = prev
                    prev = subHead
                    subHead = next
                    n -= 1
                curNode = subHead
                # the following is to add the current reversed linked list to previous finished reversed linked lists
                if not hasHead:
                    newHead = prev
                    hasHead = True
                    newTail = subTail
                else:
                    newTail.next = prev
                    newTail = subTail
                prev = None
                continue
            curNode = curNode.next
        if n > 0:
            if newHead:
                newTail.next = subTail
            else:
                newHead = subTail
        return newHead
        # 思路二的代码(递归实现)
        

if __name__ == '__main__':
    A = [1,4,2,5]
    head = ListNode(A[0])
    curNode = head
    for i in range(1,len(A)):
        newNode = ListNode(A[i])
        curNode.next = newNode
        curNode = newNode
    d = KInverse()
    head = d.inverse(head,2)
    curNode = head
    while curNode:
        print(curNode.val)
        curNode = curNode.next
