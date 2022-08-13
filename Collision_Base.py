# Luke Freeman
# 08/04/22
# Pygame Collision Program

import pygame
from sys import exit

# Function for the moving rectangle
def bouncing_rect():
    global x_speed, y_speed, other_speed

    # Speed of the moving rectangle
    # Assigned from the x and y speed variables in line 25
    moving_rect.x += x_speed
    moving_rect.y += y_speed

    # Collision with screen borders
    if moving_rect.right >= screen_width or moving_rect.left <=0:
        x_speed *= -1
    if moving_rect.bottom >=screen_height or moving_rect.top <=0:
        y_speed *= -1

    # Moving the other rectangle
    other_rect.y += other_speed
    if other_rect.top <= 0 or other_rect.bottom >= screen_height:
        other_speed *= -1

    #Collision with rectangle
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) < collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) < collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) < collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.left - moving_rect.left) < collision_tolerance and x_speed > 0:
            x_speed *= -1
        

    # drawing the rectangle above the screen and the color of the rectangle
    pygame.draw.rect(screen, (255,255,255), moving_rect)
    pygame.draw.rect(screen, (100,100,200), other_rect)


pygame.init()

screen_width,screen_height = 800,800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('game')
clock = pygame.time.Clock()

moving_rect = pygame.Rect(350,350,100,100)
x_speed, y_speed = 5,4

other_rect = pygame.Rect(300,600,200,100)
other_speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((30,30,30))
    # Calling function from line 9
    bouncing_rect()
    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)