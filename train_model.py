
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv("sample_logs.csv")

X = data[['failed_logins','data_transfer_mb','unknown_process']]
y = data['threat']

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model, open("threat_model.pkl","wb"))

print("Model Trained")
