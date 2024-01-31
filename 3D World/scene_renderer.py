
# SceneRenderer class
class SceneRenderer:

    """
    responsible for rendering the 
    scene in a graphics application. 
    Below is a summary of its key 
    functionalities:

        * Initialization: The constructor 
        initializes the SceneRenderer object 
        by storing references to the application 
        (app), context (ctx), mesh (mesh), and 
        scene (scene). It also sets up a depth 
        framebuffer (depth_fbo) using the depth 
        texture from the mesh.

        * Depth Buffer Setup: The depth buffer 
        is set up using the depth_texture obtained 
        from the mesh's texture.

        * Render Shadows: The render_shadow method 
        clears the depth framebuffer and iterates 
        through each object in the scene, calling 
        the render_shadow method for each object. 
        This pass is responsible for rendering 
        shadows.

        * Main Rendering Pass: The main_render method 
        switches back to the screen framebuffer and 
        renders each object in the scene and the skybox.

        * Scene Update: The render method first updates 
        the scene's state using the update method.

        * Resource Release: The destroy method is implemented 
        to release resources, such as the depth framebuffer 
        (depth_fbo).
    """

    def __init__(self, app):

        # Reference to the application, context, mesh, and scene
        self.app = app
        self.ctx = app.ctx
        self.mesh = app.mesh
        self.scene = app.scene

        # Depth buffer setup
        self.depth_texture = self.mesh.texture.textures['depth_texture']
        self.depth_fbo = self.ctx.framebuffer(depth_attachment=self.depth_texture)

    # Method to render shadows using depth framebuffer
    def render_shadow(self):

        # Clear the depth framebuffer and render shadows for each object in the scene
        self.depth_fbo.clear()
        self.depth_fbo.use()
        for obj in self.scene.objects:
            obj.render_shadow()

    # Method for the main rendering pass
    def main_render(self):

        # Switch back to the screen framebuffer and render each object in the scene and the skybox
        self.app.ctx.screen.use()
        for obj in self.scene.objects:
            obj.render()
        self.scene.skybox.render()

    # Method to update the scene and perform rendering passes
    def render(self):

        # Update the scene's state
        self.scene.update()

        # Rendering pass 1: Render shadows
        self.render_shadow()

        # Rendering pass 2: Main rendering
        self.main_render()

    # Method to release resources (e.g., framebuffer)
    def destroy(self):
        self.depth_fbo.release()
