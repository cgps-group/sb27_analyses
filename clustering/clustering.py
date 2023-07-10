from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

df = pd.read_pickle("subset.pkl")

df_data = df[df.columns[1:]]
ids = list(df[0])


for c in df_data:
    print("before", df_data[c].dtypes)

    df_data[c] = df_data[c].astype('int64')

    print("after", df_data[c].dtypes)


data = df_data.to_numpy()
print(df_data)
kmeans = KMeans(n_clusters=10, random_state=0, n_init="auto").fit(data)


print(df_data)
