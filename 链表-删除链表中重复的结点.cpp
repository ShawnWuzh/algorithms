/*
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
*/
/*
本题非常容易将代码写复杂，写复杂的原因还是因为没有把问题想清除，首先我们需要搞清楚什么样的结点
叫重复，如果一个结点的值和他下一个结点的值相等，说明该节点出现了重复，那么此时我们应该怎么办？
此时不应该立即删除，而是应该继续把后面结点中也等于该值的结点找出来，直到某一个结点的值不等于
该值，此时，该节点到当前结点之前的结点我们都应该删除。怎么删除？直接把之前最后一个不重复的结点
next指针指向当前结点即可，然后再对当前结点进行同样的操作。如果当前结点不是重复结点，直接把他
加入最后的序列中。本题其实就是借用了3个指针，prev, cur, next。链表的很多题目都是用多个指针
进行操作来解题。
*/

#include <iostream>
using namespace std;

struct ListNode{
  int val;
  struct ListNode* next;
  ListNode(int x): val(x),next(NULL){}
};

class Solution{
public:
  ListNode* deleteDuplication(ListNode* pHead){
    ListNode* pPrev = NULL;
    ListNode* pCur = pHead;
    ListNode* pNext = NULL;
    while(pCur){
      if(pCur->next && pCur->next->val == pCur->val){
        pNext = pCur->next;
        while(pNext && pNext->val == pCur->val){
          pNext = pNext->next;
        }
        if(pCur == pHead){
          pHead = pNext;
        }
        else{
          pPrev->next = pNext;
        }
        pCur = pNext;
    }
    else{
      pPrev = pCur;
      pCur = pCur->next;
    }
  }
  return pHead;
  }
};

int main(int argc, char const *argv[]) {
  /* code */
  ListNode a(1);
  ListNode b(2);
  ListNode c(2);
  ListNode d(4);
  ListNode *pHead = &a;
  pHead->next = &b;
  pHead->next->next = &c;
  pHead->next->next->next = &d;
  Solution s;
  ListNode *newHead = s.deleteDuplication(pHead);
  ListNode *cur = newHead;
  while(cur){
    cout<<cur->val<<endl;
    cur = cur->next;
  }
  return 0;
}
