#these were all taken from here: https://github.com/rougier/numpy-100

#. Import the numpy package under the name ``np`` (★☆☆☆☆) 
import numpy as np

#. Print the numpy version and the configuration (★☆☆☆☆) 
#print (np.__version__)
#np.__config__.show()

#. Create a null vector of size 10 (★☆☆☆☆) 
#v = np.zeros(10)
#print v

#. How to get the documentation of the numpy add function from the command line ? (★☆☆☆☆) 

#. Create a null vector of size 10 but the fifth value which is 1 (★☆☆☆☆) 
#v = np.zeros(10)
#v[4]=1
#print v

#. Create a vector with values ranging from 10 to 49 (★☆☆☆☆) 
#v = np.arange(10,50)
#print v

#. Reverse a vector (first element becomes last) (★☆☆☆☆) 
#v = np.arange(11)
#v = v[::-1]
#print v

#. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆☆☆) 
#a = np.matrix('0 1 2; 3 4 5; 6 7 8')
#a = np.arange(9).reshape(3,3)
#print a

#. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆☆☆) 
v = np.array([1,2,0,0,4,0])
nz_id = np.nonzero(v)
print ("indices: ", nz_id)

#and the actual values
print ("values: ", v[nz_id])    # for this to work, v HAS to be a np.array, can't be simply v = [1,2,3,..]

#. Create a 3x3 identity matrix (★☆☆☆☆) 

#. Create a 3x3x3 array with random values (★☆☆☆☆) 

#. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆☆☆) 

#. Create a random vector of size 30 and find the mean value  (★☆☆☆☆) 

#. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★★☆☆☆) 

#. Create a 8x8 matrix and fill it with a checkerboard pattern (★★☆☆☆) 

#. Create a checkerboard 8x8 matrix using the tile function (★★☆☆☆) 

#. Normalize a 5x5 random matrix (★★☆☆☆) 

#. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★★☆☆☆) 

#. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆☆☆) 

#. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆☆☆) 

#. Create a random vector of size 10 and sort it  (★★☆☆☆) 

#. Consider two random array A anb B, check if they are equal  (★★☆☆☆) 

#. Make an array immutable (read-only) (★★☆☆☆) 

#. Consider a random 10x2 matrix representing cartesian coordinates, convert

#. Create random vector of size 10 and replace the maximum value by 0 (★★☆☆☆) 

#. Create a structured array with ``x`` and ``y`` coordinates covering the

#. Print the minimum and maximum representable value for each numpy scalar type (★★☆☆☆) 

#. Create a structured array representing a position (x,y) and a color (r,g,b) (★★☆☆☆)

#. Consider a random vector with shape (100,2) representing coordinates, find

#. Consider the following file::

#. Generate a generic 2D Gaussian-like array (★★☆☆☆) 

#. How to randomly place p elements in a 2D array ? (★★★☆☆)

#. Subtract the mean of each row of a matrix (★★★☆☆) 

#. How to I sort an array by the nth column ? (★★★☆☆) 

#. How to tell if a given 2D array has null columns ? (★★★☆☆) 

#. Find the nearest value from a given value in an array (★★★☆☆) 

#. Consider a generator function that generates 10 integers and use it to build an

#. Consider a given vector, how to add 1 to each element indexed by a second

#. How to accumulate elements of a vector (X) to an array (F) based on an index

#. Considering a (w,h,3) image of (dtype=ubyte), compute the number of unique

#. Considering a four dimensions array, how to get sum over the last two axis

#. Considering a one-dimensional vector D, how to compute means of subsets of D

#. How to get the diagonal of a dot product ? (★★★☆☆) 

#. Consider the vector [1, 2, 3, 4, 5], how to build a new vector with 3

#. Consider an array of dimension (5,5,3), how to mulitply it by an array with

#. How to swap two rows of an array ? (★★★☆☆) 

#. Consider a set of 10 triplets describing 10 triangles (with shared

#. Given an array C that is a bincount, how to produce an array A such that

#. How to compute averages using a sliding window over an array ? (★★★☆☆) 

#. Consider a one-dimensional array Z, build a two-dimensional array whose

#. How to negate a boolean, or to change the sign of a float inplace ? (★★★☆☆) 

#. Consider 2 sets of points P0,P1 describing lines (2d) and a point p, how to

#. Consider 2 sets of points P0,P1 describing lines (2d) and a set of points P,

#. Consider an arbitrary array, write a function that extract a subpart with a

#. Consider an array Z = [1,2,3,4,5,6,7,8,9,10,11,12,13,14], how to generate an

#. Compute a matrix rank (★★★☆☆)

#. Extract all the contiguous 3x3 blocks from a random 10x10 matrix (★★★☆☆) 

#. Create a 2D array subclass such that Z[i,j] == Z[j,i] (★★★☆☆) 

#. Consider a set of p matrices wich shape (n,n) and a set of p vectors with shape (n,1).

#. Consider a 16x16 array, how to get the block-sum (block size is 4x4) ? (★★★☆☆) 

#. How to implement the Game of Life using numpy arrays ? (★★★☆☆) 

#. Given an arbitrary number of vectors, build the cartesian product (every

#. How to create a record array from a regular array ? (★★★☆☆) 

#. Comsider a large vector Z, compute Z to the power of 3 using 3 different

#. Consider two arrays A and B of shape (8,3) and (2,2). How to find rows of A

#. Considering a 10x3 matrix, extract rows with unequal values (e.g. [2,2,3]) (★★★★☆) 

#. Convert a vector of ints into a matrix binary representation (★★★★☆) 

#. Given a two dimensional array, how to extract unique rows ? (★★★★☆) 

#. Considering 2 vectors A & B, write the einsum equivalent of inner, outer,

#. Considering a path described by two vectors (X,Y), how to sample it using