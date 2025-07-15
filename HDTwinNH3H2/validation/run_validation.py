import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

model = joblib.load("../surrogate-model/models/gp_model.pkl")
test_data = pd.read_csv("test_cases/nh3h2_blends.csv")
X_test = test_data[['NH3_ratio', 'H2_ratio', 'RPM']]

scaler = StandardScaler().fit(X_test)
X_scaled = scaler.transform(X_test)

predictions = model.predict(X_scaled)
print(predictions)
