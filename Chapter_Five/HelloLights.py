import pygame

from Mesh3D import *
from MeshCube import *
from pygame.locals import * 
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255, 255, 255)
glMatrixMode(GL_PROJECTION)
gluPerspective(30, (screen_width // screen_height), 0.1, 100.0)
# glOrtho(-1, 1, 1, -1, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -3.0)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)

glLight(GL_LIGHT0, GL_POSITION, (5, 5, 5, 1))
glLightfv(GL_LIGHT0, GL_AMBIENT, (1, 0, 1, 1))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 0, 0, 1))
glLightfv(GL_LIGHT0, GL_SPECULAR, (0, 1, 0, 1))
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0, 1, 0, 1))

glEnable(GL_LIGHT0)

mesh = Cube(GL_POLYGON, "pexels-george-chambers-16317911.jpg")

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