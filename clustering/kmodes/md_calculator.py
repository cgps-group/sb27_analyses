import pickle
from kmodes.kmodes import KModes
from kmodes import kprototypes
from sklearn.metrics import silhouette_score
import pandas as pd
import numpy as np

def create_dm(dataset):
    '''
    Code modified from https://codinginfinite.com/silhouette-coefficient-for-k-modes-and-k-prototypes-clustering/#:~:text=The%20average%20silhouette%20score%20for%20a%20given%20dataset%20lies%20between,dataset%20is%20closer%20to%201.
    '''
    if type(dataset).__name__=='DataFrame':
        dataset=dataset.values    
    lenDataset=len(dataset)
    distance_matrix=np.zeros(lenDataset*lenDataset).reshape(lenDataset,lenDataset)
    for i in range(lenDataset):
        for j in range(lenDataset):
            x1= dataset[i].reshape(1,-1)
            x2= dataset[j].reshape(1,-1)
            distance=kprototypes.matching_dissim(x1, x2)
            distance_matrix[i][j]=distance
            distance_matrix[j][i]=distance
    return distance_matrix


#data=pd.read_csv("KModes-dataset.csv", index_col=["Student"])
#print(data)
#distance_matrix=create_dm(data)
#print(distance_matrix)



# Open a file, where you stored the pickled data
file = open('subset.pkl', 'rb')
# Dump information to that file
data = pickle.load(file)
# Close the file
file.close()
# Modify dataframe
data = data[data.columns[1:]]

# Calculate Matching Dissimilarity Matrix using matching_dissim function
distance_matrix=create_dm(data)
with open('subset_mdm.pkl', 'wb') as f:
    pickle.dump(distance_matrix, f)

print(distance_matrix)
