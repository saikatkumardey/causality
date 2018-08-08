# causality
Package to perform Root-Cause Analysis on time series.

# Algorithms

+ Cross-Correlation [DONE]
+ Granger's Causality [TODO]
+ Information Transfer [TODO]

# How to run it?

Clone the repository and place it in your project. [ TODO: Create PYPI package ]

        git clone https://github.com/saikatkumardey/causality

# Usage

```python

from causality import correlator

ts1 = [1,8,3]
ts2 = [1,1,8,3]
cross_corr = correlator.CrossCorrelator(ts1=ts1,ts2=ts2)
cross_corr.correlate()
print("correlation ",cross_corr.get_correlation()) # maximum correlation
print("delay ",cross_corr.get_delay()) # detected delay


#plot all correlation values by time delays

import matplotlib
import matplotlib.pyplot as plt

def plot_cross_correlation(cross_corr_obj):
    c = cross_corr_obj.cross_corr_list
    x1,x2 = cross_corr_obj.ts1,cross_corr_obj.ts2
    lag = [len(x1)-i-1 for i in range(len(x1)+len(x2)-1)]
    plt.figure(figsize=(15,7))
    plt.plot(lag,c)
    plt.title("Cross-Correlation at different lags between the measure and driver")
    plt.xlabel("lags")
    plt.ylabel("cross-correlation")
    plt.tight_layout();

plot_cross_correlation(cross_corr)

```