# DEPRECATED - This was just a little experiment

import pandas as pd
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
import pickle

df_y = pd.read_csv("data/target.csv")
df_y["t_days"] = (df_y.timestamp - df_y.timestamp[0]) / (24 * 3600)
df_y["y"] = np.abs(df_y.Q_discharge)

# Define function for calculating a power law, and an error function
capacityFadeModel = lambda q0, t, amp, power: q0 - (amp * t) ** power


def error(p, x, y):
    y0 = y[0]
    yPred = capacityFadeModel(y0, x, p[0], p[1])
    return y - yPred


params, _ = optimize.leastsq(error, [1, 1], args=(df_y.t_days.values, df_y.y.values))

with open("models/params.txt", "w") as file:
    file.write(",".join(str(p) for p in params))
