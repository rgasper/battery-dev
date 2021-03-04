from scipy.signal import find_peaks
import pandas as pd
import yaml

with open("params.yaml") as yml:
    params = yaml.safe_load(yml)
    params = params["peak_finding"]
    # no params used yet
    prominence = params["prominence"]

smooth_data = pd.read_csv("data/smoothed.csv", index_col="timestamp")
peaks, properties = find_peaks(smooth_data.current)
peaks_df = pd.DataFrame(peaks, columns=["peak_indices"])
peaks_df["peak_timestamps"] = smooth_data.index[peaks]
peaks_df.to_csv("data/peaks.csv", index=False)
