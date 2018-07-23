'''
请编写一个函数，检查链表是否为回文。
给定一个链表ListNode* pHead，请返回一个bool，代表链表是否为回文。
测试样例：
{1,2,3,2,1}
返回：true
{1,2,3,2,3}
返回：false

'''
'''
回文的意思就是当你把这个链表逆序过来，和原来的链表依然是一模一样的，这个就叫回文。所以，自然而然地就有了我们的第一种思路，
那就是把这个链表逆序过来，然后判断逆序过的链表和原链表是否一样。这个逆序过程需要靠一个桟来实现，因此额外的空间复杂度为O(n),
时间复杂度为O(n). 第二种思路就是，我们不需要借助桟来帮助我们逆序，直接在原链表上逆序，但是问题是，如果我们将整个链表逆序，原链表
就没了，那我们逆序过得链表和谁进行比较呢？所以，我们不把整个链表逆序，只把链表的后半部分逆序，然后比较前半部分和后半部分。最后再把
链表逆序回来。总结起来就是找到分界节点，然后把分界节点以及之后的节点进行逆序，然后进行判定，最后把分界节点以及之后的节点逆序回来。
'''
# written by HighW

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Palindrome:
    def isPalindrome(self, pHead):
        # 思路一：
        # stack = []
        # curNode = pHead
        # while curNode:
        #     stack.append(curNode.val)
        #     curNode = curNode.next
        # curNode = pHead
        # while curNode:
        #     val = stack.pop()
        #     if curNode.val != val:
        #         return False
        #     curNode = curNode.next
        # return True
        #思路二
        size = 0
        curNode = pHead
        while curNode:
            size += 1
            curNode = curNode.next
        border = size // 2
        n = 0
        curNode = pHead
        while curNode:
            n += 1
            if n == border:
                break
            curNode = curNode.next
        prev = None
        curHead, next = curNode, None
        while curHead:
            next = curHead.next
            curHead.next = prev
            prev = curHead
            curHead = next
        leftNode = pHead
        rightNode = prev
        n = 0
        flag = True
        while(n < border):
            if(leftNode.val != rightNode.val):
                flag = False
                break
            leftNode =leftNode.next
            rightNode = rightNode.next
            n += 1
        # recover the linked list to its original state
        newPrev = None
        curHead,next = prev, None
        while(curHead):
            next = curHead.next
            curHead.next = newPrev
            newPrev = curHead
            curHead = next
        return flag
if __name__ == '__main__':
    A = [1,2,3,2,1]
    head = ListNode(A[0])
    tail = head
    for i in range(1,len(A)):
        newNode = ListNode(A[i])
        tail.next = newNode
        tail = newNode
    p = Palindrome()
    print(p.isPalindrome(head))
    curNode = head
    while curNode:
        print(curNode.val)
        curNode = curNode.next
