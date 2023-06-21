import pygame

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

#displayRaster
pygame.display.set_caption('A Beautiful Sunset')
done = False

#load background image
background = pygame.image.load('images/background.png')
sprite = pygame.image.load('images/Bird-blue-icon.png')
while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            done = True
    screen.blit(background, (0, 0))
    screen.blit(sprite, (100, 100))
    pygame.display.update()
pygame.quit()