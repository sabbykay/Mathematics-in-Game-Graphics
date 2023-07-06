import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
#Add a title to the display window
pygame.display.set_caption("A Beautiful Sunset")
done = False

# Load background image
background_image = pygame.image.load("Images/pexels-simon-berger-1323550.jpg")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load the sprite image
sprite_image = pygame.image.load("Images/angry-bird-icon.png")

# Set the initial position of the sprite
sprite_x = 100
sprite_y = 100

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background image
    screen.blit(background_image, (0, 0))
    screen.blit(sprite_image, (100, 100))

    # Draw the sprite
    screen.blit(sprite_image, (sprite_x, sprite_y))

    # Update the display
    pygame.display.update()

pygame.quit()
