from kmodes.kmodes import KModes
import pandas as pd
import numpy as np
import pickle
import sys


IN_DATAFRAME = sys.argv[1]
IN_TRAINED_MODEL =  sys.argv[2]

print(IN_DATAFRAME,IN_TRAINED_MODEL)

#IN_DATAFRAME = "subset.pkl"
#IN_TRAINED_MODEL =  'trained_kmodes.pkl'

# Load trainig dataset
df = pd.read_pickle(IN_DATAFRAME)

# Load file with pickle
file = open(IN_TRAINED_MODEL, 'rb')
km = pickle.load(file)
file.close()


# Split labels and data
df_data = df[df.columns[1:]]
ids = list(df[0])

test_data = df_data.to_numpy()

# Make sure data is all of the same type
t_data = []
for f in test_data:
    t_data.append( list(map(str, f)) )

test_data = np.array(t_data)





# Predict clusters for the test data
test_clusters = km.predict(test_data)


# Print the predicted clusters for the test data                                                                                                                     
for i, cluster in enumerate(test_clusters):
    print(f"{ids[i]},{cluster}")
