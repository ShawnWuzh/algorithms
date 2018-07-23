'''
对于一个链表，我们需要用一个特定阈值完成对它的分化，使得小于等于这个值的结点移到前面，大于该值的结点在后面，同时保证两类结点内部的位置关系不变。
给定一个链表的头结点head，同时给定阈值val，请返回一个链表，使小于等于它的结点在前，大于等于它的在后，保证结点值不重复。
测试样例：
{1,4,2,5},3
{1,2,4,5}
'''
'''
本题有两种思路，第一种思路就是，将该链表变成一个数组， 然后利用类似快排的思路，最后将数组链表化。第二种思路就是不利用额外的数组， 直接
在原有的链表上构造新的链表。比该数小的构建一个链表，等于该数的为一个链表，大于该数的为一个链表。然后把这三个链表连接起来。本题我们将实现这两种
思路。
第一种思路实现的时候注意： 类似与这种要将一个序列分成两段的题目，找到两段的分解线就是突破口，然后在后续的过程中，移动这个分界线就行了。
第二种思路实现的方法就是，比该数小的构建一个链表， 比该数大的构建一个链表。构建这两个链表的时候分别各用两个指针来记录：head指针和尾指针。
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Divide:
    def listDivide(self, head, val):
        # version 1
        # transform the linked list to array
        # array = []
        # curNode = head
        # while curNode:
        #     array.append(curNode.val)
        #     curNode = curNode.next
        # # separate the array
        # i = 0
        # separation = -1
        # while(i < len(array)):
        #     if(array[i] <= val):
        #         j = i
        #         temp = array[j]
        #         while(j > separation):
        #             array[j] = array[j-1]
        #             j -= 1
        #         separation += 1
        #         array[separation] = temp
        #     i += 1
        # # transform the array to linked list
        # if len(array) == 1:
        #     head = ListNode(array[0])
        #     return head
        # else:
        #     head = ListNode(array[0])
        #     curNode = head
        #     i = 1
        #     while(i < len(array)):
        #         newNode = ListNode(array[i])
        #         curNode.next = newNode
        #         curNode = newNode
        #         i += 1
        # return head
        # version2
        hasHead1 = False
        hasHead2 = False
        curNode = head
        head1,head2,tail1,tail2 = None, None,None,None
        while curNode:
            if curNode.val > val:
                if not hasHead2:
                    head2 = ListNode(curNode.val)
                    tail2 = head2
                    hasHead2 = True
                else:
                    newNode = ListNode(curNode.val)
                    tail2.next = newNode
                    tail2 = newNode
            else:
                if not hasHead1:
                    head1 =  ListNode(curNode.val)
                    tail1 = head1
                    hasHead1 = True
                else:
                    newNode = ListNode(curNode.val)
                    tail1.next = newNode
                    tail1 = newNode
            curNode = curNode.next
        tail1.next = head2
        return head1

if __name__ == '__main__':
    A = [1,4,2,5]
    head = ListNode(A[0])
    curNode = head
    for i in range(1,len(A)):
        newNode = ListNode(A[i])
        curNode.next = newNode
        curNode = newNode
    d = Divide()
    head = d.listDivide(head,3)
    curNode = head
    while curNode:
        print(curNode.val)
        curNode = curNode.next
