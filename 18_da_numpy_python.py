!pip install numpy

import numpy as np
numpy.__version__

"""### Array Initialization - Single Dimension"""

import numpy as np
a = np.array([7,9,9,2])
print(a)

"""### Array Initialization - Multi Dimension"""

import numpy as np
b = np.array([(7,9,9,2),(16,11,9,6)])
print(b)

"""###Generating Array

"""

c = np.arange(10) #range of values in array
d = np.linspace(1,5,10) #set of values by Interval [start,end,no.ofvaluesEqualInterval]
print(c)
print(d)

"""### Array Properties"""

a = np.array([7,9,9,2])
b = np.array([(7,9,9,2),(16,11,9,6)])
print(b.ndim) #Dimension of Array
print(a.itemsize) #Byte Size of each Element
print(a.dtype) #Datatype of array
print(b.size*b.itemsize) #memory occupied - space occupied by 1 element * length of numpy array
print(a.size) #number of elements in array
print(b.shape) #shape of array (rows and columns)

"""### Array Reshape"""

b = np.array([(7,9,9,2),(16,11,9,6)])
print(b)
b = b.reshape(4,2)
print(b)

"""### Array Slicing"""

b = np.array([(7,9,9,2),(16,11,9,6)])
print(b[0,2]) #Slicing the Element from certain row and certain column b[rowIndex,ColumnIndex]
print(b[0:,2]) #Slicing Element from all rows and certain column

"""### Array Value Operation"""

e = np.array([7,9,9,2,16,11,96]) 
print(e.min()) #Minimum value in array
print(e.max()) #Maximum value in array
print(e.sum()) #Sum of array

"""###Array Arithmetic Operation

"""

a = np.array([7,9,9,2])
c = np.array([1,9,9,6])
print(a+c)
print(a-c)
print(a*c)
print(a/c)

a = np.array([7,9,9,2])
b = np.array([(7,9,9,2),(16,11,9,6)])
print(b.sum(axis=0)) #Each element of 1st dim array with same index with another dim element
print(b.sum(axis=1)) #sum of all element is 1st dim & sum of all element is 2nd dim
print(np.sqrt(a)) #Squareroot of array elements
print(np.std(a)) #Standard Deviation of array
print(np.exp(a)) #Exponential of array
print(np.log(a)) #Natural Log - ln
print(np.log10(a)) #Log base 10

b = np.array([(7,9,9,2),(16,11,9,6)])
f = np.array([(1,2,3,4),(5,6,7,8)])
print(np.vstack((b,f))) #Vertical Stack
print(np.hstack((b,f))) #Horizontal Stack
print(b.ravel()) #Merging as single
