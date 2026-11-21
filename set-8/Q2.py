'''class Solution:
    def searchMatrix(self,matrix,t):
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R):
            for j in range(C):
                if matrix[i][j]==t:
                    return [i,j]
        return [-1,-1]
'''
class Solution:
    def searchMatrix(self,matrix,t):
        R=len(matrix)
        C=len(matrix[0])
        lo=0
        hi=R*C-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            row=mid//C
            col=mid%C
            if matrix[row][col]==t:
                return [row,col]
            elif matrix[row][col]<t:
                lo=mid+1
            else:
                hi=mid-1
        return [-1,-1]