import numpy as np
import function as f

y1 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]
y2 = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

print(f.mean_squared_error(np.array(y1), np.array(t)))
print(f.mean_squared_error(np.array(y2), np.array(t)))
