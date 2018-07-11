# wwritten by HighW
# This is the source code for selection sort
class SelectionSort:
    def selectionSort(self,A,n):
        for i in range(n):
            min_loc = i
            for j in range(i,n):
                if A[j] < A[min_loc]:
                    min_loc = j
            A[i], A[min_loc] = A[min_loc], A[i]
        return A

if __name__ == "__main__":
    sort = SelectionSort()
    A = [9,8,7,6,5,4,3,2,1]
    n = 9
    print(sort.selectionSort(A,9))
