import pandas as pd
from scipy.signal import savgol_filter
import yaml

with open("params.yaml") as yml:
    params = yaml.safe_load(yml)
    params = params["smoothing"]
    window = params["window"]
    polyorder = params["polyorder"]
    wrap_mode = params["wrap_mode"]

# load
data = pd.read_csv("data/concatenated_battery_profile.csv", index_col="timestamp")
# process
data["current"] = savgol_filter(data["current"], window, polyorder, mode=wrap_mode)
data["voltage"] = savgol_filter(data["voltage"], window, polyorder, mode=wrap_mode)
# store
data[["current", "voltage", "temperature"]].to_csv("data/smoothed.csv", index=True)
