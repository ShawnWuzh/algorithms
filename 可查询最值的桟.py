'''
定义桟的数据结构，请在该类型中实现一个能够得到桟最小元素的min函数，要求时间复杂度为o(1)
'''
# written by HighW
'''
千万要注意，不要把函数和属性的命名弄成一模一样的哦。本题的思想就是一定要注意。本题的思路就是用另一个保存最小数的桟，同步地和数据桟同时地进行push操作和pop操作。只是在每次进行
push和pop桟的，需要保证最小数的桟里始终保存当前数据桟的最小数。
'''

class MyStack:
    def __init__(self):
        self.data = []
        self.min_stack = []
        self.size = 0

    def push(self, node):
        self.data.append(node)
        if not self.size:
            self.min_stack.append(node)
        else:
            if node <= self.min_stack[-1]:
                self.min_stack.append(node)
        self.size += 1

    def pop(self):
        if self.data[-1] <= self.min_stack[-1]:
            self.min_stack.pop()
        self.size -= 1
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def min(self):
        return self.min_stack[-1]

if __name__ == '__main__':
    A = [3,1,2,3,4,5,6]
    stack = MyStack()
    for i in range(len(A)):
        stack.push(A[i])
    print(stack.min())
