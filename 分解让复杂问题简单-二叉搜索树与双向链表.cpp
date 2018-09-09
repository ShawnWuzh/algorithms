/*
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向.
*/
/*
二叉树的中序遍历的应用，中序遍历的结果就是一个有序的序列。我们用left指针来表示链表中结点的
下一个结点，用right指针来表示链表中结点的上一个节点。这样就构成了我们的双向链表。本题有递归
和非递归两种方法，其实就是对应的二叉树的中序遍历。二叉树的很多题目其实都是二叉树三种遍历代码
的改写.
*/

#include <iostream>
#include <stack>

using namespace std;


struct TreeNode{
  int val;
  struct TreeNode *left,*right;
  TreeNode(int x):
  val(x), left(NULL),right(NULL){}
};

class Solution{
public:
  TreeNode* pHead;
  TreeNode* pLast;
  TreeNode* Convert(TreeNode* pRootOfTree){

    // 非递归版本
  //   TreeNode* cur = pRootOfTree;
  //   TreeNode* right = NULL;
  //   TreeNode* pHead = NULL;
  //   TreeNode* pLast = NULL;
  //   stack<TreeNode*> s;
  //   while(cur){
  //     s.push(cur);
  //     cur = cur->left;
  //   }
  //   while(!s.empty()){
  //     cur = s.top();
  //     s.pop();
  //     right = cur->right;
  //     while(right){
  //       s.push(right);
  //       right = right->left;
  //     }
  //     if(!pHead){
  //       pHead = cur;
  //       pHead->left = NULL;
  //       pLast = pHead;
  //     }
  //     else{
  //       pLast->right = cur;
  //       cur->left = pLast;
  //       pLast = cur;
  //     }
  //   }
  // return pHead;
  // 递归版本
  pHead = NULL;
  pLast = NULL;
  myConvert(pRootOfTree);
  return pHead;

  }
  void myConvert(TreeNode* pCur){
    if(pCur){
      myConvert(pCur->left);
      if(!pHead){
        pHead = pCur;
        pLast = pCur;
      }
      else{
        pLast->right = pCur;
        pCur->left = pLast;
        pLast = pCur;
      }
      myConvert(pCur->right);
    }
  }
};

int main(){
  TreeNode* root = new TreeNode(6);
  root->left = new TreeNode(5);
  root->right = new TreeNode(8);
  Solution s;
  TreeNode* pHead = s.Convert(root);
  cout<<pHead->val<<pHead->right->val<<pHead->right->right->val<<endl;
  cout<<pHead->right->right->val<<pHead->right->right->left->val<<pHead->right->right->left->left->val<<endl;
  return 0;
}
