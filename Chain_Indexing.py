#Method Chaining vs. Chain Indexing

import pandas as pd

df = pd.read_csv('data_file.csv') #create DataFrame

#Chain Indexing
df = df[df['CARS']==50]
df.set_index(['NAME','BRAND'], inplace=True)
df.rename(columns={'NAME': 'CARTYPE'})

#Method Chaining
(df.where(df['CARS']==50)
    .dropna()
    .set_index(['NAME','BRAND'])
    .rename(columns={'NAME': 'CARTYPE'}))
