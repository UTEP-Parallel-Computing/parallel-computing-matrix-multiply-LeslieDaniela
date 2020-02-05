# Program multiplies two 10x10 matrices using nested loops

# Times matrix calculations
import timeit
start = timeit.default_timer()

# 10 x 10 matrix
A = [[7, 10, 12, 7, 3, 5, 10, 28, 9, 6],
     [2, 42, 6, 8, 1, 2, 13, 4, 5, 6],
     [7, 8, 9, 14, 5, 21, 64, 1, 9, 2],
     [4, 7, 2, 9, 14, 33, 9, 0, 13, 5],
     [32, 8, 3, 1, 31, 4, 7, 0, 65, 1],
     [7, 10, 12, 7, 3, 5, 10, 28, 9, 6],
     [2, 42, 6, 8, 1, 2, 13, 4, 5, 6],
     [7, 8, 9, 14, 5, 21, 64, 1, 9, 2],
     [4, 7, 2, 9, 14, 33, 9, 0, 13, 5],
     [32, 8, 3, 1, 31, 4, 7, 0, 65, 1]]

# 10 x 10 matrix
B = [[7, 10, 12, 7, 3, 5, 10, 28, 9, 6],
     [2, 42, 6, 8, 1, 2, 13, 4, 5, 6],
     [7, 8, 9, 14, 5, 21, 6, 1, 9, 2],
     [4, 7, 2, 9, 14, 6, 9, 0, 13, 5],
     [32, 8, 3, 13, 1, 4, 7, 0, 65, 1],
     [7, 10, 12, 7, 3, 5, 10, 8, 9, 6],
     [2, 42, 6, 8, 1, 2, 13, 4, 5, 6],
     [7, 8, 9, 1, 5, 21, 64, 1, 9, 2],
     [4, 7, 2, 9, 14, 33, 9, 5, 13, 5],
     [15, 8, 3, 1, 31, 4, 7, 12, 6, 1]]

# product holds 10x10 matrix result
product = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# for loop iterates through rows of matrix A
for i in range(len(A)):

   # for loop iterates through columns of matrix B
   for j in range(len(B[0])):

       # for loop iterates through rows of matrix B
       for k in range(len(B)):

           # Matrix Multiplication
           product[i][j] += A[i][k] * B[k][j]

# Prints AxB matrix product
for p in product:
   print(p)

# Calculates run time of matrix multiplication
   stop = timeit.default_timer()
   print('Time: ', stop - start)