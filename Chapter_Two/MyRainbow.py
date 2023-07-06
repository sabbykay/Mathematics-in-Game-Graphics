import pygame
import math

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
width = 800
height = 400

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rainbow Pixels")

# Set up colors
colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the rainbow pixels
    num_colors = len(colors)
    pixel_width = width / num_colors

    for i in range(num_colors):
        x = i * pixel_width
        color = colors[i]
        pygame.draw.rect(screen, color, (x, 0, pixel_width, height))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
