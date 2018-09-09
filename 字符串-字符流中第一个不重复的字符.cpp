/*
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
*/

#include <queue>
#include <iostream>

using namespace std;


class Solution{
public:
  void Insert(char ch){
    int ascii_value = (int)ch;
    if(asc[ascii_value] == 0){
      q.push(ch);
    }
    asc[ascii_value]++;
  }

  Solution(){
    fill(asc,asc+128,0);
  }

  char FirstAppearingOnce(){
    while(!q.empty() && asc[(int)q.front()] != 1){
      q.pop();
    }
    if(q.empty()){
      return '#';
    }
    else{
      return q.front();
    }
  }

private:
  queue<char> q;
  int asc[128];
};

int main(int argc, char const *argv[]) {
  Solution s;
  char s1[3] = "go";
  char s2[7] = "google";
  for(int i=0;i<7;i++){
    s.Insert(s2[i]);
  }
  cout<<s.FirstAppearingOnce()<<endl;
  return 0;
}
