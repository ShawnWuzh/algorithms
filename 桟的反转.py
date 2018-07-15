'''
实现一个栈的逆序，但是只能用递归函数和这个栈本身的操作来实现，而不能自己申请另外的数据结构。

给定一个整数数组A即为给定的栈，同时给定它的大小n，请返回逆序后的栈。

测试样例：
[4,3,2,1],4
返回：[1,2,3,4]
'''
'''
这道题的关键在于搞清楚递归的原理：递归的实现就是用桟来实现的，每一次递归的时候，都会把函数里的变量压入一个桟中，记录下来以便
稍后函数返回的时候能够回到之前的状态继续执行。本题利用了递归最大的一个特征，用一个临时变量来保存每一次调用函数的结果，而这个临时变量
会被压入到函数调用栈。思路就是我们实现一个提取桟底元素的函数getBottom：利用递归，用一个临时变量来保存递归函数的返回值，然后每一次递归
都会把当前的值保存到调用栈中，然后依次从调用栈中弹出来再压入我们自己的桟中（除桟底元素外）。然后我们再利用递归函数，递归的从桟中每一次取出
桟底的元素，每一次这个桟底元素会被压入到函数调用栈中，递归结束后，会从依次从函数调用桟中弹出来，被压入到我们自己的桟中。本题精髓就是利用了
递归函数的实现就是利用了函数调用栈，因此我们不需要自己在新建一个栈了，只需要利用这个递归函数的桟就可以帮助我们变换顺序了。
'''

class StackReverse:
    def reverseStack(self, A, n):
        self.reverse(A)
        return A

    def reverse(self,A):
        if len(A):
            bottom = self.getBottom(A)
            self.reverse(A)
            A.append(bottom)

    def getBottom(self,A):
        result = A.pop()
        if len(A):
            last = self.getBottom(A)
            A.append(result)
            return last
        return result
if __name__ == '__main__':
    A = [4,3,2,1]
    reverse = StackReverse()
    print(reverse.reverseStack(A,4))
