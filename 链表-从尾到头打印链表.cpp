/*
输入一个链表，按链表值从尾到头的顺序返回一个ArrayList.
*/
#include <stack>
#include <vector>
#include <iostream>
using namespace std;
struct ListNode{
  int val;
  struct ListNode *next;
  ListNode(int x):
    val(x), next(NULL){
    }
};

class Solution {
public:
  vector<int> printListFromTailToHead(ListNode* head){
    version1 use stack
    vector<int> result;
    stack<int> reverseResult;
    struct ListNode* curNode = head;
    while(curNode){
      reverseResult.push(curNode->val);
      curNode = curNode->next;
    }
    while(!reverseResult.empty()){
      result.push_back(reverseResult.top());
      reverseResult.pop();
    }
    return result;
    // version2 use recursion
    // vector<int> result;
    // vector<int> &r = result;
    // printList(head,r);
    // return result;

  }
  // void printList(ListNode* pNode,vector<int> &r){
  //   if(pNode->next){
  //     printList(pNode->next,r);
  //   }
  //   r.push_back(pNode->val);
  // };
};

int main(int argc, char const *argv[]) {
  ListNode a(3);
  struct ListNode* pHead = &a;
  ListNode b(4);
  a.next = &b;
  Solution s;
  vector<int> result = s.printListFromTailToHead(pHead);
  for(int i=0;i < result.size();i++){
    cout<<result.at(i)<<endl;
  }
  return 0;
}
