import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 使用numpy生成模擬數據
np.random.seed(123) # 確保結果在不同的運行中可重現
group_A = np.random.normal(300, 50, 1000) # A組（舊設計）的模擬數據
group_B = np.random.normal(320, 70, 1000) # B組（新設計）的模擬數據

# 整理數據
data = [group_A, group_B]
labels = ['A', 'B']

# 繪製箱形圖
plt.figure(figsize=[10,8])
sns.set(style='whitegrid')
sns.boxplot(data=data, width=0.5, palette='vlag')

# 添加標籤和標題
plt.ylabel('Time Spent on Page (Seconds)', fontsize=12)
plt.title('Time Spent on Page for Different Website Designs', fontsize=15)
plt.xlabel('Website Design', fontsize=12)
plt.xticks(np.arange(2), labels)

# 顯示圖形
plt.show()