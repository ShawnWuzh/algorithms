/*
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
*/

/*
本题最好的办法就是找出不符合整数要求的条件，把这些条件排除了，剩下的就是满足条件的了。
*/
#include <iostream>
using namespace std;


class Solution{
public:
  bool IsNumeric(char* string){
    // 如果该数是用科学计数法来表示的。则需要满足前半部分是数字，后半部分不能含有小数。
    int locE = checkE(string);
    if(locE != -1){
      return pureNumber(string,locE) && intNumber(string+locE+1);
    }
    // 如果该数不是用科学计数法来表示的。则只需要检测该数满足数字的特征就行了。
    else{
      return pureNumber(string, strlen(string));
    }

    //
  }
  bool intNumber(char* string){
    int i = 1;
    int length = strlen(string);
    if(((string[0] == 43 || string[0] == 45) && length > 1) || (string[0] <= 57 && string[0] >= 48)){
      while(*(string + i) != '\0'){
        if(string[i] <= 57 && string[i] >= 48){
          i += 1;
        }
        else{
          return false;
        }
      }
      return true;
    }
    else{
      return false;
    }
  }

  int checkE(char* string){
    int i = 0;
    while(*(string + i) != '\0'){
      if(*(string + i) == 'E' || *(string + i) == 'e'){
        return i;
      }
      i++;
    }
    return -1;
  }

  bool pureNumber(char* string, int length){
    int float_flag = 0;
    int i = 1;
    // this is used to check pure number,including float number
    if(((string[0] == 43 || string[0] ==45) && length > 1) || (string[0] <= 57 && string[0] >= 48)){
      while(i < length){
        if(string[i] <= 57 && string[i] >= 48){
          i += 1;
        }
        else if(string[i] == 46 && float_flag == 0){
          i += 1;
          float_flag = 1;
        }
        else{
          return false;
        }
      }
      return true;
    }
    else{
      return false;
    }
  }
};

int main(int argc, char const *argv[]) {
  char *string = "1a3.14";
  Solution s;
  cout<<s.IsNumeric(string);
  return 0;
}
