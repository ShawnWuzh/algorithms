'''
对于两棵彼此独立的二叉树A和B，请编写一个高效算法，检查A中是否存在一棵子树与B树的拓扑结构完全相同。

给定两棵二叉树的头结点A和B，请返回一个bool值，代表A中是否存在一棵同构于B的子树。
'''
# written by HighW

# class TreeNode():
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
本题的思路就是，我们先利用先序遍历将二叉树序列化，然后得到两个字符串str1和str2，最后利用KMP算法(我们这里使用Python的string.Find())去在str1中匹配str2，
如果匹配成功，则说明str2存在于str1中。
'''
'''
这里要特别注意Python里的函数调用既不是call by value也不是call by reference,而是call by object。
variables in python are just references, they refer the actual objects we are working with. The most important thing is
that there are differences between immutable and mutable objects: 当传入的是mutable的objects的时候，call by reference, 但是如果在调用函数里面变量重新
指向了了另一个新的object的时候，就不再是call by reference了。如果传入的是immutable， call by value.Python里面string是immutable的，所以本题的策略是利用list来传入，
最后用join把list合成字符串。
'''

import string

# class KMP():
#     def search_pattern(self, text, pattern):
#         pmt = self.partial_match_table(pattern)
#
#     def partial_match_table(self, pattern):
#         for i in range(len(pattern)):



class IdenticalTree:
    def chkIdentical(self, A, B):
        str1 = []
        self.serialization(str1,A)
        str2 = []
        self.serialization(str2,B)
        # kmp = KMP()
        # if(kmp.search_pattern() != -1):
        #     return True
        # else:
        #     return False
        str1 = ''.join(str1)
        str2 = ''.join(str2)
        if str1.find(str2) == -1 :
            return False
        else:
            return True

    def serialization(self, string, root):
        # here we use pre-order to serialize the tree
        if root:
            string.append(str(root.val) + '!')
            self.serialization(string,root.left)
            self.serialization(string,root.right)
        else:
            string.append('#!')
