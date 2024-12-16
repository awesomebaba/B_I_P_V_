from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Example feature set (simplified for illustration)
# Features: Latitude, Longitude, GHI, DNI, Shading coefficients for each side
# Target: Energy output for each side (North, South, East, West)

# Sample Data (simplified)
data = {
    "Latitude": [28.6, 23.0, 30.0, 22.5],
    "Longitude": [77.2, 72.6, 77.2, 80.0],
    "GHI": [5.8, 6.2, 5.7, 6.0],
    "DNI": [6.5, 7.0, 6.5, 6.8],
    "Shading_North": [0.5, 0.6, 0.4, 0.5],
    "Shading_South": [0.8, 0.7, 0.9, 0.8],
    "Shading_East": [0.7, 0.6, 0.5, 0.7],
    "Shading_West": [0.6, 0.5, 0.6, 0.5],
    "Energy_Output_North": [18.85, 20.5, 19.2, 18.0],
    "Energy_Output_South": [30.24, 33.5, 32.0, 31.0],
    "Energy_Output_East": [26.46, 28.5, 27.0, 26.5],
    "Energy_Output_West": [22.68, 25.0, 23.0, 24.0]
}

# Convert the data into a pandas DataFrame
import pandas as pd
df = pd.DataFrame(data)

# Features (Latitude, Longitude, GHI, DNI, Shading coefficients)
X = df[["Latitude", "Longitude", "GHI", "DNI", "Shading_North", "Shading_South", "Shading_East", "Shading_West"]]

# Target (Energy Output for each side)
y = df[["Energy_Output_North", "Energy_Output_South", "Energy_Output_East", "Energy_Output_West"]]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Predict for new building data
new_building = pd.DataFrame({
    "Latitude": [23.0225],
    "Longitude": [72.5714],
    "GHI": [5.8],
    "DNI": [6.5],
    "Shading_North": [0.5],
    "Shading_South": [0.8],
    "Shading_East": [0.7],
    "Shading_West": [0.6]
})

# Make predictions
new_pred = model.predict(new_building)
print(f"Energy Outputs for new building: {new_pred}")
