from numpy import array
from numpy.linalg import inv
A = array([[1.0,2.0],[3.0,4.0]])
print(A)
B = inv(A)
print(B)
I = A.dot(B)
print(I)