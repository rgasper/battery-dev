from os import mkdir
import pandas as pd
import glob
import yaml
from sklearn.preprocessing import MaxAbsScaler
from joblib import dump

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

# have to reshape column as it is a single feature
current_normalizer = MaxAbsScaler().fit(all_df["current"].values.reshape(-1, 1))
voltage_normalizer = MaxAbsScaler().fit(all_df["voltage"].values.reshape(-1, 1))
temperature_normalizer = MaxAbsScaler().fit(all_df["temperature"].values.reshape(-1, 1))

if params["development"]:
    print("set to development mode, only using 1\% of the dataset")
    min = all_df.index.min()
    one_percent = int(len(all_df) / 100)
    one_percent = all_df.index[one_percent]
    all_df = all_df.loc[0:one_percent, :]

all_df["current"] = current_normalizer.transform(all_df["current"].values.reshape(-1, 1))
all_df["voltage"] = voltage_normalizer.transform(all_df["voltage"].values.reshape(-1, 1))
all_df["temperature"] = temperature_normalizer.transform(all_df["temperature"].values.reshape(-1, 1))

# save outputs
all_df.to_csv("data/raw.csv", index=True)

try:
    mkdir("models/preprocessors")
except OSError:
    pass
dump(current_normalizer, "models/preprocessors/current_normalizer.pkl")
dump(voltage_normalizer, "models/preprocessors/voltage_normalizer.pkl")
dump(temperature_normalizer, "models/preprocessors/temperature_normalizer.pkl")
