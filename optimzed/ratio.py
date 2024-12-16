import math

# Inputs
building_height = 18  # Height of the building in meters
building_breadth = 10  # Breadth of the building side in meters
solar_elevation_angle = 40  # Solar elevation angle in degrees (calculated earlier)
solar_azimuth_angle = 160 # Solar azimuth angle in degrees (calculated earlier)

# 1. Calculate Shadow Length
if solar_elevation_angle > 0:  # Ensure the sun is above the horizon
    shadow_length = building_height / math.tan(math.radians(solar_elevation_angle))
else:
    shadow_length = float('inf')  # Shadow is infinitely long if sun is at horizon or below

# 2. Determine Shadow Orientation on Each Side
# Initialize shadow ratios for all four sides
shadow_ratios = {"North": 0, "South": 0, "East": 0, "West": 0}

# Calculate shadow ratio for each side based on the azimuth angle
if 0 <= solar_azimuth_angle < 90:  # Shadow falls toward the East
    shadow_ratios["East"] = shadow_length / building_breadth
elif 90 <= solar_azimuth_angle < 180:  # Shadow falls toward the South
    shadow_ratios["South"] = shadow_length / building_breadth
elif 180 <= solar_azimuth_angle < 270:  # Shadow falls toward the West
    shadow_ratios["West"] = shadow_length / building_breadth
else:  # Shadow falls toward the North
    shadow_ratios["North"] = shadow_length / building_breadth

# Output Results
print(f"Shadow Length: {shadow_length:.2f} meters")
for side, ratio in shadow_ratios.items():
    print(f"Shadow Ratio for {side} side: {ratio:.2f}")
