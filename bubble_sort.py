# written by HighW
# This is the source code fo bubble sort

class BubbleSort():
    def bubbleSort(self, A, n):
        flag = 0 # use this flag to indicate if there is element change
        while(n):
            for i in range(n-1):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                    flag = 1
            n -= 1
            if flag == 0:
                break
            flag = 0
        return A

if __name__ == '__main__':
    sort = BubbleSort()
    A = [9,8,7,6,4,6,5,3,2,1]
    print(sort.bubbleSort(A,10))
