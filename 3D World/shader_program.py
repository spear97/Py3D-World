# ShaderProgram class
class ShaderProgram:

    """
    responsible for managing and 
    loading shader programs in a 
    graphics application. Here's a 
    summary of its key features:

        * Initialization: The constructor 
        initializes the ShaderProgram object 
        by storing a reference to the context 
        (ctx) and creating a dictionary (programs) 
        to store different shader programs. It 
        then loads and stores default shader programs 
        by calling the get_program method for each.

        * Shader Loading and Compilation: The get_program 
        method takes a shader_program_name as input, reads 
        the vertex and fragment shader code from corresponding 
        files in the 'shaders' directory, and then creates a 
        shader program using the ctx.program method. The 
        compiled shader program is returned.

        * Shader Program Storage: The loaded shader programs are 
        stored in the programs dictionary with keys corresponding 
        to different shader types, such as 'default', 'skybox', 
        'advanced_skybox', and 'shadow_map'.

        * Resource Release: The destroy method is implemented to 
        release resources for all loaded shader programs. It iterates 
        through the dictionary of shader programs and releases each program.
    """

    def __init__(self, ctx):

        # Reference to the context and dictionary to store shader programs
        self.ctx = ctx
        self.programs = {}

        # Load and store default shader programs
        self.programs['default'] = self.get_program('default')
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['advanced_skybox'] = self.get_program('advanced_skybox')
        self.programs['shadow_map'] = self.get_program('shadow_map')
        self.programs['plane'] = self.get_program('default')
        self.programs['grasspatch'] = self.get_program('default')
        self.programs['militaryvehicle'] = self.get_program('default')
        self.programs['tree'] = self.get_program('default')
        self.programs['treetop'] = self.get_program('default')
        self.programs['cactus'] = self.get_program('default')
        self.programs['treetrunk'] = self.get_program('default')
        self.programs['smallrock'] = self.get_program('default')
        self.programs['stone_a'] = self.get_program('default')
        self.programs['stone_b'] = self.get_program('default')
        self.programs['stone_c'] = self.get_program('default')
        self.programs['camel'] = self.get_program('default')
        self.programs['pyramid'] = self.get_program('default')
        self.programs['plane_dirt'] = self.get_program('default')
        self.programs['plane_grass'] = self.get_program('default')
        self.programs['plane_sand'] = self.get_program('default')

    # Method to load and compile vertex and fragment shaders, then create a shader program
    def get_program(self, shader_program_name):

        # Read vertex shader code from file
        with open(f'shaders/{shader_program_name}.vert') as file:
            vertex_shader = file.read()

        # Read fragment shader code from file
        with open(f'shaders/{shader_program_name}.frag') as file:
            fragment_shader = file.read()

        # Create and return the shader program
        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    # Method to release resources for all loaded shader programs
    def destroy(self):
        [program.release() for program in self.programs.values()]
