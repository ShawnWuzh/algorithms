/*
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
注意：本题保证输入字符串后面有足够的空间供我们进行操作，
*/

// 本题需要学到的就是，如果我们从前到后的遍历的话，遇到空格的时候，需要将后面的字符都要进行移动，如果
// 每个空格都会导致后面的n个字符进行移动，时间复杂度为O(n^2),但是如果我们从后往前遍历的话，每个字符
// 后面都是空的，直接移动该字符就行了，用两个数，一个用来保存原来的最后一个下标，另一个用来表示新
// 的字符串的起始点。本题要学到从前往后复杂度过大，我们就从后往前进行操作。


#include <iostream>

using namespace std;

class Solution{
public:
  void replaceSpace(char *str, int length){  // 本题还要注意传进来的指针变量的值，所以在函数里对指针变量进行的所有修改对原指针的内容都没有影响。
    // int max_length = 3 * length;
    // char a[max_length];
    // int i = 0;
    // int j = 0;
    // while(i < length){
    //   if(str[i] == ' '){
    //     a[j++] = '%';
    //     a[j++] = '2';
    //     a[j++] = '0';
    //   }
    //   else{
    //     a[j++] = str[i];
    //   }
    //   i++;
    // }
    // a[j] = '\0';
    // cout<<a<<endl;
    // *str = 'f';    // this will cause bus error, since you are trying to change the string literal, which is a constant, cannot be changed.
    // 接下来我们采取从后往前的顺序进行移动
    // 首先我们需要统计空格的字符数量
    int size = 0;
    int numSpace = 0;
    while(str[size] != '\0'){
      if(str[size] == ' '){
        numSpace++;
      }
      size++;
    }
    size++;
    int newsize = size + numSpace * 2;
    while(size > 0){
      if(str[size-1] != ' '){
        str[newsize-1] = str[size - 1];
        newsize--;
        size--;
      }
      else{
        str[newsize-- - 1] = '0';
        str[newsize-- - 1] = '2';
        str[newsize-- - 1] = '%';
        size--;
      }
    }
  }
};

int main(int argc, char const *argv[]) {
  char str[100] = "We are happy";
  Solution s;
  s.replaceSpace(str,12);
  cout<<str<<endl;
  return 0;
}
