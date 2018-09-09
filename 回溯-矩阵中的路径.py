'''
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。本题需要注意的点是，matrix是一个字符串而不是一个矩阵，
一定要注意输入的格式。
'''
'''
本题考查的就是回溯法，回溯法简单概括起来就是不满足条件的时候，就回退。基本步骤就是：对于满足条件的每一步，将该步加入到结果集中，然后对
该步的下面的每一可能步进行检查，如果不满足条件，回退，然后检查其他可能步，如果所有的可能步都不满足条件，说明加入结果集的该步不满足条件，
需要从结果集中把该步删除掉。
'''
'''
a b c e
s f c s
a d e e
'''
'''
ABCE
SFCS
ADEE

ABCCED
'''
class Solutions:
    def hasPath(self, matrix, rows, cols, path):
        starts = []
        for i in range(rows):
            for j in range(cols):
                if matrix[cols * i + j] == path[0]:
                    starts.append((i,j))
        if len(path) == 1 and len(starts):
            return True
        if len(path) == 1 and len(starts) == 0:
            return False
        else:
            path_dict = {}
            for start in starts:
                path_dict[start] = 1
                if self.checkPath(start,matrix,rows,cols,path,1,path_dict):
                    return True
            return False

    def checkPath(self, start, matrix, rows, cols, path, curIndex,path_dict):
        if curIndex == len(path):
            return True
        for next in [(start[0]-1,start[1]),(start[0]+1,start[1]),(start[0],start[1]+1),(start[0],start[1]-1)]:
            if next[0] >= 0 and next[0] < rows and next[1] >= 0 and next[1] < cols:
                if next not in path_dict:
                    if matrix[cols * next[0] + next[1]] == path[curIndex]:
                        path_dict[next] = 1
                        if self.checkPath(next, matrix,rows,cols,path,curIndex+1,path_dict):
                            return True
        del path_dict[start]
        return False

if __name__ == '__main__':
    s = Solutions()
    matrix = 'ABCESFCSADEE'
    path = 'ABCCED'
    print(s.hasPath(matrix,3,4,path))
