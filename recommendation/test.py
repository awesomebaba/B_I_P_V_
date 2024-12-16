import pandas as pd
import numpy as np
import folium
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

# Step 1: Load the Dataset
dataset_path = '/home/awesomebaba/Desktop/python/sih/ml_in_sih/recommendation/eeshu_raj.csv'  # Replace with your dataset path
df = pd.read_csv(dataset_path)

# Step 2: Check Dataset Columns
print("Dataset columns:", df.columns)

if not all(col in df.columns for col in ['latitude', 'longitude', 'height']):
    raise KeyError("Dataset must contain 'latitude', 'longitude', and 'height' columns.")

# Step 3: Categorize Heights into 4 Types: Low, Medium, High, Very High
def categorize_height(height):
    if height < 5:
        return 'Low'
    elif height < 15:
        return 'Medium'
    elif height < 25:
        return 'High'
    else:
        return 'Very High'

df['Height Category'] = df['height'].apply(categorize_height)

# Step 4: Features for Clustering (Latitude, Longitude, and Height)
features = ['latitude', 'longitude', 'height']
X = df[features].values

# Step 5: Normalize the Features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 6: Apply DBSCAN Clustering (Use a large epsilon for wider clusters)
dbscan = DBSCAN(eps=0.6, min_samples=10)  # Adjust eps for larger radius and min_samples for density
df['Cluster'] = dbscan.fit_predict(X_scaled)

# Step 7: Visualize Clusters on a Map
map_center = [df['latitude'].mean(), df['longitude'].mean()]
m = folium.Map(location=map_center, zoom_start=12)

# Colors based on Height Categories
height_category_colors = {
    'Low': 'lightblue', 
    'Medium': 'orange', 
    'High': 'red', 
    'Very High': 'darkred'
}

# Radius mapping based on Height Categories
height_category_radius = {
    'Low': 8,     # Smaller radius for low height
    'Medium': 12,  # Medium radius for medium height
    'High': 18,    # Larger radius for high buildings
    'Very High': 22  # Very large radius for very high buildings
}

# Step 8: Add clusters to the map with different colors and radius based on height category
for cluster_id in np.unique(df['Cluster']):
    cluster_data = df[df['Cluster'] == cluster_id]
    for _, row in cluster_data.iterrows():
        height_category = row['Height Category']
        radius = height_category_radius[height_category]
        color = height_category_colors[height_category]
        
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=radius,  # Adjusted radius for better visibility
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.7
        ).add_to(m)

# Step 9: Save the Map to HTML
m.save('dbscan_cluster_map.html')
print("Cluster map with height categories saved as dbscan_cluster_map.html.")

# Step 10: Save the clustered dataset
df.to_csv('dbscan_clustered_dataset.csv', index=False)
print("Clustered dataset with height categories saved.")
