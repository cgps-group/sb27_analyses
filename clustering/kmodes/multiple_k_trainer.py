import pickle
import pandas as pd
import numpy as np
from kmodes.kmodes import KModes

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



# Trained models with k=2..10
trained_ks = dict()
for k in range(2,11):
    # Initialize k-modes model
    km = KModes(n_clusters=k, n_init=5, verbose=1)

    # Train the model
    clusters = km.fit(training_data)

    trained_ks[k] = clusters


# Save trained model into pickle
with open('range_trained_kmodes.pkl', 'wb') as handle:
    pickle.dump(trained_ks, handle, protocol=pickle.HIGHEST_PROTOCOL)


