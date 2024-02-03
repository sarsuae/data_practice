import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf

# Simulate hourly power demand data for a week
np.random.seed(0)
power_demand = np.random.randn(24*7) * 100 + 1000
power_demand = pd.Series(power_demand)

fig, (ax1, ax2) = plt.subplots(2, 1)

# Plot hourly power demand
# ax1.plot(power_demand)
ax1.plot(power_demand, color='orange', linewidth=2)
ax1.set_title('Hourly Power Demand')
ax1.set_xlabel('Hour')
ax1.set_ylabel('Power Demand (kW)')

# Plot autocorrelation
mpl.rcParams['lines.color'] = 'orange'
plot_acf(power_demand, color='orange', ax=ax2)
ax2.set_title('Autocorrelation of Hourly Power Demand')
ax2.set_xlabel('Lag(Hour)')  # x label for acf plot, modified to 'Hour'
ax2.set_ylabel('Autocorrelation')  # y label for acf plot


plt.tight_layout()
plt.show()