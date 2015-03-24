class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        i=0
        j=0
        C=[]
        while i<len(A) and j<len(B):
            if A[i]>B[j]:
                C.append(B[j])
                j+=1
            else:
                C.append(A[i])
                i+=1
        while i<len(A):
            C.append(A[i])
            i+=1
        while j<len(B):
            C.append(B[j])
            j+=1
        if len(C)%2==1:
            return C[int(len(C)/2)]
        else:
            return (C[len(C)/2]+C[len(C)/2-1])/2.0
