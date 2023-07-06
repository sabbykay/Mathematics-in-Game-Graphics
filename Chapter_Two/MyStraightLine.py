import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

# Set up OpenGL perspective
glViewport(0, 0, width, height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, width / height, 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)

# Set up line coordinates
line_start = (-0.5, -0.5, 0.0)
line_end = (0.5, 0.5, 0.0)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen and set up 3D drawing
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Draw the line
    glBegin(GL_LINES)
    glVertex3fv(line_start)
    glVertex3fv(line_end)
    glEnd()

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
