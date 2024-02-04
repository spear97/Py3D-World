from model import *
import glm
import random


X_MIN_BOUND, X_MAX_BOUND = -50, 50
Z_MIN_BOUND, Z_MAX_BOUND = -55, 35

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
    
    # Constructor
    def __init__(self, app):
        # Reference to the application
        self.app = app

        # List to store objects in the scene
        self.objects = []

        # Load objects into the scene
        self.load()

        # Create and set up the advanced skybox
        self.skybox = AdvancedSkyBox(app)


    """
    Remover and Adder Functions
    """

    # Method to add an object to the scene
    def add_object(self, obj):
        self.objects.append(obj)

    # Method to remove an object from the scene
    def remove_object(self, obj):
        self.objects.remove(obj)


    """
    Loader and Updater Functions
    """

    # Method to load initial objects into the scene (e.g., floor)
    def load(self):
        app = self.app
        add = self.add_object

        self.render_Environment1(app, add)

    # Method to update the scene
    def update(self):
        #print('hello from Scene.Update')
        pass

    """
    GETTERS
    """

    # Get an X Value that exists within the BOUNDS
    def get_x(self):
        return random.randrange(X_MIN_BOUND, X_MAX_BOUND)

    # Get a Z Value that exists with the BOUNDS
    def get_z(self):
        return random.randrange(Z_MIN_BOUND, Z_MAX_BOUND)

    # Get a yaw Value to rotate around the Y-Axis for
    def get_yaw(self):
        return random.randrange(0.0, 360.0)

    """
    Environment
    """

    # The Default Environment that will render upon start
    def render_DefaultEnvironment(self, app, add):
        add(Plane(app, pos=(0, -1, -10), scale=(0.25, 0.25, 0.25)))

    # The First Environment that is able to be selected to render
    def render_Environment1(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Grass(app, pos=(0, -1, -10), scale=(0.25, 0.25, 0.25)))
        
        # Generate all the Patches of Grass for the Environment
        for i in range(500):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(GrassPatch(app, pos=(x, -0.87, z), rot=(0, yaw, 0)))

        # Generate all the Grass for the Environment
        for i in range(150):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(Grass(app, pos=(x, -0.87, z), rot=(0, yaw, 0)))

        # Geneate all the Small Rocks for the Enviornment
        for i in range(20):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(SmallRock(app, pos=(x, -0.87, z), rot=(0, yaw, 0), scale=(0.25, 0.25, 0.25)))

        # Generate all the Trees for the Environment
        for i in range(20):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(TreeBottom(app, pos=(x, -0.75, z), rot=(0, yaw, 0), scale=(0.5, 0.5, 0.5)))
            add(TreeTop(app, pos=(x, 3-0.75, z), rot=(0, yaw, 0), scale=(0.5, 0.5, 0.5)))

        # Genereate all the Military Vehicles for the Environment
        for i in range(20):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(MilitaryVehicle(app, pos=(x, -0.75, z), rot=(0, yaw, 0)))

        # Generate all the Stone_As for the Environment
        for i in range(5):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(Stone_A(app, pos=(x, -0.75, z), rot=(0, yaw, 0), scale=(0.25, 0.25, 0.25)))

        # Generate all the Stone_Bs for the Environment
        for i in range(5):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(Stone_B(app, pos=(x, -0.75, z), rot=(0, yaw, 0), scale=(0.25, 0.25, 0.25)))

        # Generate all the Stone_Cs for the Environment
        for i in range(5):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(Stone_C(app, pos=(x, -0.75, z), rot=(0, yaw, 0), scale=(0.25, 0.25, 0.25)))

        # Generate all the Tree Trunks for the Enviornment
        for i in range(5):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(TreeTrunk(app, pos=(x, -0.75, z), rot=(0, yaw, 0)))

        # Generate all the Tents for the Environment
        for i in range(5):
            x,z,yaw = self.get_x(), self.get_z(), self.get_yaw()
            add(Tent(app, pos=(x, -1.25, z), rot=(0, yaw, 0), scale=(0.3, 0.3, 0.3)))


    # The Second Environment that is able to be selected to render
    def render_Environment2(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Dirt(app, pos=(0, -1, -10), scale=(0.25, 0.25, 0.25)))

    # The Third Environment that is able to be selected to render
    def render_Environment3(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Sand(app, pos=(0, -1, -10), scale=(0.25, 0.25, 0.25)))


