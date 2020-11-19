import numpy as np

x = np.zeros((360, 2, 3), dtype=np.float)
#x[:, 0, 1] = 1

for i in range(0,360):
    x[i, :, :] = -180 + i

print(x[:, :])

