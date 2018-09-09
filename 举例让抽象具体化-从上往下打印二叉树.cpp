/*
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
*/

/*
本题就是层序遍历的体现。就是队列的运用，只是此时一定要注意特殊情况，当树的根节点也是空结点
的时候。
*/

#include <iostream>
#include <queue>

using namespace std;

struct TreeNode{
  int val;
  struct TreeNode* left;
  struct TreeNode* right;
  TreeNode(int x):
    val(x),left(NULL),right(NULL){}
};


class Solution{

public:
  vector<int> PrintFromTopToBottom(TreeNode *root){
    vector<int> result;
    if(!root){   // 一定要注意这里要检查是否为空，如果把空节点入队，会出现segmentation fault.
      return result;
    }
    queue<TreeNode*> q;
    TreeNode* curNode = root;
    q.push(curNode);
    TreeNode* p= NULL;
    while(!q.empty()){
      p = q.front();
      q.pop();
      result.push_back(p->val);
      if(p->left){
        q.push(p->left);
      }
      if(p->right){
        q.push(p->right);
      }
    }
    return result;
  }
};

int main(int argc, char const *argv[]) {
  TreeNode a(4);
  TreeNode b(5);
  TreeNode c(6);
  a.left = &b;
  a.right = &c;
  Solution s;
  vector<int> result = s.PrintFromTopToBottom(&a);
  cout<<result[0]<<" "<<result[1]<<" "<<result[2];
  return 0;
}
