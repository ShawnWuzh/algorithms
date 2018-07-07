'''
现在有一个行和列都排好序的矩阵，请设计一个高效算法，快速查找矩阵中是否含有值x。
给定一个int矩阵mat，同时给定矩阵大小nxm及待查找的数x，请返回一个bool值，代表矩阵中是否存在x。所有矩阵中数字及x均为int范围内整数。保证n和m均小于等于1000。
测试样例：
[[1,2,3],[4,5,6],[7,8,9]],3,3,10
返回：false
'''

'''
本题的思路就是从右上角开始遍历，当要找的元素比当前元素小的时候，从该元素的左边开始找，当要找的元素比当前元素大的时候，从该元素的下边开始找。
类似于查找这种类型的题，通常我们想根据一个指标值将元素划分成两个部分，比指标小的一部分，比指标大的一部分。类似于二分查找。
'''
# Written by HighW
class Finder():
    def findX(self,mat,n,m,x):
        i = 0
        j = m - 1
        while(i < n and j >= 0):
            if x == mat[i][j]:
                return True
            if x > mat[i][j]:
                i += 1
            else:
                j -= 1
        return False


if __name__ == '__main__':
    finder = Finder()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(finder.findX(mat,3,3,10))
