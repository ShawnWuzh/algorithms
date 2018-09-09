/*
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
*/

/*
首先根据前序遍历我们可以确定树的根节点, 然后根据中序遍历我们找到根节点，然后中序遍历中根节点左边的数目
就是左子树的数目，右边的数目就是右子树的数目。然后根据前序遍历的结果找出左子树和右子树的根节点。
*/


#include <iostream>
#include <vector>

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
    TreeNode* reConstructBinaryTree(vector<int> pre, vector<int> vin){
    TreeNode* root = myConstruct(pre,vin,0,pre.size()-1,0,vin.size()-1);
    return root;
  }
  TreeNode* myConstruct(vector<int> pre, vector<int> vin, int preStart,int preEnd,int inStart,int inEnd){
    if(preStart > preEnd || inStart > inEnd){
      return NULL;
    }
    int root = pre[preStart];
    TreeNode* p = new TreeNode(root);   //注意这里的用法。
    // TreeNode root(pre[preStart]);  //这种方法不得行，
    // TreeNode* p = &root;

    int rootIndex;
    for(int i=inStart;i<=inEnd;i++){
      if(vin[i] == pre[preStart]){
        rootIndex = i;
        p->left = myConstruct(pre,vin, preStart+1, preStart+ rootIndex - inStart,inStart, rootIndex-1);
        p->right = myConstruct(pre,vin, preStart + rootIndex -inStart + 1, preEnd,rootIndex + 1, inEnd);
        break;
      }
    }
    return p;
  }
};

int main(int argc, char const *argv[]) {
  int a[]={1,2,4,7,3,5,6,8};
  int b[]={4,7,2,1,5,3,8,6};
  vector<int> c(a,a+8);
  vector<int> d(b,b+8);
  Solution s;
  TreeNode* root = s.reConstructBinaryTree(c,d);
  cout<<root->val;
  return 0;
}
