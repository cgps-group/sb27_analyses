# This set of scripts used Kmodes to cluster E. coli data

This requires to run `data_prep.py` in the `clustering` directory

* `subset_kmodes.py` Creates subset of entire ENA E. coli dataset in an accepted `Kmodes` format  

* `subset.pkl` Output of `subset_kmodes.py`

* `clustering.py` Trains Kmodes model

* `trained_kmodes.pkl` Trained model saved as pickle

* `predicting.py` Predicts cluster membership given cgmlst profile (downloaded from PathogenWatch)

