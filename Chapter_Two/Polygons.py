import pygame

pygame.init()

screen_width = 1000
screen_heigth = 800

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption("Polygons")
done = False

white = pygame.Color(255, 255, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.polygon(screen, white, ((150, 200),(600, 400),(400, 600)))
    pygame.display.update()
pygame.quit()