import pandas as pd
import pickle

# Load the trained model from the pickle file
with open("/home/awesomebaba/Desktop/python/sih/ml_in_sih/optimzed/shadow_ratio_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a simple function to predict shadow ratios
def test_model(input_data):
    """
    Test the model with new input data to predict shadow ratios.
    
    Parameters:
    input_data (dict): A dictionary containing feature values for the model.
    
    Returns:
    dict: Predicted shadow ratios for North, South, East, and West sides.
    """
    # Convert input data into a pandas DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Predict shadow ratios using the trained model
    predictions = model.predict(input_df)
    
    # Return the predicted shadow ratios (assuming the model outputs 4 values for each side)
    return {
        "North_Side_Shadow_Ratio": predictions[0][0],
        "South_Side_Shadow_Ratio": predictions[0][1],
        "East_Side_Shadow_Ratio": predictions[0][2],
        "West_Side_Shadow_Ratio": predictions[0][3],
    }

# Example usage:
input_data = {
    "Latitude": 23.037454,
    "Longitude": 72.569816,
    "Building_Height": 15,
    "Distance_to_North_Building": 6.152654,
    "Distance_to_South_Building": 4.093645,
    "Distance_to_East_Building": 8.620151,
    "Distance_to_West_Building": 7.381624,
    "Height_North_Building": 7.795182,
    "Height_South_Building": 4.530818,
    "Height_East_Building": 3.193299,
    "Height_West_Building": 10.724151,
    "Azimuth_Angle": 185.566785,
    "Elevation_Angle": 48.566123
}

# Call the function to get predicted shadow ratios
predicted_ratios = test_model(input_data)

# Print the predicted shadow ratios
print(predicted_ratios)
