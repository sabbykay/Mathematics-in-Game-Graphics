import pygame.image
from OpenGL.GL import *

class Mesh3D:
    def __init__(self):
        self.vertices = [(0.5, -0.5, 0.5),
                         (-0.5, -0.5, 0.5),
                         (0.5, 0.5, 0.5),
                         (-0.5, 0.5, 0.5),
                         (0.5, 0.5, -0.5),
                         (-0.5, 0.5, -0.5)]

        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        self.texture = pygame.image.load("Images/pexels-george-chambers-16317911.jpg")
        self.texID = 0
        self.normal_color = (1.0, 1.0, 1.0)

    def draw(self):
        glPushMatrix()
        glLoadIdentity()
        glColor3f(self.normal_color[0], self.normal_color[1], self.noraml_color[2])
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texID)
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glTexCoord2fv(self.uvs[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t]])
            glTexCoord2fv(self.uvs[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glTexCoord2fv(self.uvs[self.triangles[t + 2]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)

    def load_drawing(self, filename):
        vertices = []
        triangles = []
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for 
                                  value in 
                                  line[2:].split()]
                    vertices.append((vx, vy, vz))
                if line[:2] == "f ":
                    t1, t2, t3 = [value for value in
                                  line[2:].split()]
                    triangles.append(
                        [int(value) for value in
                         t1.split('/')][0] - 1)
                    triangles.append(
                        [int(value) for value in
                         t2.split('/')][0] - 1)
                    triangles.append(
                        [int(value) for value in
                         t3.split('/')][0] - 1)
                line = fp.readline()
        return vertices, triangles

    def int_texture(self):
        self.texID = glGenTextures(1)
        textureData = pygame.image.tostring(self.texture, "RGB", 1)
        width = self.texture.get_width()
        height = self.texture.get_height()
        glBindTexture(GL_TEXTURE_2D, self.texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, textureData)