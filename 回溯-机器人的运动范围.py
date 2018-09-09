'''
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
'''
'''
0 1 2 3
4 5 6 7
8 9 10 11
'''
'''
python使用的机制叫做call by object, 也就是call by object reference, 当object是immutable(integer, string, tuple)的时候，使用的机制叫做call by value，
如果object是mutable(list, dict)的时候，使用的机制叫做call by reference.本题中需要尤其注意递归函数的num其实是call by value，所以不能在函数里进行更改。
'''
class Solutions:
    def movingCount(self, threshold,rows,cols):
        start = (0,0)
        if 0 > threshold:
            return 0
        num = 1
        track = {start:1}
        num = self.track(threshold, start,rows, cols, num, track)
        return num
    def track(self, threshold, start, rows, cols, num, track):
        for next in [(start[0] + 1, start[1]), (start[0] - 1, start[1]), (start[0],start[1] + 1), (start[0],start[1] - 1)]:
            if next[0] < rows and next[0] >= 0 and next[1] < cols and next[1] >= 0 and next not in track:
                track[next] = 1
                digit_list = list(str(next[0]) + str(next[1]))
                sumDigits = 0
                for digit in digit_list:
                    sumDigits += int(digit)
                if sumDigits <= threshold:
                    num += 1
                    num = self.track(threshold, next, rows, cols, num ,track)
        return num
if __name__ == '__main__':
    s = Solutions()
    print(s.movingCount(18,4,5))
