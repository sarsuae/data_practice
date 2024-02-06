import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter

# 假設我們有1000位用戶
N = 1000

# 我們隨機生成每位用戶使用軟體的時間（以天為單位）
np.random.seed(123)
user_time = np.random.exponential(scale=90, size=N)
user_time = np.round(user_time).astype(int)

#考慮到一些用戶可能仍在使用該軟體，所以他們的生存時間會被右設限 (即，我們只知道他們使用此軟體至少有多長時間)
observed = (np.random.rand(N) < 0.5)

# 創建一個 DataFrame 來儲存數據
data = pd.DataFrame({'user_time': user_time, 'observed': observed})

# 建立和訓練 Kaplan-Meier Model
kmf = KaplanMeierFitter()
kmf.fit(data['user_time'], event_observed=data['observed'])

# 劃出結果
kmf.plot_survival_function()
plt.title('Survival function of user churn')
plt.xlabel('Days')
plt.ylabel('Surviving fraction of users')
plt.grid(True)
plt.show()