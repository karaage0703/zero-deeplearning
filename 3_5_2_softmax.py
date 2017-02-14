import numpy as np
import function as f

a = np.array([1010, 1000, 990])

print (f.softmax_ng(a))
print (f.softmax(a))

b = np.array([0.3, 2.9, 4.0])
print (f.softmax_ng(b))
print (f.softmax(b))


