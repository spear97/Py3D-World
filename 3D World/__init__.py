import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer


# GraphicsEngine class responsible for setting up and managing the graphics engine
class GraphicsEngine:

    """
    Summary:
    designed to serve as the core component for setting up and managing a graphics engine 
    using the Pygame and ModernGL libraries. Its primary responsibilities include initializing 
    various modules, creating an OpenGL context, managing window settings, handling input events 
    (such as quitting the application), tracking time, and orchestrating the rendering pipeline. 
    The class encapsulates functionalities related to light, camera, mesh, scene, and renderer.

    Key functionalities of the GraphicsEngine class:

        * Initialization: Initializes Pygame modules, sets up window size and OpenGL attributes, 
          creates an OpenGL context, and configures mouse settings.

        * Tracking Time: Utilizes Pygame's clock to keep track of the current time and calculate 
          the time elapsed between frames.

        * Resource Management: Manages resources related to light, camera, mesh, scene, and renderer, 
          ensuring proper initialization and destruction.

        * Event Handling: Implements event handling to detect quit events, allowing for a clean shutdown 
          of the application.

        * Rendering: Clears the framebuffer, updates the camera, and renders the scene using the specified 
          renderer.

        * Main Loop: Runs the main loop of the graphics engine, continuously updating the time, checking 
          for events, updating the camera, rendering the scene, and maintaining a consistent frame rate.
    """


    def __init__(self, win_size=(1600, 900)):
        # Initialize pygame modules
        pg.init()
        
        # Window size
        self.WIN_SIZE = win_size
        
        # Set OpenGL attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        
        # Create OpenGL context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        
        # Mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        
        # Detect and use existing OpenGL context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'  # Uncomment if needed
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        
        # Create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        
        # Initialize light
        self.light = Light()
        
        # Initialize camera
        self.camera = Camera(self)
        
        # Initialize mesh
        self.mesh = Mesh(self)
        
        # Initialize scene
        self.scene = Scene(self)
        
        # Initialize renderer
        self.scene_renderer = SceneRenderer(self)

    # Check for quit events
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    # Render the scene
    def render(self):
        # Clear the framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        
        # Render the scene using the renderer
        self.scene_renderer.render()
        
        # Swap buffers
        pg.display.flip()

    # Get the current time
    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001

    # Run the graphics engine loop
    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)

# Entry point for the program
if __name__ == '__main__':
    # Create an instance of the GraphicsEngine and run the application
    app = GraphicsEngine((640, 640))
    app.run()






























