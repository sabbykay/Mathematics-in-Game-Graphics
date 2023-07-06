import pygame

pygame.init()
screen_width = 1000
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

done = False
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)

pygame.font.init()
font = pygame.font.Font('Beautiful Marry.otf', 80)
font2 = pygame.font.Font('Beautiful Marry.otf', 80)
text = font.render('DADDYSABBY96', False, white)
text2 = font.render('Just Kidding', False, red)
while not done:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            done = True
    x = (screen_width - text.get_width()) / 2
    y = (screen_height - text.get_height()) / 2
    screen.blit(text, (x, y))
    screen.blit(text2, (10, 10))
    pygame.display.update()
pygame.quit()