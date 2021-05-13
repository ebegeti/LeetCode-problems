#Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column is set to 0.

from chapter1_arrays_strings import AssortedMethods


def setZeros(matrix):
    rows=[0 for i in range(0,len(matrix))]
    cols=[0 for i in range(0,len(matrix[0]))]
    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[0])):
            if matrix[row][col]==0:
                rows[row]=1
                cols[col]=1


    for row in range(0,len(matrix)):
        for col in range(0,len(matrix[0])):
            if (rows[row]==1 or cols[col]==1):
                matrix[row][col]=0
    return matrix



# driver code
if __name__ == "__main__":
    matrix=AssortedMethods.AssortedMethods()
    matrix=matrix.setRandomMatrix(10,4,5)
    print(matrix,'\n\n')
    print(setZeros(matrix))
