#二乗和誤差
import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)     # np.array配列を引数に取る（ただのlistは×）

