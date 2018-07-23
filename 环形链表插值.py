'''
有一个整数val，如何在节点值有序的环形链表中插入一个节点值为val的节点，并且保证这个环形单链表依然有序。

给定链表的信息，及元素的值A及对应的nxt指向的元素编号同时给定val，请构造出这个环形链表，并插入该值。

测试样例：
[1,3,4,5,7],[1,2,3,4,0],2
返回：{1,2,3,4,5,7}
'''
'''
链表的题目，一定要找到头节点，一切操作，遍历都是通过头节点来进行的。遍历都是用一个临时Node来保存当前的node，然后
从头部开始遍历。循环链表结束的位置就是当一个节点的下一个节点等于head的时候。做的时候如果发现想不通，一定要画下图，
应该就会很清楚了。
'''
# written by HighW
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class InsertValue:
    def insert(self, A, nxt, val):
        head = ListNode(A[0])
        nextLoc = nxt[0]
        curNode = head
        while nextLoc != 0:
            node = ListNode(A[nextLoc])
            curNode.next = node
            nextLoc = nxt[nextLoc]
            curNode = node
        curNode.next = head
        prev = head
        next = head.next
        while True:
            if val <= next.val and val >= prev.val:
                break
            else:
                prev = next
                next = next.next
            if next == head:
                break
        new_node = ListNode(val)
        prev.next = new_node
        new_node.next = next
        return head

if __name__ == '__main__':
    A = [1,3,4,5,7]
    nxt = [1,2,3,4,0]
    val = 2
    iv = InsertValue()
    head = iv.insert(A,nxt,val)
    print(head.next.val)
