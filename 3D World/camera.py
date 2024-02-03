# Import necessary libraries
import glm  # GLM library for vector and matrix operations
import pygame as pg  # Pygame for handling user input and window creation

# Constants for camera settings
FOV = 50  # Field of view in degrees
NEAR = 0.1  # Near clipping plane
FAR = 100  # Far clipping plane
SPEED = 0.01  # Movement speed
SENSITIVITY = 0.04  # Mouse sensitivity

# Camera class definition
class Camera:

    """
    responsible for handling camera movement, rotation, and generating 
    view and projection matrices. Here's a summary of its key components 
    and functionality:

        * Initialization: The constructor initializes the camera with a reference 
          to the application (app), an initial position, yaw, and pitch. It also 
          sets up initial vectors representing camera orientation.

        * View and Projection Matrices: The class maintains view and projection 
          matrices, which are calculated during initialization and updated based 
          on camera movement and rotation.

        * Mouse Input Handling: The rotate method handles the camera's rotation 
          based on mouse movement. It adjusts yaw and pitch angles and ensures 
          that the pitch stays within reasonable bounds.

        * Camera Vectors Update: The update_camera_vectors method updates the 
          camera's orientation vectors (forward, right, up) based on the current 
          yaw and pitch angles.

        * Update Method: The update method is intended to be called in the game 
          loop. It updates the camera's position, handles user input for movement 
          and rotation, and recalculates the view matrix to reflect the updated 
          camera orientation.

        * Camera Movement: The move method processes key inputs for camera movement, 
          adjusting the camera's position based on the pressed keys.

        * View and Projection Matrix Generation: The get_view_matrix and 
          get_projection_matrix methods compute the view and projection 
          matrices, respectively, using the camera's position, orientation, 
          and specified parameters (e.g., field of view, near, and far planes).

        * Camera Movement Speed and Sensitivity: The camera movement speed (SPEED) 
          and mouse sensitivity (SENSITIVITY) are constants defined outside the class.
    """

    # Constructor
    def __init__(self, app, position=(0, 0, 4), yaw=-90, pitch=0):

        # Reference to the application
        self.app = app

        # Aspect ratio of the window
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]

        # Initial camera position, orientation, and vectors
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)

        # Initial yaw and pitch angles
        self.yaw = yaw
        self.pitch = pitch

        # View matrix
        self.m_view = self.get_view_matrix()

        # Projection matrix
        self.m_proj = self.get_projection_matrix()

    # Method to handle rotation based on mouse movement
    def rotate(self):

        rel_x, rel_y = pg.mouse.get_rel()
        self.yaw += rel_x * SENSITIVITY
        self.pitch -= rel_y * SENSITIVITY

        # Ensure pitch stays within reasonable bounds
        self.pitch = max(-89, min(89, self.pitch))

    # Method to update camera vectors based on yaw and pitch
    def update_camera_vectors(self):

        # Convert yaw and pitch to radians for trigonometric calculations
        yaw, pitch = glm.radians(self.yaw), glm.radians(self.pitch)

        # Update the forward vector based on yaw and pitch
        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        # Normalize vectors to ensure they have unit length
        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(0, 1, 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    # Method to update the camera (called in the game loop)
    def update(self):

        # Move the camera based on user input
        self.move()

        # Rotate the camera based on mouse movement
        self.rotate()

        # Update the camera orientation vectors based on yaw and pitch
        self.update_camera_vectors()

        # Update the view matrix to reflect the new camera position and orientation
        self.m_view = self.get_view_matrix()

    # Method to handle camera movement based on key inputs
    def move(self):

        # Calculate the camera movement velocity based on the predefined speed and delta time
        velocity = SPEED * self.app.delta_time

        # Get the current state of all keys to check for user input
        keys = pg.key.get_pressed()

        # Update camera position based on pressed keys
        if keys[pg.K_w]:  # Move forward (along the camera's forward vector)
            self.position += self.forward * velocity

        if keys[pg.K_s]:  # Move backward (opposite to the camera's forward vector)
            self.position -= self.forward * velocity

        if keys[pg.K_a]:  # Move left (along the camera's right vector)
            self.position -= self.right * velocity

        if keys[pg.K_d]:  # Move right (opposite to the camera's right vector)
            self.position += self.right * velocity

        if keys[pg.K_q]:  # Move up (along the camera's up vector)
            self.position += self.up * velocity

        if keys[pg.K_e]:  # Move down (opposite to the camera's up vector)
            self.position -= self.up * velocity


    # Method to get the view matrix
    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    # Method to get the projection matrix
    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)
