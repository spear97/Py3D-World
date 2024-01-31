from vao import VAO
from texture import Texture

# Mesh class responsible for managing vertex array objects (VAO) and textures
class Mesh:

    """
    responsible for managing Vertex Array Objects (VAO) 
    and textures in the graphics application. Here's a 
    summary of its key features:

        * Initialization: The constructor initializes the Mesh 
          object with a reference to the application (app). It 
          then creates and initializes a VAO and a Texture object.

        * Vertex Array Object (VAO): The Mesh class contains a VAO 
          object (self.vao), which is responsible for managing the 
          configuration of vertex attributes and their associated data.

        * Texture: The class includes a Texture object (self.texture) 
          responsible for managing textures used in the mesh.

        * Destroy Method: The destroy method is responsible for releasing 
          resources associated with the Mesh object. It calls the destroy 
          methods of both the VAO and Texture objects, ensuring that allocated 
          OpenGL resources are properly released.
    """

    def __init__(self, app):
        self.app = app
        
        # Initialize Vertex Array Object (VAO) and Texture
        self.vao = VAO(app.ctx)
        self.texture = Texture(app)

    # Destroy the VAO and Texture
    def destroy(self):
        self.vao.destroy()
        self.texture.destroy()
