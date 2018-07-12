'''
请编写一个方法，将字符串中的空格全部替换为“%20”。假定该字符串有足够的空间存放新增的字符，并且知道字符串的真实长度(小于等于1000)，同时保证字符串由大小写的英文字母组成。

给定一个string iniString 为原始的串，以及串的长度 int len, 返回替换后的string。

测试样例：
"Mr John Smith”,13
返回："Mr%20John%20Smith"
”Hello  World”,12
返回：”Hello%20%20World”
'''
# written by HighW
'''
首先统计出空格的数目，然后算出最终字符串的长度，然后从字符串的最后面开始遍历，遇到非空格，就移动到新字符串的对应位置，如果遇到空格，在相应位置上填上规定字符。
'''
class Replacement:
    def replaceSpace(self, iniString, length):
        num_space = 0
        for i in range(length):
            if iniString[i] == ' ':
                num_space += 1
        new_length = length - num_space + num_space * 3
        new_string = [None for i in range(new_length)]
        for j in range(length-1,-1,-1):
            if iniString[j] != ' ':
                new_string[new_length-1] = iniString[j]
                new_length -= 1
            else:
                new_string[new_length-1] = '0'
                new_string[new_length-2] = '2'
                new_string[new_length-3] = '%'
                new_length -= 3
        return ''.join(new_string)

if __name__ == '__main__':
    replacement = Replacement()
    iniString = "aabcb"
    print(replacement.replaceSpace(iniString,5))
