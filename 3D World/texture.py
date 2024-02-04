import pygame as pg
import moderngl as mgl
import glm


# Texture class
class Texture:

    """
    responsible for managing textures 
    in the graphics application. Here's 
    a summary of its key features:

        * Initialization: The constructor 
          initializes the Texture object with 
          references to the application (app), 
          the context (ctx), and a dictionary 
          (self.textures) to store various textures.

        * Texture Storage: The class stores different 
          textures with numeric and string identifiers 
          in the self.textures dictionary. The textures 
          include regular 2D textures (0, 1, 2), a cube 
          texture ('skybox'), and a depth texture ('depth_texture').

        * Creating Depth Texture: The get_depth_texture 
          method creates and configures a depth texture, 
          setting properties such as repeat behavior.

        * Creating Cube Texture: The get_texture_cube method 
          creates and configures a cube texture from individual 
          face textures. It loads the face textures, flips them 
          as needed, and writes the data to the cube texture.

        * Creating 2D Texture: The get_texture method creates and 
          configures a regular 2D texture. It loads the texture from 
          a file, flips it, and configures properties such as mipmaps 
          and anisotropic filtering.

        * Destroy Method: The destroy method is responsible for releasing 
          resources associated with all loaded textures. It iterates over the 
          textures in the dictionary and calls the release method to free up 
          OpenGL resources.
    """

    def __init__(self, app):

        # Reference to the application, context, and dictionary to store textures
        self.app = app
        self.ctx = app.ctx
        self.textures = {}

        # Load and store various textures used in the application
        self.textures[0] = self.get_texture(path='textures/img.png')
        self.textures[1] = self.get_texture(path='textures/img_1.png')
        self.textures[2] = self.get_texture(path='textures/img_2.png')
        self.textures['skybox'] = self.get_texture_cube(dir_path='textures/skybox1/', ext='png')
        self.textures['plane'] = self.get_texture(path='textures/Untextured.png')
        self.textures['grasspatch'] = self.get_texture(path='textures/grasspatch.png')
        self.textures['grass'] = self.get_texture(path='textures/grass.png')
        self.textures['tent'] = self.get_texture(path='textures/tent.png')
        self.textures['militaryvehicle'] = self.get_texture(path='textures/militaryvehicle.png')
        self.textures['tree'] = self.get_texture(path='textures/tree.png')
        self.textures['treetop'] = self.get_texture(path='textures/treetop.png')
        self.textures['cactus'] = self.get_texture(path='textures/cactus.png')
        self.textures['treetrunk'] = self.get_texture(path='textures/treetrunk.png')
        self.textures['smallrock'] = self.get_texture(path='textures/smallrock.png')
        self.textures['stone_a'] = self.get_texture(path='textures/stone_a.png')
        self.textures['stone_b'] = self.get_texture(path='textures/stone_b.png')
        self.textures['stone_c'] = self.get_texture(path='textures/stone_c.png')
        self.textures['camel'] = self.get_texture(path='textures/camel.png')
        self.textures['pyramid'] = self.get_texture(path='textures/pyramid.png')
        self.textures['plane_dirt'] = self.get_texture(path='textures/plane_dirt.png')
        self.textures['plane_grass'] = self.get_texture(path='textures/plane_grass.png')
        self.textures['plane_sand'] = self.get_texture(path='textures/plane_sand.png')
        self.textures['depth_texture'] = self.get_depth_texture()


    # Method to create and configure a depth texture
    def get_depth_texture(self):

        depth_texture = self.ctx.depth_texture(self.app.WIN_SIZE)
        depth_texture.repeat_x = False
        depth_texture.repeat_y = False
        return depth_texture

    # Method to create and configure a cube texture from individual face textures
    def get_texture_cube(self, dir_path, ext='png'):

        faces = ['right', 'left', 'top', 'bottom'] + ['front', 'back'][::-1]
        textures = []

        # Load face textures and flip them accordingly
        for face in faces:
            texture = pg.image.load(dir_path + f'{face}.{ext}').convert()
            if face in ['right', 'left', 'front', 'back']:
                texture = pg.transform.flip(texture, flip_x=True, flip_y=False)
            else:
                texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
            textures.append(texture)

        size = textures[0].get_size()
        texture_cube = self.ctx.texture_cube(size=size, components=3, data=None)

        # Write face texture data to the cube texture
        for i in range(6):
            texture_data = pg.image.tostring(textures[i], 'RGB')
            texture_cube.write(face=i, data=texture_data)

        return texture_cube

    # Method to create and configure a regular 2D texture
    def get_texture(self, path):

        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, flip_x=False, flip_y=True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        
        # Configure mipmaps and anisotropic filtering
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        texture.anisotropy = 32.0

        return texture

    # Method to release resources for all loaded textures
    def destroy(self):
        [tex.release() for tex in self.textures.values()]