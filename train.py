from sklearn.tree import DecisionTreeClassifier
import joblib
import numpy as np

X = np.array([[10], [20], [30], [60], [70], [80]]) #taining data
y = ["SMALL", "SMALL", "SMALL", "LARGE", "LARGE", "LARGE"]

model = DecisionTreeClassifier()  #model train
model.fit(X, y)

joblib.dump(model, "model.pkl")  #saves model

print("Model trained and saved")