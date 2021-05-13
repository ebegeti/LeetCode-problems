#Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

from chapter1_arrays_strings import AssortedMethods


def rotate(matrix,N):
     for layer in range(0,int(N/2)):
         first=layer
         last=N-1-layer
         for i in range(first,last):
             offset=i-first
             top=matrix[first][i]
             matrix[first][i]=matrix[last-offset][first]
             matrix[last-offset][first] = matrix[last][last - offset]
             matrix[last][last - offset] = matrix[i][last]
             matrix[i][last] = top
     return matrix
             
             

# driver code
if __name__ == "__main__":
    matrix=AssortedMethods.AssortedMethods()
    matrix=matrix.setRandomMatrix(10,10,10)
    print(matrix,'\n\n')
    print(rotate(matrix,10))
