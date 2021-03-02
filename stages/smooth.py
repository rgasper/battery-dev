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
data["smoothed_current"] = savgol_filter(data["current"], window, polyorder, mode=wrap_mode)
data["smoothed_voltage"] = savgol_filter(data["voltage"], window, polyorder, mode=wrap_mode)
# store
data["smoothed_current"].to_csv("data/current.csv", index=True)
data["smoothed_voltage"].to_csv("data/voltage.csv", index=True)
data["temperature"].to_csv("data/temperature.csv", index=True)
