

# Predict clusters for the test data                                                                                                                                 test_clusters = km.predict(test_data)

# Print the predicted clusters for the test data                                                                                                                     
for i, cluster in enumerate(test_clusters):
    print(f"Test data {i+1} belongs to cluster {cluster+1}")
