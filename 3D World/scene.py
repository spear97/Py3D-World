from model import *
import glm
import random

# BOUNDS About X-Axis
X_MIN_BOUND, X_MAX_BOUND = -50, 50

# Bounds About Z-Axis
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

        self.render_Environment3(app, add)

    # Method to update the scene
    def update(self):
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

    # Get where the plane needs to be
    def get_plane_pos(self):
        return (0, -1, -10)

    # Get the First Option for Scaling
    def get_scale_1(self):
        return (0.5, 0.5, 0.5)

    # Get the Second Option for Scaling
    def get_scale_2(self):
        return (0.25, 0.25, 0.25)

    # Get the Scale of the plane
    def get_plane_scale(self):
        return (0.25, 0.25, 0.25)

    """
    Position Generators
    """

    # Generate the (X,Z) Coordinate for the Y-Value of -0.87
    def generate_height_pos_1(self):
        x,z = self.get_x(), self.get_z()
        return (x, -0.87, z)

    # Genereate the (X,Z) Coordinate for the Y-Value for -0.75
    def generate_height_pos_2(self):
        x,z = self.get_x(), self.get_z()
        return (x, -0.75, z)

    # Generate the Yaw-Value value for the Object to rotate to
    def generate_rotation(self):
        yaw = self.get_yaw()
        return (0, yaw, 0)

    """
    Object Generators
    """

    # Generate Patches of Grass
    def generate_grass_patches(self, add, app, instances):
        for i in range(instances):
            add(GrassPatch(app, pos=self.generate_height_pos_1(), rot=self.generate_rotation()))

    # Generate Single Instances of Grass
    def generate_grass(self, add, app, instances):
        for i in range(instances):
            add(Grass(app, pos=self.generate_height_pos_1(), rot=self.generate_rotation()))

    # Generate Small Rocks
    def generate_small_rocks(self, add, app, instances):
        for i in range(instances):
            add(SmallRock(app, pos=self.generate_height_pos_1(), rot=self.generate_rotation()))

    # Generate Trees
    def generate_trees(self, add, app, instances):
        for i in range(instances):

            # Generate Positions
            gen_pos = pos=self.generate_height_pos_2()
            gen_pos_offset= (gen_pos[0], 3-gen_pos[1], gen_pos[2])

            # Generate Rotations
            gen_rot = self.generate_rotation()

            # Add Objects to Scene
            add(TreeBottom(app, pos=gen_pos, rot=gen_rot, scale=self.get_scale_1()))
            add(TreeTop(app, pos=gen_pos_offset, rot=gen_rot, scale=self.get_scale_1()))

    # Generate Trees without any leaves
    def generate_trees_no_tops(self, add, app, instances):
        for i in range(instances):
            add(TreeBottom(app, pos=self.generate_height_pos_1(), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate Military Vehicles
    def generate_military_vehicles(self, add, app, instances):
        for i in range(instances):
            add(MilitaryVehicle(app, pos=self.generate_height_pos_1(), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate the First Version of Stones
    def generate_stones_A(self, add, app, instances):
        for i in range(instances):
            add(Stone_A(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate the Second Version of Stones
    def generate_stones_B(self, add, app, instances):
        for i in range(instances):
            add(Stone_B(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate the Third Version of Stones
    def generate_stones_C(self, add, app, instances):
        for i in range(instances):
            add(Stone_C(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate Tree Trunks
    def generate_tree_trunks(self, add, app, instances):
        for i in range(5):
            add(TreeTrunk(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation()))

    # Generate Tents
    def generate_tents(self, add, app, instances):
        for i in range(instances):
            add(Tent(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate Bushes
    def generate_bushes(self, add, app, instances):
        for i in range(instances):
            add(TreeTop(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(),scale=self.get_scale_1()))

    # Generate Cacti
    def generate_cacti(self, add, app, instances):
        for i in range(instances):
            add(Cactus(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation()))

    # Generate Pyramids
    def generate_pyramids(self, add, app, instances):
        for i in range(instances):
            add(Pyramid(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate Camels
    def generate_camels(self, add, app, instances):
        for i in range(5):
            add(Camel(app, pos=self.generate_height_pos_2(), rot=self.generate_rotation(), scale=self.get_scale_1()))

    """
    Environment
    """

    # The Default Environment that will render upon start
    def render_DefaultEnvironment(self, app, add):
        add(Plane(app, pos=self.get_plane_pos(), scale=self.get_plane_scale()))

    # The First Environment that is able to be selected to render
    def render_Environment1(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Grass(app, pos=self.get_plane_pos(), scale=self.get_plane_scale()))
        
        # Generate all the Patches of Grass for the Environment
        self.generate_grass_patches(instances=500, add=add, app=app)

        # Generate all the Grass for the Environment
        self.generate_grass(instances=150, add=add, app=app)

        # Geneate all the Small Rocks for the Enviornment
        self.generate_small_rocks(instances=20, add=add, app=app)

        # Generate all the Trees for the Environment
        self.generate_trees(instance=20, add=add, app=app)

        # Genereate all the Military Vehicles for the Environment
        self.generate_military_vehicles(instances=20, add=add, app=app)

        # Generate all the Stone_As for the Environment
        self.generate_stones_A(instances=20, add=add, app=app)

        # Generate all the Stone_Bs for the Environment
        self.generate_stones_B(instances=20, add=add, app=app)

        # Generate all the Stone_Cs for the Environment
        self.generate_stones_C(instances=20, add=add, app=app)

        # Generate all the Tree Trunks for the Enviornment
        self.generate_tree_trunks(instances=5, add=add, app=app)

        # Generate all the Tents for the Environment
        self.generate_tents(instances=5, add=add, app=app)


    # The Second Environment that is able to be selected to render
    def render_Environment2(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Dirt(app, pos=self.get_plane_pos(), scale=self.get_plane_scale()))

        # Generate all the Patches of Grass for the Environment
        self.generate_grass_patches(instances=250, add=add, app=app)

        # Generate all Bushes
        self.generate_bushes(instances=20, add=add, app=app)

        # Geneate all the Small Rocks for the Enviornment
        self.generate_small_rocks(instances=20, add=add, app=app)

        # Generate all the Grass for the Environment
        self.generate_grass(instances=20, add=add, app=app)

        # Generate all the Trees for the Environment
        self.generate_trees_no_tops(instances=20, add=add, app=app)

        # Generate all the Stone_As for the Environment
        self.generate_stones_A(instances=5, add=add, app=app)

        # Generate all the Stone_Bs for the Environment
        self.generate_stones_B(instances=5, add=add, app=app)

        # Generate all the Stone_Cs for the Environment
        self.generate_stones_C(instances=5, add=add, app=app)

        # Genereate all the Military Vehicles for the Environment
        self.generate_military_vehicles(instances=20, add=add, app=app)

    # The Third Environment that is able to be selected to render
    def render_Environment3(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Sand(app, pos=self.get_plane_pos(), scale=self.get_plane_scale()))

        # Genereate all the Cacti for the Environment
        self.generate_cacti(instances=20, add=add, app=app)

        # Geneate all the Small Rocks for the Enviornment
        self.generate_small_rocks(instances=20, add=add, app=app)

        # Generate all the Stone_As for the Environment
        self.generate_stones_A(instances=5, add=add, app=app)

        # Generate all the Stone_Bs for the Environment
        self.generate_stones_B(instances=5, add=add, app=app)

        # Generate all the Stone_Cs for the Environment
        self.generate_stones_C(instances=5, add=add, app=app)

        # Generate all the Pyramid for the Environment
        self.generate_pyramids(instances=5, add=add, app=app)

        # Generate all the Camels for the Environment
        self.generate_camels(instances=5, add=add, app=app)


