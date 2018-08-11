def reverse(expression):
    stack = []
    symbol = ''
    for c in expression:
        if len(stack) == 0 or stack[-1] in '+-*/':
            if symbol == '':
                symbol += c
            else:
                if c in '+-*/':
                    stack.append(symbol)
                    stack.append(c)
                    symbol = ''
                else:
                    symbol += c
        else:
            stack.append(c)


    stack.append(symbol)
    print(stack)
    reverse_expression = []
    while(len(stack)):
        reverse_expression.append(stack.pop())
    print(reverse_expression)
    return ''.join(reverse_expression)
def playlist(songs):
    num_pairs = 0
    max_value = -1
    table = [0 for i in range(1001)]
    for i in range(len(songs)):
        table[songs[i]] += 1
        if songs[i] > max_value:
            max_value = songs[i]
    max_times = 2 * max_value // 60
    for i in range(len(songs)):
        for j in range(1,max_times+1):
            another = j * 60 - songs[i]
            if another < 0 or another > 1000:
                continue
            else:
                if another == songs[i]:
                    if table[another] > 1:
                        num_pairs += (table[another] - 1)
                else:
                    if table[another] > 0:
                        num_pairs += table[another]
        table[songs[i]] -= 1
    return num_pairs

if __name__ == '__main__':
    print('hello')
    print(reverse('-1+-2*9-23'))
    print(playlist([30,20,150,100,40,60,70,80,100,1,1000]))
