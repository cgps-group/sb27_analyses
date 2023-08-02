import pickle
import pandas as pd
from sklearn.metrics import silhouette_score

# Open trained models file
file = open('range_trained_kmodes.pkl', 'rb')
# Dump information to that file
models = pickle.load(file)
# Close the file
file.close()



# Open subset file
file2 = open('subset.pkl', 'rb')
# Dump information to that file
data = pickle.load(file2)
# Close the file
file2.close()
df_data = data[data.columns[1:]]



# Open matching distances file
file3 = open('subset_mdm.pkl', 'rb')
# Dump information to that file
mdm = pickle.load(file3)
# Close the file
file3.close()


# Print to csv
#out_table = []
#out_table.append(list(data[0]))


print(data)


for k in models:
    results=models[k].predict(df_data)
    #print(results)
    #out_table.append(list(results))
    ss = silhouette_score(mdm, models[k].labels_,metric="precomputed")
    print(f'Silhouette Score(n='+str(k)+'): '+str(ss))


# Print to csv table
to_print = [*zip(*out_table)]
df = pd.DataFrame(to_print, columns =['accession', '2','3','4','5','6','7','8','9','10'])
df.to_csv("results.csv",index=False)
