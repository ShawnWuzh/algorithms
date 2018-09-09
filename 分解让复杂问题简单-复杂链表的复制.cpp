/*
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
*/

/*
第一种首先是暴力的解法，我们先按照复制简单链表的方式复制链表，也就是说复制的过程中我们先不考虑random的指针，
然后接下来就是复制每一个结点里面的random指针，由于每一个结点在链表里的位置是一定的。我们可以遍历原来的链表
找到每一个random指针所指的位置，在复制链表中找到相应的位置，这个位置就是复制链表中random指针所指的位置。
可以看出遍历原始链表找出random指针指的位置是本题开销很大的地方。
第二种方法就是我们用空间来换取时间的方式来解决random指针的问题，用map或者hashtable来保存原链表和复制链表中的结点之间
的对应关系。我们使用C++中的map来实现。
第三种方法就是不利用额外的空间来进行复制，我们先像复制常规链表那样进行复制，但是我们把每一结点的复制结点插入到
原结点的后面，这样操作的原因是，方便后面我们进行random指针的复制。具体来说：A->A'->B->B'. A的random指针
指向B，那么我们很容易让A’的random指针指向B'，因为每一个结点的复制结点就在其后面。最后我们再将这个链表拆分
成两个链表。
*/

#include <iostream>
#include <map>

using namespace std;

struct RandomListNode{
  int label;
  struct RandomListNode *next, *random;
  RandomListNode(int x):
  label(x),next(NULL),random(NULL){}
};

class Solution{
public:
  RandomListNode* Clone(RandomListNode* pHead){

    // version1: use extra space to save time
    // RandomListNode* pNew = NULL;
    // if(!pHead){
    //   return pNew;
    // }
    // map<RandomListNode*, RandomListNode*> links;
    // RandomListNode* pCur = pHead->next;
    // RandomListNode* pCopy = new RandomListNode(pHead->label);
    // pNew = pCopy;
    // links.insert(map<RandomListNode*,RandomListNode*>::value_type(pHead,pCopy));
    // while(pCur){
    //   pCopy->next = new RandomListNode(pCur->label);
    //   pCopy = pCopy->next;
    //   links.insert(map<RandomListNode*,RandomListNode*>::value_type(pCur,pCopy));
    //   pCur = pCur->next;
    // }
    // pCur = pHead;
    // while (pCur) {
    //   if(pCur->random){
    //   links.find(pCur)->second->random = links.find(pCur->random)->second;
    // }
    //   pCur = pCur->next;
    // }
    // return pNew;

    // version 2 : does not use extra space to save time
    RandomListNode* cur = pHead;
    RandomListNode* temp = NULL;
    if(!pHead){
      return temp;
    }
    while(cur){
      temp = cur->next;
      cur->next = new RandomListNode(cur->label);
      cur->next->next = temp;
      cur = temp;
    }
    cur = pHead;
    while(cur->next->next){
      if(cur->random){
        cur->next->random = cur->random->next;
      }
        cur = cur->next->next;
    }
    RandomListNode* pNew = pHead->next;
    cur = pHead;
    while(cur->next->next){
      temp = cur->next;
      cur->next = temp->next;
      temp->next = cur->next->next;
      cur = cur->next;
    }
    cur->next = NULL;

    return pNew;
  }
};
int main(int argc, char const *argv[]) {
  RandomListNode* pHead = new RandomListNode(4);
  pHead->next = new RandomListNode(5);
  pHead->next->next = new RandomListNode(7);
  pHead->random = pHead->next->next;
  Solution s;
  RandomListNode* newH = s.Clone(pHead);
  cout<<newH->label<<newH->next->label<<newH->next->next->label<<newH->random->label<<endl;
  return 0;
}
