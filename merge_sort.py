# written by HighW
# This is the source code for merge sort
class MergeSort():
    def mergeSort(self, A, n):
        self.split_merge(A,0,n-1)
        return A

    def split_merge(self,A,start, end):
        if start == end:
            return
        else:
            middle = (start + end ) // 2
            self.split_merge(A,start, middle)
            self.split_merge(A,middle+1, end)
            sorted = []
            i,j = start,middle+1
            while(i <= middle and j<= end ):
                if(A[i] < A[j]):
                    sorted.append(A[i])
                    i += 1
                else:
                    sorted.append(A[j])
                    j += 1
            while(i <= middle):
                sorted.append(A[i])
                i += 1
            while(j <= end):
                sorted.append(A[j])
                j += 1
            for i in range(len(sorted)):
                A[i + start] = sorted[i]
if __name__ == '__main__':
    sort = MergeSort()
    A = [9,8,7,6,6,5,4,3,2,1]
    print(sort.mergeSort(A,10))
