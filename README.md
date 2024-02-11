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

## ShaderProgram

## VAO

## Texture

The `Texture` class is responsible for managing textures in the graphics application. Here's a summary of its key features:

- **Initialization:** The constructor initializes the Texture object with references to the application (app), the context (ctx), and a dictionary (self.textures) to store various textures.

- **Texture Storage:** The class stores different textures with numeric and string identifiers in the self.textures dictionary. The textures include regular 2D textures, cube textures, and a depth texture.

- **Creating Depth Texture:** The get_depth_texture method creates and configures a depth texture, setting properties such as repeat behavior.

- **Creating Cube Texture:** The get_texture_cube method creates and configures a cube texture from individual face textures. It loads the face textures, flips them as needed, and writes the data to the cube texture.

- **Creating 2D Texture:** The get_texture method creates and configures a regular 2D texture. It loads the texture from a file, flips it, and configures properties such as mipmaps and anisotropic filtering.

- **Destroy Method:** The destroy method is responsible for releasing resources associated with all loaded textures. It iterates over the textures in the dictionary and calls the release method to free up OpenGL resources.
