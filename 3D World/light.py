import glm


class Light:

    """
    represents a light source in the graphics 
    application. Below is a summary of its key 
    functionalities:

        * Constructor: The constructor initializes a 
        light source with specified properties. It 
        takes parameters such as the initial position 
        (position) and color (color). The light source 
        has ambient (Ia), diffuse (Id), and specular (Is) 
        intensities. The view matrix (m_view_light) is 
        calculated using the get_view_matrix method.

        * View Matrix Calculation: The get_view_matrix method 
        calculates and returns the view matrix for the light 
        source. It uses the glm library's lookAt function to 
        create a view matrix based on the light's position, 
        direction, and an up vector.
    """

    def __init__(self, position=(50, 50, -10), color=(1, 1, 1)):
        self.position = glm.vec3(position)
        self.color = glm.vec3(color)
        self.direction = glm.vec3(0, 0, 0)
        # intensities
        self.Ia = 0.06 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
        # view matrix
        self.m_view_light = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.direction, glm.vec3(0, 1, 0))