/*
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
*/
/*
二叉搜索树的中序遍历是一个递增序列。但是前序和后序遍历貌似没有什么显然的顺序结果。但是后序遍历的结果最后
一个结点一定是根节点,然后之前的序列，前一半部分所有结点一定比根节点小，后半部分一定比根节点大，然后
我们就可以递归地检查左半部分和右半部分。首先我们需要找到前半部分和和后半部分的分界点。
*/
/*
9
72
681416
6 8 7 14 16 2 9
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
    bool VerifySequenceOfBST(vector<int> sequence){
      if(!sequence.size()){
        return false;
      }
      return myVerify(sequence,0,sequence.size()-1);
    }
    bool myVerify(vector<int> sequence,int start, int end){
      if(start >= end){
        return true;
      }
      int i = end-1;
      while(i >= start && sequence[i] > sequence[end]){
        i--;
      }
      for(int j=i;j>=start;j--){
        if(sequence[j] > sequence[end]){
          return false;
        }
      }
      return myVerify(sequence,start, i) && myVerify(sequence,i+1,end-1);
      // 其实下面的代码写的复杂了，说明思路还是不清晰，一定要把思路理清晰，然后再开始写代码。
      // if(start >= end){
      //   return true;
      // }
      // int rightS,rightE,leftS,leftE;
      // rightE=rightS=leftS=leftE=-1;
      // int root = sequence[end];
      // for(int i=end-1;i>=start;i--){
      //   if(sequence[i] < root){
      //     leftE = i;
      //     break;
      //   }
      // }
      // // does not exist left tree
      // if(leftE == -1){
      //   return myVerify(sequence, start, end-1);
      // }
      // // does not exist right tree
      // else if(leftE == end - 1){
      //   for(int i=0; i <= leftE-1; i++){
      //     if(sequence[i] > root){
      //       return false;
      //     }
      //   }
      //   return myVerify(sequence, start, end-1);
      // }
      // else{
      //   rightS = leftE + 1;
      //   rightE = end -1;
      //   leftS = 0;
      //   for(int i=0;i<leftE;i++){
      //     if(sequence[i] > root){
      //       return false;
      //     }
      //   }
      //   return myVerify(sequence,leftS,leftE) && myVerify(sequence, rightS, rightE);
      // }
    }
};

int main(int argc, char const *argv[]) {
  int a[] = {6,8,7,14,16,15,9};
  vector<int> b(a,a+7);
  Solution s;
  cout<<s.VerifySequenceOfBST(b);
  return 0;
}
