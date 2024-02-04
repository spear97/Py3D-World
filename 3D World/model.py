import moderngl as mgl
import numpy as np
import glm

"""
PARENT OBJECTS
"""

class BaseModel:

    """
    serves as a foundation for representing 
    3D objects in the graphics application. 
    Below is a summary of its key functionalities:

        * Constructor: The constructor initializes an 
        object in the 3D scene. It takes parameters 
        such as the application (app), Vertex Array 
        Object (VAO) name (vao_name), texture ID (tex_id), 
        initial position (pos), rotation angles (rot), 
        and scale (scale). It stores references to the 
        application, initializes the object's transformation 
        properties, calculates the initial model matrix, 
        and sets up texture and VAO information.

        * Update Method: The update method is a placeholder 
        that should be implemented in derived classes. It 
        is intended to update the object's state, and it 
        is called within the game loop.

        * Get Model Matrix Method: The get_model_matrix 
        method calculates and returns the model matrix 
        for the object based on its position, rotation, 
        and scale. It uses the glm library for matrix 
        transformations.

        * Render Method: The render method updates the object's 
        state by calling the update method and then renders the 
        object using its associated VAO.
    """

    # Constructor for an object in the 3D scene
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        # Reference to the application
        self.app = app

        # Initial position, rotation, and scale of the object
        self.pos = pos
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale

        # Model matrix for the object
        self.m_model = self.get_model_matrix()

        # Texture ID and Vertex Array Object (VAO) information
        self.tex_id = tex_id
        self.vao_name = vao_name
        self.vao = app.mesh.vao.vaos[vao_name]

        # Program associated with the VAO
        self.program = self.vao.program

        # Reference to the camera for rendering
        self.camera = self.app.camera

    # Method to update the object's state (called in the game loop)
    def update(self): ...

    # Method to calculate and return the model matrix for the object
    def get_model_matrix(self):

        # Initialize the model matrix
        m_model = glm.mat4()

        # Translate the model matrix based on the object's position
        m_model = glm.translate(m_model, self.pos)

        # Rotate the model matrix based on the object's rotation angles
        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))

        # Scale the model matrix based on the object's scale
        m_model = glm.scale(m_model, self.scale)

        # Return the calculated model matrix
        return m_model

    # Method to render the object
    def render(self):

        # Update the object's state before rendering
        self.update()

        # Render the object using its associated Vertex Array Object (VAO)
        self.vao.render()

# ExtendedBaseModel class, inheriting from BaseModel
class ExtendedBaseModel(BaseModel):

    def __init__(self, app, vao_name, tex_id, pos, rot, scale):

        # Call the constructor of the base class (BaseModel)
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

        # Perform additional initialization specific to ExtendedBaseModel
        self.on_init()

    # Method to update the object's state for rendering
    def update(self):

        # Bind the texture and update shader uniforms for rendering
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    # Method to update shadow-related shader uniforms
    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    # Method to render the object for shadow mapping
    def render_shadow(self):
        # Update shadow-related shader uniforms and render using shadow VAO
        self.update_shadow()
        self.shadow_vao.render()

    # Method to perform additional initialization
    def on_init(self):

        # Update light-related shader uniforms
        self.program['m_view_light'].write(self.app.light.m_view_light)

        # Set texture and MVP matrices for the main rendering program
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)

        # Configure shadow-related rendering parameters
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)

        # Set texture and MVP matrices for the shadow mapping program
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

        # Set light-related shader uniforms for the main rendering program
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)

"""
OBJECTS THAT CAN BE SPAWNED
"""

# Define a class named Plane that inherits from ExtendedBaseModel
class Plane(ExtendedBaseModel):
    # Constructor method to initialize the Plane object
    def __init__(self, app, vao_name='plane', tex_id='plane',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Plane that inherits from ExtendedBaseModel
class Plane_Grass(ExtendedBaseModel):
    # Constructor method to initialize the Plane object
    def __init__(self, app, vao_name='plane_grass', tex_id='plane_grass',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        
# Define a class named Plane that inherits from ExtendedBaseModel
class Plane_Dirt(ExtendedBaseModel):
    # Constructor method to initialize the Plane object
    def __init__(self, app, vao_name='plane_dirt', tex_id='plane_dirt',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Plane that inherits from ExtendedBaseModel
class Plane_Sand(ExtendedBaseModel):
    # Constructor method to initialize the Plane object
    def __init__(self, app, vao_name='plane_sand', tex_id='plane_sand',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Grass that inherits from ExtendedBaseModel
class Grass(ExtendedBaseModel):
    # Constructor method to initialize the Grass object
    def __init__(self, app, vao_name='grass', tex_id='grass',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named GrassPatch that inherits from ExtendedBaseModel
class GrassPatch(ExtendedBaseModel):
    # Constructor method to initialize the GrassPatch object
    def __init__(self, app, vao_name='grasspatch', tex_id='grasspatch',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Tent that inherits from ExtendedBaseModel
class Tent(ExtendedBaseModel):
    # Constructor method to initialize the GrassPatch object
    def __init__(self, app, vao_name='tent', tex_id='tent',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named TreeTrunk that inherits from ExtendedBaseModel
class TreeTrunk(ExtendedBaseModel):
    # Constructor method to initialize the TreeTrunk object
    def __init__(self, app, vao_name='treetrunk', tex_id='treetrunk',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(0.1, 0.1, 0.1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named TreeBottom that inherits from ExtendedBaseModel
class TreeBottom(ExtendedBaseModel):
    # Constructor method to initialize the TreeBottom object
    def __init__(self, app, vao_name='tree', tex_id='tree',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named TreeTop that inherits from ExtendedBaseModel
class TreeTop(ExtendedBaseModel):
    # Constructor method to initialize the TreeTop object
    def __init__(self, app, vao_name='treetop', tex_id='treetop',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Small Rock that inherits from ExtendedBaseModel
class SmallRock(ExtendedBaseModel):
    # Constructor method to initialize the Small Rock object
    def __init__(self, app, vao_name='smallrock', tex_id='smallrock',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Stone_A that inherits from ExtendedBaseModel
class Stone_A(ExtendedBaseModel):
    # Constructor method to initialize the Stone_A object
    def __init__(self, app, vao_name='stone_a', tex_id='stone_a',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Stone_B that inherits from ExtendedBaseModel
class Stone_B(ExtendedBaseModel):
    # Constructor method to initialize the Stone_B object
    def __init__(self, app, vao_name='stone_b', tex_id='stone_b',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(25, 25, 25)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Stone_B that inherits from ExtendedBaseModel
class Stone_C(ExtendedBaseModel):
    # Constructor method to initialize the Stone_C object
    def __init__(self, app, vao_name='stone_c', tex_id='stone_c',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Military Vehicle that inherits from ExtendedBaseModel
class MilitaryVehicle(ExtendedBaseModel):
    # Constructor method to initialize the GrassPatch object
    def __init__(self, app, vao_name='militaryvehicle', tex_id='militaryvehicle',
                 pos=(0, -0.75, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Cactus that inherits from ExtendedBaseModel
class Cactus(ExtendedBaseModel):
    # Constructor method to initialize the Cactus object
    def __init__(self, app, vao_name='cactus', tex_id='cactus',
                 pos=(0, -0.9, 0), rot=(0, 0, 0), scale=(0.0075, 0.0075, 0.0075)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Pyramid that inherits from ExtendedBaseModel
class Pyramid(ExtendedBaseModel):
    # Constructor method to initialize the Pyramid object
    def __init__(self, app, vao_name='pyramid', tex_id='pyramid',
                 pos=(0, -1, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Define a class named Camel that inherits from ExtendedBaseModel
class Camel(ExtendedBaseModel):
    # Constructor method to initialize the Camel object
    def __init__(self, app, vao_name='camel', tex_id='camel',
                 pos=(0, -1, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        # Call the constructor of the parent class (ExtendedBaseModel) using super()
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# Cube class, inheriting from ExtendedBaseModel
class Cube(ExtendedBaseModel):

    def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        # Call the constructor of the base class (ExtendedBaseModel)
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

# MovingCube class, inheriting from Cube
class MovingCube(Cube):

    def __init__(self, *args, **kwargs):

        # Call the constructor of the base class (Cube) with provided arguments and keyword arguments
        super().__init__(*args, **kwargs)

    # Override the update method to ensure the model matrix is updated before rendering
    def update(self):

        # Update the model matrix based on the current position, rotation, and scale
        self.m_model = self.get_model_matrix()

        # Call the update method of the base class (Cube) to perform additional updates
        super().update()

"""
SKYBOXES
"""

# SkyBox class, inheriting from BaseModel
class SkyBox(BaseModel):

    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        # Call the constructor of the base class (BaseModel)
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        
        # Perform additional initialization specific to SkyBox
        self.on_init()

    # Override the update method to update the view matrix for the skybox
    def update(self):

        # Write the modified view matrix (without translation) to the shader
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    # Method to perform additional initialization for the skybox
    def on_init(self):

        # Set the skybox texture and configure shader uniform
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)

        # Set the projection and modified view matrix for the shader
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

# AdvancedSkyBox class, inheriting from BaseModel
class AdvancedSkyBox(BaseModel):

    def __init__(self, app, vao_name='advanced_skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):

        # Call the constructor of the base class (BaseModel)
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

        # Perform additional initialization specific to AdvancedSkyBox
        self.on_init()

    # Override the update method to update the inverse projection view matrix for the skybox
    def update(self):

        # Calculate the inverse projection view matrix and write it to the shader
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    # Method to perform additional initialization for the advanced skybox
    def on_init(self):

        # Set the skybox texture and configure shader uniform
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)



















