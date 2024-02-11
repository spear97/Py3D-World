# Py3D-World

## Description

This project serves to illustrate how to render a 3D-Textured, Environment Engine utlizing Python, OpenGL, and some GLSL. It is based off two projects two seperate projects. The first being StanislavPetrovV's [3D-Graphics-Engine Project](https://github.com/StanislavPetrovV/3D-Graphics-Engine) and the second being a prior project that I initially created for in my Computer Graphics Class at Texas Wesleyan Univerity for the Spring Semester of 2022. The purpose for developing this project is to act as two things:

1. To illustrate how Python can be used to render Computer Graphics for the Purposes of Simulation Programming
2. To act as a template for anyone to use in the future. 

## Table of Contents

1. [Classes](#Classes)

# Classes

## GraphicsEngine

## Model Classes

### BaseModel

### ExtendedBaseModel

### Plane

### Plane_Grass

### Plane_Dirt

### Plane_Sand

### Grass

### Grass_Patch

### Tent

### TreeTrunk

### TreeBottom

### TreeTop

### SmallRock

### Stone_A

### Stone_B

### Stone_C

### MilitaryVehicle

### Cactus

### Pyramid

### Camel

### Cube

### MovingCube

### Skybox

### Advanced Skybox

## VBO Classes

### VBO

### BaseVBO

### CactusVBO

### CamelVBO

### GrassVBO

### GrassPatchVBO

### MilitaryVehicleVBO

### PlaneVBO

### Plane_GrassVBO

### Plane_SandVBO

### Plane_DirtVBO

### PyramidVBO

### SmallRockVBO

### Stone_A_VBO

### Stone_B_VBO

### Stone_C_VBO

### TentVBO

### TreeVBO

### TreeTopVBO

### TreeTrunkVBO

### CubeVBO

### SkyBoxVBO

### AdvanceSkyBoxVBO

## Scene

## Camera

The `Camera` class is responsible for handling camera movement, rotation, and generating view and projection matrices. Here's a summary of its key components and functionality:

- **Initialization:** The constructor initializes the camera with a reference to the application (app), an initial position, yaw, and pitch. It also sets up initial vectors representing camera orientation.

- **View and Projection Matrices:** The class maintains view and projection matrices, which are calculated during initialization and updated based on camera movement and rotation.

- **Mouse Input Handling:** The rotate method handles the camera's rotation based on mouse movement. It adjusts yaw and pitch angles and ensures that the pitch stays within reasonable bounds.

- **Camera Vectors Update:** The update_camera_vectors method updates the camera's orientation vectors (forward, right, up) based on the current yaw and pitch angles.

- **Update Method:** The update method is intended to be called in the game loop. It updates the camera's position, handles user input for movement and rotation, and recalculates the view matrix to reflect the updated camera orientation.

- **Camera Movement:** The move method processes key inputs for camera movement, adjusting the camera's position based on the pressed keys.

- **View and Projection Matrix Generation:** The get_view_matrix and get_projection_matrix methods compute the view and projection matrices, respectively, using the camera's position, orientation, and specified parameters (e.g., field of view, near, and far planes).

- **Camera Movement Speed and Sensitivity:** The camera movement speed (SPEED) and mouse sensitivity (SENSITIVITY) are constants defined outside the class.

## ShaderProgram

The `ShaderProgram` class is responsible for managing and loading shader programs in a graphics application. Here's a summary of its key features:

- **Initialization:** The constructor initializes the ShaderProgram object by storing a reference to the context (ctx) and creating a dictionary (programs) to store different shader programs. It then loads and stores default shader programs by calling the get_program method for each.

- **Shader Loading and Compilation:** The get_program method takes a shader_program_name as input, reads the vertex and fragment shader code from corresponding files in the 'shaders' directory, and then creates a shader program using the ctx.program method. The compiled shader program is returned.

- **Shader Program Storage:** The loaded shader programs are stored in the programs dictionary with keys corresponding to different shader types, such as 'default', 'skybox', 'advanced_skybox', and 'shadow_map'.

- **Resource Release:** The destroy method is implemented to release resources for all loaded shader programs. It iterates through the dictionary of shader programs and releases each program.

## VAO

The `VAO` class is responsible for managing Vertex Array Objects (VAOs) in the graphics application. Here's a summary of its key features:

- **Initialization:** The constructor initializes the VAO object with a reference to the context (ctx), a VBO object (self.vbo), and a ShaderProgram object (self.program).

- **VAO Storage:** The class contains a dictionary (self.vaos) to store different VAOs associated with various objects. The keys are string identifiers, such as 'cube,' 'shadow_cube,' 'skybox,' and 'advanced_skybox.'

- **Creating VAOs:** The get_vao method is responsible for creating and configuring a VAO. It takes a program (ShaderProgram) and a vbo (VBO) as parameters. It uses the context to create a vertex array, associating it with the provided program and VBO.

- **Destroy Method:** The destroy method is responsible for releasing resources associated with the VAO object. It calls the destroy methods of the VBO and ShaderProgram objects, ensuring that allocated OpenGL resources are properly released.

## Texture

The `Texture` class is responsible for managing textures in the graphics application. Here's a summary of its key features:

- **Initialization:** The constructor initializes the Texture object with references to the application (app), the context (ctx), and a dictionary (self.textures) to store various textures.

- **Texture Storage:** The class stores different textures with numeric and string identifiers in the self.textures dictionary. The textures include regular 2D textures, cube textures, and a depth texture.

- **Creating Depth Texture:** The get_depth_texture method creates and configures a depth texture, setting properties such as repeat behavior.

- **Creating Cube Texture:** The get_texture_cube method creates and configures a cube texture from individual face textures. It loads the face textures, flips them as needed, and writes the data to the cube texture.

- **Creating 2D Texture:** The get_texture method creates and configures a regular 2D texture. It loads the texture from a file, flips it, and configures properties such as mipmaps and anisotropic filtering.

- **Destroy Method:** The destroy method is responsible for releasing resources associated with all loaded textures. It iterates over the textures in the dictionary and calls the release method to free up OpenGL resources.
