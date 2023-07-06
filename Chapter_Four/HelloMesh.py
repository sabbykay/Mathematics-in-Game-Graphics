import pygame

from Mesh3D import *
from MeshCube import *
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
gluPerspective(90, (screen_width / screen_height), 0.1, 100.0)
vertical_fov = 80
glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glTranslatef(0.0, 0.0, -3)
mesh = Cube()

while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(5, 1, 0, 1)
    mesh.draw()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
