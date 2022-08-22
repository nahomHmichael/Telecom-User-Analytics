import pandas as pd

df = pd.read_csv('data/field_descriptions.csv')

print(df.head(5))
#x = df.to_csv('data/field_descriptions.csv', index=False)