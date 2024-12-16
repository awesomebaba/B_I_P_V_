import pandas as pd
from pvlib.solarposition import get_solarposition
from datetime import datetime

# Example Data
latitude = 28.6   # Latitude of New Delhi, India
longitude = 77.2  # Longitude of New Delhi, India
date = datetime(2024, 12, 7, 12, 0)  # Date and Time

# Solar Position Calculation
solar_position = get_solarposition(date, latitude, longitude)

# Extract Solar Elevation and Azimuth
solar_elevation = solar_position['apparent_elevation'].iloc[0]
solar_azimuth = solar_position['azimuth'].iloc[0]

print(f"Solar Elevation: {solar_elevation:.2f}°")
print(f"Solar Azimuth: {solar_azimuth:.2f}°")
