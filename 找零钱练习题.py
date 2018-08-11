'''
有数组penny，penny中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值的货币可以使用任意张，再给定一个整数aim(小于等于1000)代表要找的钱数，求换钱有多少种方法。
给定数组penny及它的大小(小于等于50)，同时给定一个整数aim，请返回有多少种方法可以凑成aim。
测试样例：
[1,2,4],3,3
返回：2
'''
'''
首先我们先采用暴力递归的方式来求解，然后采用记忆搜索的方法，最后采用动态规划的方法。动态规划其实就是一种以空间换时间的方法。
'''
class Exchange:
    def countWays(self, penny, n, aim):
        table = {}
        new_table = [[0 for j in range(aim+1)] for i in range(len(penny))]
        for i in range(len(penny)):
            new_table[i][0] = 1
        i = 0
        while i * penny[0] <= aim:
            new_table[0][i*penny[0]] = 1
            i += 1
        return self.dpCounts(penny,0,aim,new_table)
    # 暴力解法
    def counts(self, penny, index, aim):
        res = 0
        if index >= len(penny) and aim != 0:
            return res
        elif index >= len(penny) and aim == 0:
            return 1
        num_current = 0
        while(True):
            if num_current * penny[index] > aim:
                break
            res += self.counts(penny, index+1, aim - num_current * penny[index])
            num_current += 1
        return res
    # 从上面的暴力解法可以看出，还有很多地方可以进行优化，比如可能会出现
    # 多次的递归，他们具有相同的index和aim，那么如果我们把这些相同的值给
    # 保存下来，那么下一次就不再需要进行递归了，从而可以节省很多的时间，这种
    # 方式叫做记忆搜索算法, 通过记忆搜索算法，我们的时间复杂度从开始的暴力搜索
    # 的933ms到61ms了，可以说是降了不少。
    def memoryCounts(self,penny,index,aim,table):
        res = 0
        if index >= len(penny) and aim != 0:
            return 0
        elif index >= len(penny) and aim == 0:
            return 1
        num_current = 0
        while True:
            if num_current * penny[index] > aim:
                break
            else:
                newAim = aim - num_current * penny[index]
                newIndex = index + 1
                if str(newAim) + '-' + str(newIndex) in table:
                    res += table[str(newAim) + '-' + str(newIndex)]
                else:
                    res += self.memoryCounts(penny, newIndex, newAim, table)
            num_current += 1
        table[str(aim)+ '-' + str(index)] = res
        return res
    # 上面的暴力算法，可以看出，其实就是遇到一个对应值，直接把该值放进一个字典里，而没有考虑
    # 状态之间的联系。table[i][j] = table[i-1][j-0*penny[i]] + （table[i-1][j- 1*penny[i]] + .... + table[i-1][j- num*penny[i]]）,
    # 相当于求某一个ij的时候，等于对他前一行的遍历之和。括号里其实可以用table[i][j-1*penny[i]]代替，这样，我们从左往右，从上往下计算，就会
    # 少重复计算很多。
    '''
    table:
        i  j 0 1 2 3 4 ......... aim
        0    1 1 1 1 1            1
        1    1
        2    1
        3    1
        4    1
        5    1
        .
        .
        .
        N-1  1
    '''
    # 当我们使用动态规划之后，整个时间复杂度由原来的64ms降低到35ms了，也就是说从O(N * AIM^2) 到 O(N * aim)
    def dpCounts(self, penny, index, aim, table):
        for i in range(1,len(penny)):
            for j in range(1,aim + 1):
                if j - penny[i] >= 0:
                    table[i][j] = table[i-1][j] + table[i][j-penny[i]]
                else:
                    table[i][j] = table[i-1][j]

        return table[len(penny) - 1][aim]


if __name__ == '__main__':
    penny = [3,6,8,10,12,15,18,21,22,23,25,28,31,34,35,37,40,41,44,47,50,51,52,53,54,57,59,61,62,64,66,68,69,72,73,75,76,77,80,82,85,86]
    n = 42
    aim = 39
    ex = Exchange()
    print(ex.countWays(penny,n,aim))
