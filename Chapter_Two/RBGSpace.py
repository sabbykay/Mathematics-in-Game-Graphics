import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            done = True
        for y in range(800) :
            for x in range(1000) :
                screen.set_at((x, y),
                    pygame.Color(0, int(x/1000 * 255) ,
                        int(y/800 * 255)))
    pygame.display.update()
pygame.quit()