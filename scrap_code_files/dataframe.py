import pandas as pd
import json

with open('match_summary.json') as f:
    data = json.load(f)

df = pd.DataFrame(data)

df.rename({'Scorecard':'match_id'}, axis=1, inplace= True)
pd.set_option('display.max_columns', None)

pd.reset_option('display.max_columns')
print(df)
df.to_csv('match_summary.csv', index=False)