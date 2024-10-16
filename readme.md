# BIPV Potential Assessment and Visualization Using LOD-1 3D City Model (BlueSentinel)

## Project Overview

This project focuses on creating an **interactive application** to help assess **Building Integrated Photovoltaic (BIPV)** potential for buildings using a **LOD-1 (Level of Detail 1) 3D City Model**. The application will simulate building shadows and calculate how much sunlight hits the vertical surfaces of buildings, which helps determine the potential for solar panels to be integrated into the building’s walls.

The application is designed to be used by **policy-makers**, **solar energy providers**, **architects**, and **citizens** to evaluate how much solar energy can be harvested from vertical surfaces (building façades) in addition to rooftops. It will be part of the **VEDAS portal** under the "3D City Model and Rooftop Solar Potential" tool.

## Key Features
- **3D City Visualization**: Uses satellite data (Cartosat-2/3 and Cartosat-1) to create basic 3D models of buildings (LOD-1 models) by extruding building footprints.
- **Shadow Simulation**: Simulates the shadows cast by nearby buildings on each building surface based on the sun's position.
- **Solar Energy Calculation**: Estimates the amount of sunlight hitting vertical building faces and calculates the BIPV potential.
- **User Input**: Users can choose a date (to simulate the sun’s position) and input Global Horizontal Irradiation (GHI) values for that date.
- **Energy Potential Display**: Renders building surfaces in 3D, color-coded based on their BIPV potential. It will also show the total energy potential from both BIPV and rooftop solar panels for the building.

## How It Works

1. **Input**: 
   - Select a **date** (to determine the sun’s position).
   - Enter **Global Horizontal Irradiation (GHI)** data (sunlight energy for that day).

2. **Process**:
   - The system generates a simple 3D city model from satellite data (LOD-1).
   - Shadows from nearby buildings are simulated.
   - The amount of sunlight that hits the building walls is calculated based on the GHI input and the sun’s position.

3. **Output**:
   - The 3D city model is displayed, with each building's surfaces colored according to their BIPV potential.
   - The total potential for energy generation from both BIPV and rooftop solar panels is provided.

## Who Can Use This?

- **Policy-makers**: For planning renewable energy projects and setting solar energy targets for urban areas.
- **Solar Energy Providers**: To assess which buildings are suitable for BIPV installation and optimize energy generation.
- **Architects**: To integrate solar energy solutions into their building designs.
- **Citizens**: To evaluate the solar potential of their buildings for potential BIPV installation.

