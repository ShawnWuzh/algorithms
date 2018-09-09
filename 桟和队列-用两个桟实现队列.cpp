/*
用两个桟来实现队列，完成队列的push和pop操作，队列中的元素为int类型。
*/

#include <stack>
#include <iostream>

using namespace std;

class Solution{
public:
  int pop(){
    int top;
    if(!stack2.empty()){
      top = stack2.top();
      stack2.pop();     // 一定要记住C++ stack的pop函数是没有返回值的。
      return top;
    }
    else{
      while(!stack1.empty()){
        top = stack1.top();
        stack1.pop();
        stack2.push(top);
      }
      top =  stack2.top();
      stack2.pop();
      return top;
    }
  }
  void push(int node){
    stack1.push(node);
  }

private:
  stack<int> stack1;
  stack<int> stack2;

};

int main(int argc, char const *argv[]) {
  /* code */
  Solution s;
  s.push(1);
  s.push(2);
  s.push(3);
  cout<<s.pop()<<endl;
  return 0;
}
