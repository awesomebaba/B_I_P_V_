import os
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Get the absolute path to the .pkl file
model_path = '/home/awesomebaba/Desktop/python/sih/ml_in_sih/linear_regression_model.pkl'

# Check if the model file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the trained model
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Welcome to the Emission Prediction API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data (energy produced in kWh) from the POST request
        data = request.get_json()
        
        # Extract energy produced (ensure the key is 'energy_produced')
        energy_produced = data['energy_produced']
        
        # Make the prediction using the loaded model
        prediction = model.predict([[energy_produced]])
        
        # Return the prediction (carbon emitted in kg)
        return jsonify({'predicted_carbon_emission': prediction[0]})
    
    except Exception as e:
        # If there's any issue with the request or prediction
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
