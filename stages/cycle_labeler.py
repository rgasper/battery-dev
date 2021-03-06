from scipy.signal import find_peaks
import pandas as pd
import yaml

with open("params.yaml") as yml:
    params = yaml.safe_load(yml)
    params = params["cycle_labeling"]
    # no params used yet
    prominence = params["peak_prominence"]

smooth_data = pd.read_csv("data/smoothed.csv", index_col="timestamp")
raw_data = pd.read_csv("data/raw.csv", index_col="timestamp")
current_peaks, properties = find_peaks(smooth_data.current)

cycle_edges = current_peaks.tolist()
cycle_edges.append(len(raw_data.index) - 1)  # the last cycle just goes off to the end of the plot
raw_data["cycle"] = None
previous_peak_ind = 0
for cycle_number, peak_ind in enumerate(cycle_edges):
    start_timestamp = raw_data.index[previous_peak_ind]
    stop_timestamp = raw_data.index[peak_ind]
    previous_peak_ind = peak_ind
    raw_data.loc[start_timestamp:stop_timestamp, "cycle"] = cycle_number

raw_data.to_csv("data/raw_cycle_labeled.csv", index=False)
