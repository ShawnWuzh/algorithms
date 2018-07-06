# written by HighW
# This is the source code for quick sort
class QuickSort():
    def quickSort(self, A, n):
        self.pivot_split(A,0, n-1)
        return A
    def pivot_split(self, A, start, end):
        if start > end:
            return
        else:
            pivot_loc = start
            for i in range(start+1, end+1):
                if A[i] < A[pivot_loc]:
                    j = i - 1
                    temp = A[i]
                    while(j >= pivot_loc):
                        A[j+1] = A[j]
                        j -= 1
                    A[j + 1] = temp
                    pivot_loc += 1
            self.pivot_split(A, start, pivot_loc-1)
            self.pivot_split(A, pivot_loc + 1, end)
if __name__ == '__main__':
    sort = QuickSort()
    A = [9,8,7,6,5,4,3,2,1]
    print(sort.quickSort(A,9))
