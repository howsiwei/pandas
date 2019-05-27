import pandas as pd
df = pd.DataFrame({'a': [1, 2]})
import pdb
pdb.set_trace()
df['b'] = 1
df[['a', 'c']] = 1
