import numpy as np
import pandas as pd

data = {
    'c0': [0, 1, 2, 3],
    'c1': [4, 5, 6, 7],
    'c2': 8,
    'c3': 9,
}
df = pd.DataFrame(data)
# data2 = {'c2': 2, 'c3': 3}
# df.assign(**data2)
# df[['c0']] = [3, 2, 1, 0]
# df[['c0', 'c1', 'c2']] = [[3, 2, 1, 0], [7, 8, 9, 10], 17]
# df[['c0', 'c1', 'c2']] = pd.Series([3, 2, 1, 0])
df['c0'] = pd.Series([3, 2, 1, 0])
print(df)
