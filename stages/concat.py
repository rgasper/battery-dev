import pandas as pd
import glob
import os

# NOTE must be run from repo root.

files = glob.glob("data/initial_features/*")
dfs = []
for file in sorted(files):
    dfs.append(pd.read_csv(file))
all_df = pd.concat(dfs)
all_df.to_csv("data/concatenated_battery_profile.csv")
