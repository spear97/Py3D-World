from vbo import VBO
from shader_program import ShaderProgram

# VAO class
class VAO:

    """
    responsible for managing Vertex Array Objects (VAOs) 
    in the graphics application. Here's a summary of its 
    key features:

        * Initialization: The constructor initializes the VAO object 
          with a reference to the context (ctx), a VBO object (self.vbo), 
          and a ShaderProgram object (self.program).

        * VAO Storage: The class contains a dictionary (self.vaos) to store 
          different VAOs associated with various objects. The keys are string 
          identifiers, such as 'cube,' 'shadow_cube,' 'skybox,' and 'advanced_skybox.'

        * Creating VAOs: The get_vao method is responsible for creating and configuring 
          a VAO. It takes a program (ShaderProgram) and a vbo (VBO) as parameters. It uses 
          the context to create a vertex array, associating it with the provided program and VBO.

        * Destroy Method: The destroy method is responsible for releasing resources associated with 
          the VAO object. It calls the destroy methods of the VBO and ShaderProgram objects, ensuring 
          that allocated OpenGL resources are properly released.
    """

    def __init__(self, ctx):

        # Reference to the context, VBO, and ShaderProgram
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # Create and store VAOs for different objects with associated programs and VBOs
        self.vaos['skybox'] = self.get_vao(program=self.program.programs['skybox'], vbo=self.vbo.vbos['skybox'])
        self.vaos['advanced_skybox'] = self.get_vao(program=self.program.programs['advanced_skybox'], vbo=self.vbo.vbos['advanced_skybox'])

        #Objects that need to have vaos generated for
        objs = ['cube', 'plane', 'grasspatch', 
                'tent', 'grass', 'militaryvehicle', 
                'tree', 'cactus', 'treetrunk', 
                'smallrock', 'stone_a', 'stone_b', 
                'stone_c', 'camel', 'pyramid']

        #Generate the VAOs
        for obj in objs:
            self.vaos[obj] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos[obj])
            self.vaos[f"shadow_{obj}"] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos[obj])

    # Method to create and configure a VAO
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    # Method to release resources for the VAO, associated VBO, and ShaderProgram
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()