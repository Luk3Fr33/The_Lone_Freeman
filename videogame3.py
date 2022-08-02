import pygame

from sys import exit


pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('game')

clock = pygame.time.Clock()

sky_surface = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\snowymountains.png')

ground_surface = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\iceGround.png')  # This line doesn't work for some reason
snowy_ground = pygame.transform.scale(ground_surface, (800,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, -250))
    screen.blit(snowy_ground, (0,730))
    pygame.display.update()

    clock.tick(60)
