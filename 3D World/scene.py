from model import *
import glm

# Scene class
class Scene:

    """
    responsible for managing the objects within a 3D scene. 
    It maintains a list of objects and provides methods for 
    adding objects to the scene, loading initial objects 
    (e.g., floor with cubes), and updating the scene. Additionally, 
    it incorporates an advanced skybox for environmental rendering.

    Key functionalities of the Scene class:

        * Initialization: Takes a reference to the application (app) 
          and initializes an empty list to store objects. It loads 
          initial objects into the scene and creates an advanced skybox.

        * Adding Objects: Provides a method (add_object) to add objects 
          to the scene by appending them to the list of objects.

        * Loading Initial Objects: Defines a load method to populate 
          the scene with objects. In the given example, it creates a 
          floor with a grid of cubes.

        * Updating the Scene: Implements an update method to update 
          the scene. In this case, it checks if a moving cube exists 
          in the scene and, if so, updates its rotation based on the 
          application's time.
    """

    def __init__(self, app):
        # Reference to the application
        self.app = app

        # List to store objects in the scene
        self.objects = []

        # Load objects into the scene
        self.load()

        # Create and set up the advanced skybox
        self.skybox = AdvancedSkyBox(app)

    # Method to add an object to the scene
    def add_object(self, obj):
        self.objects.append(obj)

    # Method to Create a Tree with Leaves
    def make_Tree(self, app, add, pos=(0,0,0)):
        add(TreeBottom(app))
        add(TreeTop(app, pos=(pos[0], pos[1]+4, pos[2])))

    # Method to load initial objects into the scene (e.g., floor)
    def load(self):
        app = self.app
        add = self.add_object

        add(Plane(app, pos=(0, -1, -10)))
        add(Camel(app))

    # Method to update the scene
    def update(self):

        # Check if a moving cube exists in the scene
        if hasattr(self, 'moving_cube') and self.moving_cube:

            # Update the rotation of the moving cube based on the application's time
            self.moving_cube.rot.xyz = self.app.time

