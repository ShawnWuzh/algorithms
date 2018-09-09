/*
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
*/
/*
本题其实就是带记忆功能的DFS的应用，本题的关键是要注意，路径定义是从树的根节点
往下一直到叶节点。因此我们从根结点开始往下搜索，用一个数组保存当前的路径，每搜索
一个结点，就把该结点加入到当前的路径中，如果当前的节点的左右子树都已搜索完毕，则将
当前结点从路径数组中弹出来，如果当前结点已经满足了条件，而且是叶节点的话，表示当前路径
符合条件，则把当前路径添加到结果中，而且还要把当前结点从当前路径中弹出来。

本题还要注意一下vecor pass by reference 和 pass by value.注意默认的情况下， vector
作为参数传入函数，函数会做一个copy，这样会导致开销过大，所以我们最好是用传入reference的方法，
传入vector,当我们不想要函数更改我们的vecor的时候，可以传入一个const的vector reference。
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

  static bool sortBySize(vector<int> a, vector<int> b){
    return a.size() > b.size();
  }
  vector<vector<int> > FindPath(TreeNode* root, int expectNumber){
    vector<vector<int> > result;
    vector<int> curPath;
    addToPath(result, curPath, root, expectNumber);
    sort(result.begin(),result.end(),sortBySize);
    return result;
  }
  void addToPath(vector<vector<int> > &result, vector<int> &curPath, TreeNode* curNode, int expectNumber){
    if(curNode){
      int newExpect = expectNumber - curNode->val;
      curPath.push_back(curNode->val);
      if(newExpect == 0 && !curNode->left && !curNode->right){
        result.push_back(curPath);
      }
        if(curNode->left){
          addToPath(result,curPath,curNode->left,newExpect);
        }
        if(curNode->right){
          addToPath(result,curPath,curNode->right,newExpect);
        }
        if(!curPath.empty()){
        curPath.pop_back();
    }
  }
}
};

int main(){
  Solution s;
  TreeNode* root = new TreeNode(10);
  root->left = new TreeNode(5);
  root->right = new TreeNode(12);
  root->left->left = new TreeNode(4);
  root->left->right = new TreeNode(7);
  vector<vector<int> > result = s.FindPath(root,22);
  if(!result.empty()){
    cout<<result[0][0]<<result[0][1]<<result[0][2]<<result[1][0]<<result[1][1];
  }
  else{
    cout<<"empty";
  }
  return 0;
}
