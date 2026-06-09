

import pandas as pd

df = pd.read_parquet("train-00000-of-00001.parquet")

# 查看基本信息
print(df.shape)        # 行数和列数
print(df.columns)      # 列名
print(df.dtypes)       # 数据类型
print(df.head())       # 前5行数据