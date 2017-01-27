import numpy as np

B = np.array([[1,2], [3,4], [5,6]])
print(B)
print(np.ndim(B))
print(B.shape)
print(B.shape[0])

C = np.array([[1,2,3],[4,5,6]])
print(np.dot(C, B))

D = np.array([7,8])
print(np.dot(B, D))

