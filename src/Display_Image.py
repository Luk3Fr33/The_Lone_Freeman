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
sky_surface = pygame.image.load(r'C:\Users\ebay1\Desktop\The_Lone_Freeman\img\snowymountains.png')
# Image imported and had to be transformed because of size
# new variable is snowy_ground
groud_surface = pygame.image.load(r'C:\Users\ebay1\Desktop\The_Lone_Freeman\img\ice_Ground.jpg')
snowy_ground = pygame.transform.scale(groud_surface, (800,300))

# allows for the screen to constantly display unless the screen is closed
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # The test surface is displayed at the exact pixels entered
    # Pixels in pygame start at the top left at (0,0) like looking at a fourth quadrant
    screen.blit(sky_surface,(0,-250))
    # You need to put the sky before the ground or it will print over it
    screen.blit(snowy_ground,(0,730))

    pygame.display.update()
    # Updates the clock to 60 frames per seconds
    # Makes sure the game dosent run too fast
    clock.tick(60)