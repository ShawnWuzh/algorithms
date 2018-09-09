/*
给一个链表，若其中包含环，请找出该链表的环的入口节点，否则，输出null.
*/
// 用一个快指针，一个慢指针，如果有环的话，快指针必然会在环上某一位置相遇。
#include <iostream>
struct ListNode{
  int val;
  struct ListNode* next;
  ListNode(int x):   // in C++, the only difference bewteen class and a struct is that members ans base classed are private by default in
  // classes, whereas they are public by default in structs. So structs can have constructors, ans the syntax is the same for classes.
    val(x), next(NULL){  // this is called member initialization list in c++. We recommend you to use member initialization list in all cases.
      // this was like a constructor  
    }
};

class Solution {
public:
  ListNode* EntryNodeOfLoop(ListNode* pHead){
      struct ListNode* pFast = pHead;
      struct ListNode* pSlow = pHead;
      while(pFast && pSlow){
        pSlow = pSlow->next;
        if(pFast->next){
          pFast = pFast->next->next;
        }
        else{
          pFast = pFast->next;
        }
        if(pFast == pSlow){
          break;
        }
      }
      if(pFast && pSlow){
        pSlow = pHead;
        while(pFast != pSlow){
          pFast = pFast->next;
          pSlow = pSlow->next;
        }
        return pSlow;
      }
      else{
        return NULL;
      }
  }
};
int main(int argc, char const *argv[]) {
  /* code */
  ListNode a(2);
  struct ListNode* pHead = &a;
  Solution s;
  std::cout << s.EntryNodeOfLoop(pHead)->val;
  return 0;
}
