import numpy as np
import trimesh
import pyrender
from PIL import Image

def load_obj_and_render_shadow(obj_file_path, sun_direction):
    # Load the 3D model (e.g., building) using trimesh
    mesh = trimesh.load(obj_file_path)

    # Create a pyrender scene
    scene = pyrender.Scene()

    # Convert the trimesh mesh to a pyrender mesh
    mesh_node = pyrender.Mesh.from_trimesh(mesh)

    # Add the mesh to the scene
    scene.add(mesh_node)

    # Add directional light to simulate sunlight
    light = pyrender.DirectionalLight(color=np.ones(3), intensity=3.0)

    # Set the direction of the light (sun_direction)
    # Example: Sun at an arbitrary angle (sun_direction is a 3D vector)
    light_pose = np.eye(4)
    light_pose[:3, 2] = sun_direction  # Sunlight direction

    # Add the light to the scene
    scene.add(light, pose=light_pose)

    # Add a camera to the scene
    camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0)
    camera_pose = np.array([
        [1.0, 0.0,  0.0, 0.0],
        [0.0, 1.0,  0.0, -1.0],
        [0.0, 0.0,  1.0, 3.0],
        [0.0, 0.0,  0.0, 1.0]
    ])
    scene.add(camera, pose=camera_pose)

    # Create an offscreen renderer
    renderer = pyrender.OffscreenRenderer(viewport_width=640, viewport_height=480)

    # Render the scene
    color, depth = renderer.render(scene)

    # Convert the image to a PIL image and save it
    img = Image.fromarray(color)
    img.save("shadow_render_with_camera.png")

    print("Rendered image saved as 'shadow_render_with_camera.png'")

# Define the sun's direction (Example: [-1, -1, -1] as a vector)
# This simulates sunlight coming from an angle in the sky
sun_direction = np.array([-1.0, -1.0, -1.0])  # Adjust as per your needs

# Path to your .obj file
obj_file_path = '/home/awesomebaba/Desktop/python/PS_2/models/Scene.obj'  # Replace with your actual .OBJ file path

# Call the function to load the .obj and render the scene with shadows
load_obj_and_render_shadow(obj_file_path, sun_direction)
