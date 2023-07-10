from kmodes.kmodes import KModes

import pickle
import pandas as pd
import numpy as np

# Load trainig dataset
df = pd.read_pickle("subset.pkl")


# Split labels and data
df_data = df[df.columns[1:]]
ids = list(df[0])

training_data = df_data.to_numpy()


# Make sure data is all of the same type
t_data = []
for f in training_data:
    t_data.append( list(map(str, f)) )

training_data = np.array(t_data)


# Initialize k-modes model
k = 10  # Number of clusters
km = KModes(n_clusters=k, n_init=5, verbose=1)


# Train the model
clusters = km.fit(training_data)


# Save trained model into pickle
with open('trained_kmodes.pkl', 'wb') as handle:
    pickle.dump(clusters, handle, protocol=pickle.HIGHEST_PROTOCOL)
