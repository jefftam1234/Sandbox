import numpy as np
import math

credit_spread = 0.05
T = 4.1
RecovRate = 0.4
path = 500000

iter = 10

timeGrid = np.arange(start=0, stop=T+0.05, step=0.05)
dt = []
for i in range(len(timeGrid)-1):
    dt.append(timeGrid[i+1] - timeGrid[i])

prob_def = [1-math.exp(-credit_spread/(1-RecovRate) * i) for i in dt]

for n in range(iter):
    default_matrix = np.zeros((path, len(dt)), int)
    uni_var = np.random.uniform(0,1,path*len(dt))
    default_path = np.zeros(path, int)

    for i in range(path):
        ruin = False
        for j in range(len(dt)):
            if ruin:
                continue
            else:
                nIndex = i * len(dt) + j
                if uni_var[nIndex] < prob_def[j]:
                    default_matrix[i, j] = 1
                    default_path[i] = 1

    theo_default = 1-math.exp(-credit_spread/(1-RecovRate)*T)
    mc_default = sum(default_path)/path
    print(f'theo = {theo_default},  mc = {mc_default}, %diff = {(mc_default/theo_default-1)*100}%\n')
print('End')