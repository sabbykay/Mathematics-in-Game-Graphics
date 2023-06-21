import pygame

pygame.init()
screen_width = 1000
screen_height = 200
screen = pygame.display.set_mode((screen_width,screen_height))

done = False
white = pygame.Color(255, 255, 255)

pygame.font.init()
font = pygame.font.Font('Beautiful Marry.otf',
                        120)
text = font.render('DADDYSABBY96', False, white)
while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            done = True
        screen.blit(text, (0.2, 0.2))
    pygame.display.update()
pygame.quit()