import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns

# 使用 Seaborn 設置圖表樣式
sns.set(style='whitegrid')

# 假設我們有以下的廣告支出數據（以萬為單位）
ad_spend = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900]).reshape(-1, 1)

# 我們也有相應的銷售數據（以萬為單位）
sales = np.array([650, 790, 900, 1100, 1250, 1450, 1600, 1800, 2000])

# 我們將廣告支出數據用作特徵來預測銷售
model = LinearRegression()
model.fit(ad_spend, sales)

# 預測廣告花費為 $1,000,000 的銷售量
predicted_sales = model.predict([[1000]])
print('Predicted sales for an ad spend of $1,000,000: ', predicted_sales)

# 繪製圖表
plt.figure(figsize=(10,6))  # 設置圖表大小
plt.scatter(ad_spend, sales, color='orange')
plt.plot(ad_spend, model.predict(ad_spend), color='pink', linewidth=2)
plt.title('Ad Spend vs Sales', fontsize=16)  # 增加字體大小
plt.xlabel('Ad Spend', fontsize=14)  # 增加字體大小
plt.ylabel('Sales', fontsize=14)  # 增加字體大小
plt.xticks(fontsize=12)  # 調整 X 軸刻度的字體大小
plt.yticks(fontsize=12)  # 調整 Y 軸刻度的字體大小
plt.show()