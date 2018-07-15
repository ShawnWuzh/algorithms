'''
编写一个类,只能用两个栈结构实现队列,支持队列的基本操作(push，pop)。

给定一个操作序列ope及它的长度n，其中元素为正数代表push操作，为0代表pop操作，保证操作序列合法且一定含pop操作，请返回pop的结果序列。

测试样例：
[1,2,3,0,4,0],6
返回：[1,2]
'''
'''
桟一定要把握住先进后出的特性，然后只能从一端进出，而队列是先进先出，一边进，一边出。桟和队列的题一定要牢牢把握住这两点。
'''
class TwoStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def twoStack(self, ope, n):
        result = []
        for i in ope:
            if i > 0:
                self.push(i)
            if i == 0:
                result.append(self.pop())
        return result

    def push(self, element):
        self.stack1.append(element)

    def pop(self):
        if len(self.stack2) == 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__ == '__main__':
    ope = [1,2,3,0,4,0]
    stack = TwoStack()
    print(stack.twoStack(ope,6))
