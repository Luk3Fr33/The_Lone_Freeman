# Luke Freeman
# 08/01/22
# Pygame Base Program

# Sys module is needed for closing pygame without throwing an error for conflicting statements
import pygame
from sys import exit

# Pygame Init is nessecery for pygame to run correctly
pygame.init()

# Creates a screen by 800x800
# The screen starts at the top left at the cords (0,0)
screen = pygame.display.set_mode((800,800))
# Set the caption of the display
pygame.display.set_caption('game')
# Ties the framerate to the clock
clock = pygame.time.Clock()

# Smaller display surface made on the orginal display or the screen variable
# The pixel size at 100xp is made out to the right, and 200xp is made down
# Or made from the fourth quadrat of a normal 2d graph
test_surface = pygame.Surface((100,200))
# Colors the test surface
test_surface.fill('Red')

# allows for the screen to constantly display unless the screen is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # The test surface is displayed at the exact pixels entered
    # Pixels in pygame start at the top left at (0,0) like looking at a fourth quadrant
    screen.blit(test_surface,(200,100))

    pygame.display.update()
    # Updates the clock to 60 frames per seconds
    # Makes sure the game dosent run too fast
    clock.tick(60)