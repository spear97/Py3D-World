import numpy as np
import moderngl as mgl
import pywavefront

# VBO class
class VBO:

    """
    responsible for managing different 
    VBOs associated with various objects 
    in the graphics application. Here's a 
    summary of its key features:

        * Initialization: The constructor initializes 
        the VBO object with a dictionary (self.vbos) to 
        store different VBOs for various objects. It 
        creates instances of specific VBO classes 
        (CubeVBO, SkyBoxVBO, AdvancedSkyBoxVBO) and 
        stores them in the dictionary.

        * VBO Storage: The class stores VBOs for different 
        objects, such as a cube ('cube'), a skybox ('skybox'), 
        and an advanced skybox ('advanced_skybox'). Each VBO is 
        an instance of a specific VBO class.

        * Destroy Method: The destroy method is responsible for 
        releasing resources associated with all loaded VBOs. It 
        iterates over the VBOs in the dictionary and calls the 
        destroy method for each VBO, freeing up OpenGL resources.
    """

    def __init__(self, ctx):

        # Dictionary to store different VBOs for various objects
        self.vbos = {}
        self.vbos['cube'] = CubeVBO(ctx)
        self.vbos['skybox'] = SkyBoxVBO(ctx)
        self.vbos['advanced_skybox'] = AdvancedSkyBoxVBO(ctx)
        self.vbos['plane'] = PlaneVBO(ctx)
        self.vbos['grasspatch'] = GrassPatchVBO(ctx)
        self.vbos['tent'] = TentVBO(ctx)
        self.vbos['grass'] = GrassVBO(ctx)
        self.vbos['militaryvehicle'] = MilitaryVehicleVBO(ctx)
        self.vbos['tree'] = TreeVBO(ctx)
        self.vbos['treetop'] = TreeTopVBO(ctx)
        self.vbos['cactus'] = CactusVBO(ctx)
        self.vbos['treetrunk'] = TreeTrunkVBO(ctx)
        self.vbos['smallrock'] = SmallRockVBO(ctx)
        self.vbos['stone_a'] = Stone_A_VBO(ctx)
        self.vbos['stone_b'] = Stone_B_VBO(ctx)
        self.vbos['stone_c'] = Stone_C_VBO(ctx)
        self.vbos['camel'] = CamelVBO(ctx)
        self.vbos['pyramid'] = PyramidVBO(ctx)
        self.vbos['plane_grass'] = Plane_GrassVBO(ctx)
        self.vbos['plane_dirt'] = Plane_DirtVBO(ctx)
        self.vbos['plane_sand'] = Plane_SandVBO(ctx)

    # Method to release resources for all loaded VBOs
    def destroy(self):
        [vbo.destroy() for vbo in self.vbos.values()]

# BaseVBO class
class BaseVBO:

    """
    an abstract base class providing 
    a foundation for managing Vertex 
    Buffer Objects (VBOs) in the graphics 
    application. Here's a summary of its 
    key features:

        * Initialization: The constructor 
        initializes the BaseVBO object with 
        a reference to the context (self.ctx), 
        a VBO (self.vbo), and placeholders 
        (self.format and self.attribs) for the 
        vertex format attributes.

        * Abstract Method: The class defines an 
        abstract method get_vertex_data, which 
        is intended to be implemented in derived 
        classes. This method is responsible for 
        providing the vertex data that will be 
        used to create the VBO.

        * VBO Creation: The get_vbo method is 
        responsible for creating and configuring 
        a VBO using the vertex data obtained from 
        the get_vertex_data method.

        * Resource Release: The destroy method 
        releases resources associated with the 
        VBO. It calls the release method on the 
        VBO, freeing up OpenGL resources.
    """

    def __init__(self, ctx):
        # Reference to the context, VBO, and attributes for vertex format
        self.ctx = ctx
        self.vbo = self.get_vbo()
        self.format: str = None
        self.attribs: list = None

    # Abstract method to get vertex data (to be implemented in derived classes)
    def get_vertex_data(self): ...

    # Method to create and configure a VBO using vertex data
    def get_vbo(self):
        vertex_data = self.get_vertex_data()
        vbo = self.ctx.buffer(vertex_data)
        return vbo

    # Method to release resources for the VBO
    def destroy(self):
        self.vbo.release()

# Define a class named CactusVBO that inherits from BaseVBO
class CactusVBO(BaseVBO):
    # Constructor method to initialize the CactusVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/cactus.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named CamelVBO that inherits from BaseVBO
class CamelVBO(BaseVBO):
    # Constructor method to initialize the CamelVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/camel.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named GrassVBO that inherits from BaseVBO
class GrassVBO(BaseVBO):
    # Constructor method to initialize the GrassVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/grass.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named GrassPatchVBO that inherits from BaseVBO
class GrassPatchVBO(BaseVBO):
    # Constructor method to initialize the GrassPatchVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the grasspatch from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the grasspatch and parse its contents
        objs = pywavefront.Wavefront('objects/grasspatch.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named TentVBO that inherits from BaseVBO
class MilitaryVehicleVBO(BaseVBO):
    # Constructor method to initialize the MilitaryVehicleVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the militaryvehicle from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the grasspatch and parse its contents
        objs = pywavefront.Wavefront('objects/militaryvehicle.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named PlaneVBO that inherits from BaseVBO
class PlaneVBO(BaseVBO):
    # Constructor method to initialize the PlaneVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/plane.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Plane_GrassVBO that inherits from BaseVBO
class Plane_GrassVBO(BaseVBO):
    # Constructor method to initialize the Plane_GrassVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/plane_grass.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Plane_SandVBO that inherits from BaseVBO
class Plane_SandVBO(BaseVBO):
    # Constructor method to initialize the Plane_SandVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/plane_sand.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Plane_DirtVBO that inherits from BaseVBO
class Plane_DirtVBO(BaseVBO):
    # Constructor method to initialize the Plane_DirtVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/plane_dirt.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named PyramidVBO that inherits from BaseVBO
class PyramidVBO(BaseVBO):
    # Constructor method to initialize the PyramidVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/pyramid.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named SmallRockVBO that inherits from BaseVBO
class SmallRockVBO(BaseVBO):
    # Constructor method to initialize the SmallRockVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the plane from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/smallrock.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Stone_A_VBO that inherits from BaseVBO
class Stone_A_VBO(BaseVBO):
    # Constructor method to initialize the Stone_A_VBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for stone_a from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/stone_a.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Stone_B_VBO that inherits from BaseVBO
class Stone_B_VBO(BaseVBO):
    # Constructor method to initialize the Stone_B_VBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for stone_a from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/stone_b.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named Stone_C_VBO that inherits from BaseVBO
class Stone_C_VBO(BaseVBO):
    # Constructor method to initialize the Stone_C_VBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for stone_a from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/stone_c.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named TentVBO that inherits from BaseVBO
class TentVBO(BaseVBO):
    # Constructor method to initialize the TentVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the grasspatch from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the grasspatch and parse its contents
        objs = pywavefront.Wavefront('objects/tent.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named TreeVBO that inherits from BaseVBO
class TreeVBO(BaseVBO):
    # Constructor method to initialize the TreeVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the tree from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the tree and parse its contents
        objs = pywavefront.Wavefront('objects/tree.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named TreeTopVBO that inherits from BaseVBO
class TreeTopVBO(BaseVBO):
    # Constructor method to initialize the TreeTopVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the tree from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the tree and parse its contents
        objs = pywavefront.Wavefront('objects/treetop.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data

# Define a class named TreeTrunkVBO that inherits from BaseVBO
class TreeTrunkVBO(BaseVBO):
    # Constructor method to initialize the TreeTrunkVBO object
    def __init__(self, app):
        # Call the constructor of the parent class (BaseVBO) using super()
        super().__init__(app)
        
        # Define the format of the vertex data (2D texture coordinates, 3D normals, 3D positions)
        self.format = '2f 3f 3f'
        
        # Specify attribute names corresponding to texture coordinates, normals, and positions
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Method to retrieve vertex data for the TreeTrunk from an external Wavefront .obj file
    def get_vertex_data(self):
        # Load the Wavefront .obj file representing the plane and parse its contents
        objs = pywavefront.Wavefront('objects/treetrunk.obj', cache=True, parse=True)
        
        # Extract the vertex data from the parsed object's materials
        obj = objs.materials.popitem()[1]
        vertex_data = obj.vertices
        
        # Convert the vertex data to a NumPy array with float32 data type
        vertex_data = np.array(vertex_data, dtype='f4')
        
        # Return the processed vertex data
        return vertex_data


# CubeVBO class, derived from BaseVBO
class CubeVBO(BaseVBO):

    """
    derived from the BaseVBO class, 
    and it is specifically designed 
    for managing Vertex Buffer Objects 
    (VBOs) related to a cube in a graphics 
    application. Here's a summary of its 
    key features:

        * Initialization: The constructor initializes 
        the CubeVBO object by calling the constructor 
        of the base class (BaseVBO) using super().__init__(ctx). 
        It also sets the format and attribs attributes to 
        define the vertex format for the cube.

        * Vertex Format: The format attribute is set to '2f 3f 3f', 
        indicating the format for vertex data with 2 floats for 
        texture coordinates, 3 floats for normals, and 3 floats 
        for positions.

        * Attributes: The attribs attribute is set to a list of 
        attribute names corresponding to the vertex format. It 
        includes 'in_texcoord_0', 'in_normal', and 'in_position', 
        which are commonly used in shaders.

        * Static Method for Vertex Data: The get_data static method 
        takes vertices and indices and arranges the vertex data 
        accordingly. It is used to generate the final vertex data 
        for the cube.

        * Vertex Data Generation: The get_vertex_data method is 
        implemented to generate the vertex data for the cube. 
        It defines the cube's vertices, indices to form triangles, 
        and additional data such as texture coordinates and normals. 
        It then uses the get_data method to concatenate this data and 
        create the final vertex data.

        * Texture Coordinates and Normals: The texture coordinates are 
        defined for each vertex, and normals are specified for each 
        face of the cube.

        * Final Vertex Data: The final vertex data is a NumPy array that 
        includes normals, texture coordinates, and positions. This data 
        is structured to match the specified vertex format.
    """

    def __init__(self, ctx):
        super().__init__(ctx)
        self.format = '2f 3f 3f'
        self.attribs = ['in_texcoord_0', 'in_normal', 'in_position']

    # Static method to arrange vertex data based on vertices and indices
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    # Method to generate vertex data for the cube
    def get_vertex_data(self):
        # Cube vertices
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        # Indices to form triangles
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]
        
        # Generate vertex data using vertices and indices
        vertex_data = self.get_data(vertices, indices)

        # Texture coordinates
        tex_coord_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
        tex_coord_indices = [(0, 2, 3), (0, 1, 2),
                             (0, 2, 3), (0, 1, 2),
                             (0, 1, 2), (2, 3, 0),
                             (2, 3, 0), (2, 0, 1),
                             (0, 2, 3), (0, 1, 2),
                             (3, 1, 2), (3, 0, 1)]

        # Generate texture coordinate data using tex_coord_vertices and tex_coord_indices
        tex_coord_data = self.get_data(tex_coord_vertices, tex_coord_indices)

        # Normals for each face of the cube
        normals = [(0, 0, 1) * 6,
                   (1, 0, 0) * 6,
                   (0, 0, -1) * 6,
                   (-1, 0, 0) * 6,
                   (0, 1, 0) * 6,
                   (0, -1, 0) * 6]

        # Convert normals to numpy array and reshape to match the vertex_data format
        normals = np.array(normals, dtype='f4').reshape(36, 3)

        # Concatenate normals, vertex_data, and tex_coord_data to form the final vertex_data
        vertex_data = np.hstack([normals, vertex_data])
        vertex_data = np.hstack([tex_coord_data, vertex_data])
        return vertex_data

# SkyBoxVBO class, derived from BaseVBO
class SkyBoxVBO(BaseVBO):

    """
    derived from the BaseVBO class 
    and is designed for managing Vertex 
    Buffer Objects (VBOs) related to a 
    skybox in a graphics application. 
    Here's a summary of its key features:

        * Initialization: The constructor initializes 
        the SkyBoxVBO object by calling the constructor 
        of the base class (BaseVBO) using super().__init__(ctx). 
        It then sets the format to '3f' (three floats per vertex) 
        and defines the attribute names for the shader program 
        (in_position).

        * Static Method for Vertex Data: The class includes a static 
        method, get_data, which arranges vertex data based on vertices 
        and indices. This method is used to generate the final vertex 
        data for the skybox.

        * Vertex Data Generation: The get_vertex_data method is implemented 
        to generate the vertex data for the skybox. It defines the skybox's 
        vertices, indices to form triangles, and uses the get_data method to 
        concatenate this data and create the final vertex data.

        * Data Transformation: Before returning the vertex data, the method 
        flips the data along the second axis and copies it to ensure C-order. 
        This transformation is done to match the data format expected by the 
        graphics library.
    """

    # Constructor for SkyBoxVBO class, derived from BaseVBO
    def __init__(self, ctx):

        # Call the constructor of the base class (BaseVBO)
        super().__init__(ctx)
    
        # Set the format for vertex data to '3f' (three floats per vertex)
        self.format = '3f'
    
        # Define the attribute names for the shader program
        self.attribs = ['in_position']

    # Static method to arrange vertex data based on vertices and indices
    @staticmethod
    def get_data(vertices, indices):
        data = [vertices[ind] for triangle in indices for ind in triangle]
        return np.array(data, dtype='f4')

    # Method to generate vertex data for the skybox
    def get_vertex_data(self):
        # Skybox vertices
        vertices = [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1),
                    (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1)]

        # Indices to form triangles
        indices = [(0, 2, 3), (0, 1, 2),
                   (1, 7, 2), (1, 6, 7),
                   (6, 5, 4), (4, 7, 6),
                   (3, 4, 5), (3, 5, 0),
                   (3, 7, 4), (3, 2, 7),
                   (0, 6, 1), (0, 5, 6)]

        # Generate vertex data using vertices and indices
        vertex_data = self.get_data(vertices, indices)

        # Flip the data along the second axis and copy it to ensure C-order
        vertex_data = np.flip(vertex_data, 1).copy(order='C')
        return vertex_data

# AdvancedSkyBoxVBO class, derived from BaseVBO
class AdvancedSkyBoxVBO(BaseVBO):

    """
    derived from the BaseVBO 
    class and is designed for 
    managing Vertex Buffer Objects 
    (VBOs) related to an advanced 
    skybox in a graphics application. 
    Here's a summary of its key features:

        * Initialization: The constructor 
        initializes the AdvancedSkyBoxVBO 
        object by calling the constructor 
        of the base class (BaseVBO) using 
        super().__init__(ctx). It then sets 
        the format to '3f' (three floats per 
        vertex) and defines the attribute names 
        for the shader program (in_position).

        * Vertex Data Generation: The get_vertex_data 
        method is implemented to generate the vertex 
        data for the advanced skybox. It sets a specific 
        z value in clip space and defines three vertices 
        in clip space. The vertices are then converted 
        into a NumPy array with float32 dtype, and this 
        array is returned as the final vertex data.
    """

    # Constructor for AdvancedSkyBoxVBO class, derived from BaseVBO
    def __init__(self, ctx):
        # Call the constructor of the base class (BaseVBO)
        super().__init__(ctx)
    
        # Set the format for vertex data to '3f' (three floats per vertex)
        self.format = '3f'
    
        # Define the attribute names for the shader program
        self.attribs = ['in_position']


    # Method to generate vertex data for the advanced skybox
    def get_vertex_data(self):
        # Set z value in clip space
        z = 0.9999
        
        # Define vertices in clip space
        vertices = [(-1, -1, z), (3, -1, z), (-1, 3, z)]
        
        # Convert vertices to numpy array with float32 dtype
        vertex_data = np.array(vertices, dtype='f4')
        return vertex_data













