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
        self.vaos['cube'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['cube'])
        self.vaos['shadow_cube'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['cube'])

        self.vaos['skybox'] = self.get_vao(program=self.program.programs['skybox'], vbo=self.vbo.vbos['skybox'])
        self.vaos['advanced_skybox'] = self.get_vao(program=self.program.programs['advanced_skybox'], vbo=self.vbo.vbos['advanced_skybox'])

        self.vaos['plane'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['plane'])
        self.vaos['shadow_plane'] = self.get_vao(program=self.program.programs['shadow_map'],vbo=self.vbo.vbos['plane'])

        self.vaos['grasspatch'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['grasspatch'])
        self.vaos['shadow_grasspatch'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['grasspatch'])

        self.vaos['tent'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['tent'])
        self.vaos['shadow_tent'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['tent'])

        self.vaos['grass'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['grass'])
        self.vaos['shadow_grass'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['grass'])

        self.vaos['militaryvehicle'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['militaryvehicle'])
        self.vaos['shadow_militaryvehicle'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['militaryvehicle'])

        self.vaos['tree'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['tree'])
        self.vaos['shadow_tree'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['tree'])

        self.vaos['treetop'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['treetop'])
        self.vaos['shadow_treetop'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['treetop'])

        self.vaos['cactus'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['cactus'])
        self.vaos['shadow_cactus'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['cactus'])

        self.vaos['treetrunk'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['treetrunk'])
        self.vaos['shadow_treetrunk'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['treetrunk'])

        self.vaos['smallrock'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['smallrock'])
        self.vaos['shadow_smallrock'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['smallrock'])

        self.vaos['stone_a'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['stone_a'])
        self.vaos['shadow_stone_a'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['stone_a'])

        self.vaos['stone_b'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['stone_b'])
        self.vaos['shadow_stone_b'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['stone_b'])

        self.vaos['stone_c'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['stone_c'])
        self.vaos['shadow_stone_c'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['stone_c'])

        self.vaos['camel'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['camel'])
        self.vaos['shadow_camel'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['camel'])

        self.vaos['pyramid'] = self.get_vao(program=self.program.programs['default'], vbo=self.vbo.vbos['pyramid'])
        self.vaos['shadow_pyramid'] = self.get_vao(program=self.program.programs['shadow_map'], vbo=self.vbo.vbos['pyramid'])


    # Method to create and configure a VAO
    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    # Method to release resources for the VAO, associated VBO, and ShaderProgram
    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()