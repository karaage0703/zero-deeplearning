import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D

def numerical_diff(f, x):
    h = 1e-4 # 0.0001
    return (f(x+h) - f(x-h)) / (2*h)

def function_2(x):
    return x[0]**2 + x[1]**2

def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

x = [0,0]
X = [0,0]
x[0] = np.arange(-3.0, 3.0, 0.1)
x[1] = np.arange(-3.0, 3.0, 0.1)
X[0], X[1] = np.meshgrid(x[0], x[1])
Z = function_2(X)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(X[0],X[1],Z)
plt.show()

print(numerical_diff(function_tmp1, 3.0))
print(numerical_diff(function_tmp2, 4.0))
