# written by HighW
# This is the source code for insertion sort
class InsertionSort:
    def insertionSort(self, A, n):
        for i in range(1,n):
            current = A[i]
            j = i-1
            while(j >= 0 and A[j] > current):
                A[j+1] = A[j]
                j -= 1
            A[j+1] = current
        return A

if __name__ == '__main__':
    sort = InsertionSort()
    A = [9,8,7,6,4,6,5,3,2,1]
    print(sort.insertionSort(A,10))
