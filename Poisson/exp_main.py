import numpy as np
import math

credit_spread = 0.1
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
    uni_var = np.random.uniform(0,1,path)
    exp_var = [-math.log(1-uv) for uv in uni_var]
    default_path = np.zeros(path, int)

    for i in range(path):
        ruin = False
        accum_haz = 0.0
        for j in range(len(dt)):
            accum_haz += prob_def[j]
            if accum_haz >= exp_var[i]:
                ruin = True
                default_matrix[i, j] = 1
                default_path[i] = 1

    theo_default = 1-math.exp(-credit_spread/(1-RecovRate)*T)
    mc_default = sum(default_path)/path
    print(f'theo = {theo_default},  mc = {mc_default}, %diff = {(mc_default/theo_default-1)*100}%\n')
print('End')