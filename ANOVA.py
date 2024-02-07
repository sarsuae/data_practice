import pandas as pd
from scipy import stats

# 滿意度評分資料
feedback = {
  'A': [7, 8, 7, 6, 7],
  'B': [6, 7, 7, 6, 6],
  'C': [8, 8, 9, 8, 7]
}

# 使用Pandas製作 DataFrame
feedback_df = pd.DataFrame(feedback)

# 使用Scipy的 f_oneway 函式進行ANOVA分析
f_value, p_value = stats.f_oneway(feedback_df['A'], feedback_df['B'], feedback_df['C'])

print(f'ANOVA結果：F值 = {f_value}，p值 = {p_value}')