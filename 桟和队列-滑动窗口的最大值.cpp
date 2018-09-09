/*
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
*/
/*
采用双端队列的思路进行求解。这是一道滑动窗口的问题。用一个队列，队列的头部为当前窗口的最大值，
每一次窗口移动时，即当我们的数向右移动的时候。先检查一下当前队列的头部的下标是否在窗口内，如果
不在，则将该元素从队列头部弹出，然后继续检查新的队列头部，直到在窗口内。接着我们需要将新的元素
加入到我们的队列中，加入的时候，我们比较新元素与队尾的元素，如果新元素小于队尾的元素，则将新元素
加入到队尾中，如果新元素大于队尾的元素，则将队尾的元素从队尾中弹出，继续比较新的队尾。 最后将
我们的队头的元素加入到结果中。最后注意一点，我们加入到队列中的不是我们的元素本身，而是他们的下标。
*/


#include <vector>
#include <iostream>
#include <deque>
using namespace std;

class Solution{
public:
  vector<int> maxInWindows(const vector<int>& num, unsigned int size){
    // version1
    // vector<int> result;
    // int begin = 0;
    // int end = begin + size - 1;
    // int resultSize = 0;
    // while(end < num.size()){
    //   if(resultSize == 0){
    //   result.push_back(findMax(num, begin, end));
    // }
    // else{
    //   if(num[end] >= result[resultSize-1]){
    //     result.push_back(num[end]);
    //   }
    //   else{
    //     result.push_back(findMax(num,begin,end));
    //   }
    // }
    // begin += 1;
    // end = begin + size - 1;
    // }
    // return result;
    //version 2
    deque<int> maxq;
    vector<int> result;
    for(int i=0;i<num.size();i++){
      while(!maxq.empty() && num[maxq.back()] < num[i]){
          maxq.pop_back();
        }
        maxq.push_back(i);
        if(i >= size - 1){
          while(!maxq.empty() && maxq.front() < i - size + 1){
            maxq.pop_front();
          }
          result.push_back(num[maxq.front()]);
        }
    }
    return result;

  }
  // int findMax(const vector<int>& num, int start, int end){
  //   int max = num[start];
  //   for(int i=start;i<=end;i++){
  //     if(num[i] > max){
  //       max = num[i];
  //     }
  //   }
  //   return max;
  // }
};
int main(int argc, char const *argv[]) {
  int array[8] = {2,3,4,2,6,2,5,1};
  vector<int> a(array,array+8);
  vector<int>& b = a;
  Solution s;
  vector<int> max = s.maxInWindows(b,3);
  for(int i =0;i<max.size();i++){
    cout<<max.at(i)<<endl;
  }
  return 0;
}
