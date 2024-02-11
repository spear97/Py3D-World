from model import *
import glm
import random

# BOUNDS About X-Axis
X_MIN, X_MAX = -115, -25

# BOUNDS About Z-Axis
ENV1_Z_MIN, ENV1_Z_MAX = -45, 45
ENV2_Z_MIN, ENV2_Z_MAX = -160, -70
ENV3_Z_MIN, ENV3_Z_MAX = 68, 160


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

    """
    Loader and Updater Functions
    """

    # Method to load initial objects into the scene (e.g., floor)
    def load(self):

        app = self.app
        add = self.add_object

        # Default Environment
        self.render_DefaultEnvironment(app, add)

        # Environment1 - Forest
        self.render_Environment1(app, add)

        # Environment2 - Rocky Terrain
        self.render_Environment2(app, add)

        # Environment3 - Desert
        self.render_Environment3(app, add)
            

    # Method to update the scene
    def update(self):
        pass

    """
    POSITION & YAW GETTERS
    """

    # Get an X Value that exists within the BOUNDS
    def get_x(self, min_val, max_val):
        return random.randrange(min_val, max_val)

    # Get a Z Value that exists with the BOUNDS
    def get_z(self, min_val, max_val):
        return random.randrange(min_val, max_val)

    # Get a yaw Value to rotate around the Y-Axis for
    def get_yaw(self):
        return random.randrange(0.0, 360.0)

    """
    PLANE POSITIONS GETTERS
    """

    # Get where the plane needs to be
    def get_plane_pos1(self):
        return (-75, -1, 0)

    # Get where the plane needs to be
    def get_plane_pos2(self):
        return (-75, -1, -115)

    # Get where the plane needs to be
    def get_plane_pos3(self):
         return (-75, -1, 115)

    # Get where the plane needs to be
    def get_plane_pos_default(self):
        return (0, -1, -10)

    """
    SCALE GETTERS
    """

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
    POSITION GENERATORS
    """

    # Generate the (X,Z) Coordinate for the Y-Value of -0.87
    def generate_height_pos_1(self, min_val, max_val):
        x,z = self.get_x(X_MIN, X_MAX), self.get_z(min_val, max_val)
        return (x, -0.87, z)

    # Genereate the (X,Z) Coordinate for the Y-Value for -0.75
    def generate_height_pos_2(self, min_val, max_val):
        x,z = self.get_x(X_MIN, X_MAX), self.get_z(min_val, max_val)
        return (x, -0.75, z)

    # Generate the Yaw-Value value for the Object to rotate to
    def generate_rotation(self):
        yaw = self.get_yaw()
        return (0, yaw, 0)

    """
    OBJECT GENERATORS
    """

    # Generate Patches of Grass
    def generate_grass_patches(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(GrassPatch(app, pos=self.generate_height_pos_1(min_val, max_val), rot=self.generate_rotation()))

    # Generate Single Instances of Grass
    def generate_grass(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Grass(app, pos=self.generate_height_pos_1(min_val, max_val), rot=self.generate_rotation()))

    # Generate Small Rocks
    def generate_small_rocks(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(SmallRock(app, pos=self.generate_height_pos_1(min_val, max_val), rot=self.generate_rotation()))

    # Generate Trees
    def generate_trees(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            
            # Generate Positions
            gen_pos = self.generate_height_pos_2(min_val, max_val)
            gen_pos_offset = (gen_pos[0], 3-gen_pos[1], gen_pos[2])

            # Generate Rotation
            gen_rot = self.generate_rotation()

            # Add Objects to Scene
            add(TreeBottom(app, pos=gen_pos, rot=gen_rot, scale=self.get_scale_1()))
            add(TreeTop(app, pos=gen_pos_offset, rot=gen_rot, scale=self.get_scale_1()))

# Generate Trees without any leaves
    def generate_trees_no_tops(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(TreeBottom(app, pos=self.generate_height_pos_1(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate Military Vehicles
    def generate_military_vehicles(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(MilitaryVehicle(app, pos=self.generate_height_pos_1(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate the First Version of Stones
    def generate_stones_A(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Stone_A(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate the Second Version of Stones
    def generate_stones_B(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Stone_B(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate the Third Version of Stones
    def generate_stones_C(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Stone_C(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate Tree Trunks
    def generate_tree_trunks(self, add, app, instances, min_val, max_val):
        for i in range(5):
            add(TreeTrunk(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation()))

    # Generate Tents
    def generate_tents(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Tent(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_1()))

    # Generate Bushes
    def generate_bushes(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(TreeTop(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(),scale=self.get_scale_1()))

    # Generate Cacti
    def generate_cacti(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Cactus(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation()))

    # Generate Pyramids
    def generate_pyramids(self, add, app, instances, min_val, max_val):
        for i in range(instances):
            add(Pyramid(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_2()))

    # Generate Camels
    def generate_camels(self, add, app, instances, min_val, max_val):
        for i in range(5):
            add(Camel(app, pos=self.generate_height_pos_2(min_val, max_val), rot=self.generate_rotation(), scale=self.get_scale_1()))

    """
    ENVIRONMENTS
    """

    # The Default Environment that will render upon start
    def render_DefaultEnvironment(self, app, add):
        add(Plane(app, pos=self.get_plane_pos_default(), scale=self.get_plane_scale()))

    # The Default Environment that will render upon start
    def render_Environment1(self, app, add):

        # Plane that Environment 1 will Generate on
        add(Plane_Grass(app, pos=self.get_plane_pos1(), scale=self.get_plane_scale()))

        # Spawn Grass Patches into the Environment
        self.generate_grass_patches(add, app, 500, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Grass into the Environment
        self.generate_grass(add, app, 150, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Small Rocks into the Environment
        self.generate_small_rocks(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Trees into the Environment
        self.generate_trees(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Military Vehicles into the Environment
        self.generate_military_vehicles(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn First Type of Stones into the Enviornment
        self.generate_stones_A(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Second Type of Stones into the Environment
        self.generate_stones_B(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Third Type of Stones into the Environment
        self.generate_stones_C(add, app, 20, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Tree Trunks inot the Environment
        self.generate_tree_trunks(add, app, 5, ENV1_Z_MIN, ENV1_Z_MAX)

        # Spawn Tents into the Environment
        self.generate_tents(add, app, 5, ENV1_Z_MIN, ENV1_Z_MAX)

    # The Default Environment that will render upon start
    def render_Environment2(self, app, add):

        # Plane that Environment2 will Generate On
        add(Plane_Dirt(app, pos=self.get_plane_pos2(), scale=self.get_plane_scale()))

        # Generate all the Patches of Grass for the Environment
        self.generate_grass_patches(add, app, 250, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all Bushes
        self.generate_bushes(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

        # Geneate all the Small Rocks for the Enviornment
        self.generate_small_rocks(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all the Grass for the Environment
        self.generate_grass(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all the Trees for the Environment
        self.generate_trees_no_tops(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all the Stone_As for the Environment
        self.generate_stones_A(add, app, 5, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all the Stone_Bs for the Environment
        self.generate_stones_B(add, app, 5, ENV2_Z_MIN, ENV2_Z_MAX)

        # Generate all the Stone_Cs for the Environment
        self.generate_stones_C(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

        # Genereate all the Military Vehicles for the Environment
        self.generate_military_vehicles(add, app, 20, ENV2_Z_MIN, ENV2_Z_MAX)

    # The Default Environment that will render upon start
    def render_Environment3(self, app, add):

        # Generate the Plane that will be needed for the Environment to Generate on
        add(Plane_Sand(app, pos=self.get_plane_pos3(), scale=self.get_plane_scale()))

        # Generate all the Cacti for the Environment
        self.generate_cacti(add, app, 20, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Small Rocks for the Environment
        self.generate_small_rocks(add, app, 20, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Stone_As for the Environment
        self.generate_stones_A(add, app, 5, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Stone_Bs for the Environment
        self.generate_stones_B(add, app, 5, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Stone_Cs for the Environment
        self.generate_stones_C(add, app, 20, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Pyramid for the Environment
        self.generate_pyramids(add, app, 5, ENV3_Z_MIN, ENV3_Z_MAX)

        # Generate all the Camels for the Environment
        self.generate_camels(add, app, 5, ENV3_Z_MIN, ENV3_Z_MAX)

