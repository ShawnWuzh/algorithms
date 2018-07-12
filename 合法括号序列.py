'''
对于一个字符串，请设计一个算法，判断其是否为一个合法的括号串。

给定一个字符串A和它的长度n，请返回一个bool值代表它是否为一个合法的括号串。

测试样例：
"(()())",6
返回：true
测试样例：
"()a()()",7
返回：false
测试样例：
"()(()()",7
返回：false

'''
# written by HighW
class Parenthesis:
    def chkParenthesis(self, A, n):
        num_brakets = 0
        for i in range(n):
            if A[i] == '(':
                num_brakets += 1
            elif A[i] == ')':
                num_brakets -= 1
            if num_brakets < 0:
                return False
        if num_brakets > 0:
            return False
        return True
if __name__ == "__main__":
    p = Parenthesis()
    A = "(()())"
    print(p.chkParenthesis(A,6))
