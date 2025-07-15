from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

# Load data
data = pd.read_csv("../data-prep/cleaned_data.csv")
X = data[['NH3_ratio', 'H2_ratio', 'RPM']]
y = data['NOx_emission']

# Split & scale
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)

# Train GP
gp = GaussianProcessRegressor()
gp.fit(X_train_scaled, y_train)

# Save model
joblib.dump(gp, "models/gp_model.pkl")

