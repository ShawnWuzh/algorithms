/*
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
*/
#include <stack>
#include <iostream>


using namespace std;

class Solution{
public:
  void push(int value){
    data.push(value);
    if(minS.empty() || value < minS.top()){
      minS.push(value);
    }
    else{
      minS.push(minS.top());
    }
  }

  void pop(){
    data.pop();
    minS.pop();
  }

  int top(){
    return data.top();
  }

  int min(){
    return minS.top();
  }
private:
  stack<int> data;
  stack<int> minS;
};

int main(){
  Solution s;
  s.push(5);
  s.push(4);
  s.push(3);
  s.push(6);
  s.pop();
  s.pop();
  cout<<s.min()<<endl;
  return 0;
}
