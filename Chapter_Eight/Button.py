import pygame.mouse
from OpenGL.GL import *
from Utils import map_value
from pygame.locals import *
from Settings import window_dimensions, gui_dimensions

class Button:
    def __init__(self, screen, position, width, height, color, o_color, p_color, on_click):
        self.screen = screen
        self.position = position
        self.width = width
        self.height = height
        self.normal_color = color
        self.over_color = o_color
        self.pressed_color = p_color
        self.on_click = on_click
        self.mouse_down = False
    
    def draw(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mx = map_value(0, 800, 0, 1600, mouse_pos[0])
        my = map_value(0, 600, 1200, 0, mouse_pos[1])
        glPushMatrix()
        glLoadIdentity()
        # if mouse over button
        if self.position[0] < mx < (self.position[0] + self.width) and \
            self.position[1] < my < (self.position[1] + self.height):
            for e in events:
                if e.type == MOUSEBUTTONDOWN and e.button == 1:
                    self.mouse_down = True
                    self.on_click()
                elif e.type == MOUSEBUTTONUP and e.button == 1:
                    self.mouse_down = False
                    if self.mouse_down:
                        glColor3f(self.pressed_color[0], self.pressed_color[1], self.pressed_color[2])
                else:
                    glColor3f(self.over_color[0], self.over_color[1], self.over_color[2])
            else:
                glColor3f(self.normal_color[0], self.normal_color[1], self.normal_color[2])
                glBegin(GL_POLYGON)
                glVertex2f(self.position[0], self.position[1])
                glVertex2f(self.position[0] + self.width, self.position[1])
                glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
                glVertex2f(self.position[0], self.position[1] + self.height)
                glEnd()
            glPopMatrix()