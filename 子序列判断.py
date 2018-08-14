# written by Zachary WU
# question 4

# use a partial table to save the match information
def partial_match_table(pattern):
    table = [None] * len(pattern)
    table[0] = -1
    i = -1   # i is the prefix length
    j = 0
    while(j < len(pattern) - 1):
        if(i == -1 or pattern[i] == pattern[j]):
            i += 1
            j += 1
            table[j] = i
        else:
            i = table[i]
    return table

def is_subsequence(list_a, list_b):
    if len(list_a) > len(list_b):
        return False
    pmt = partial_match_table(list_a)
    i = 0
    j = 0
    while(i < len(list_b) and j < len(list_a)):
        if(j == -1 or list_b[i].find(list_a[j]) != -1):
            i += 1
            j += 15
        else:
            j = pmt[j]
    if j != len(list_a):
        return False
    else:
        return True

if __name__ == '__main__':
    list_a = ['a','b','c']
    list_b = ['ad','e','ac','de']
    print(is_subsequence(list_a,list_b))
