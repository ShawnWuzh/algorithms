'''
This is the source code for Knuth-Morris-Pratt algorithm for string match
Written by HighW
'''
class KMP():
    def __init__(self):
        self.text = None
        self.pattern = None

    def search_pattern(self,text, pattern):
        self.text = text
        self.pattern = pattern
        pmt = self.partial_match_table(self.pattern)
        i = 0
        j = 0
        while(i < len(text) and j < len(pattern)):
            if(j == -1 or text[i] == pattern[j]):
                i += 1
                j += 1
            else:
                j = pmt[j]
        if j != len(pattern):
            return -1
        else:
            return i - j

    def partial_match_table(self,pattern):
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
if __name__ == '__main__':
    kmp = KMP()
    pattern = 'AAABBBAAACC'
    text = 'AAAcccBBBAAADDAADDAAABBBAAACC'
    print(kmp.search_pattern(text,pattern))
