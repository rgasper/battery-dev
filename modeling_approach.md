##Some definitions:
SOH: State-of-health, the metric we are trying to predict. Here, SOH corresponds to the amount of charge we can get out of the battery from a standardized test. Usually, a 2 or 3 hour discharge, but it doesn't really matter - the point is that these SOH measurements are common in the lab, but essentially never happen in real-world use.
Load: the demand on the battery, i.e., the current signal
Response: the performance of the battery at a given load, i.e., the voltage signal
- At a given load (current), the voltage of the battery will change during lifetime. As the battery ages, the performance can get better or worse, depending on what's changing inside the battery. 
#Data:
X: Timeseries data of temperature, current, and voltage
- Real-world use, i.e., non-constant current load, partial charge/discharges
Y: 4 accurate capacity measurements (SOH metric)
#Goal:
Use the timeseries data to predict capacity at 4 later dates.
#Challenge / Approach:
##Training:
- The x-data is composed of many distinct patterns: the battery is being cycled between different voltages using different loads, so it's hard to extract simple features, because simple features would be both a function of SOH and how the battery was being used at that time
	- Solution: Identify load 'motifs', use the voltage response during each 'motif' as input to predict SOH
		- Signal detection algorithm? Ideally, unsupervised (find motifs without us telling it how many motifs to find, expected timeframe, …)
			- Motifs could overlap! E.g., there could be some bigger patterns that are compositions of small patterns.
		- Finding motifs discretizes the timeseries from millions of data points to a few thousand motif periods
		- The I-V-T-t data from a motif will either be directly input into a SOH model, or…
		- Some kind of feature extraction will occur during each motif
			- Feature extraction will hopefully help to regularize, so that the algorithm works well when used on different future loads
		- Each motif will probably have its own SOH model
		- Assumption with this approach: the variation of the battery load during lab testing reflects the variation of battery load during real-world operation. Some form of feature extraction is likely crucial to account for differences between the trained battery load and real-world battery loads.
	- Limited Y-data: there's only 4 'true' SOH measurements to train on, compared with ~10 million timeseries data points
		- Solution: Use a simple polynomial / power law function of time (pick the best model based on BIC or other fit metrics) to interpolate 'synthetic' SOH values between true SOH values
			- Interpolate values at the end timestamp of each motif, to give each motif a 'true' SOH value to train the SOH prediction algorithm
#Inference:
- Grab the last 3-6 hours of the battery use
- Separate the previous 3-6 hours into known motifs
	- Even if the signal isn't the exact same as known motifs, I think a signal detection algorithm should be able to point us to regions of the signal, like 'this part is most like motif A', etc…
- Predict SOH for each identified motif
- Inferred SOH is simply the average of all the predicted SOHs from the various motifs.
#Details:
- Use clustering algorithm to find similarity between different dynamic use periods
	- Time-based window doesn't seem appropriate
	- More likely, it is possible to identify use 'motif periods' based on the dynamic load (the current demanded from the battery)
		- Time frame of motifs looks like 1 hour, with maybe some variation, but they look pretty darn close to exactly 1 hour, but those hours may be a composition of several shorter patterns
		- Every once and a while a 3 hour motif shows up, which is obviously distinct from any other 1 hour motif
	- Looking at the data, the charges are fairly distinct, even if they don't start/end at the same voltages
		- Voltage increases significantly (more than the RMS of the discharge behavior)
		- Some of the charging protocols have a decreasing current potion that might be easy to find
