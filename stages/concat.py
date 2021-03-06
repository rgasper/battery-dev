import pandas as pd
import glob
import yaml
import logging

# NOTE must be run from repo root.

with open("params.yaml") as yml:
    params = yaml.safe_load(yml)

files = glob.glob("data/initial_features/*")
dfs = []
for file in sorted(files):
    df = pd.read_csv(file)
    dfs.append(df)
all_df = pd.concat(dfs)
all_df = all_df.set_index("timestamp")
all_df = all_df.sort_index()
if params["development"]:
    logging.info("set to development mode, only using 1\% of the dataset")
    min = all_df.index.min()
    one_percent = int(len(all_df) / 100)
    one_percent = all_df.index[one_percent]
    all_df = all_df.loc[0:one_percent, :]
all_df.to_csv("data/raw.csv", index=True)
