import pygame

from sys import exit


white = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
X = 800
Y = 400


pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('game')

clock = pygame.time.Clock()

sky_surface = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\snowymountains.png')

ground_surface = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\iceGround.jpg')  
snowy_ground = pygame.transform.scale(ground_surface, (800,300))


intro_screen = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\Lone Freeman.png')  # Intro screen image

font = pygame.font.Font('freesansbold.ttf',32)            # Font
endfont = pygame.font.Font('freesansbold.ttf', 100)       # Font for the game over screen
toptext = font.render('The Lone Freeman', True, red, blue)  # Top text for the intro screen
bottomtext = font.render('Press space to start', True, red, blue)   # Bottom text for the intro screen
textRect = toptext.get_rect()  # Creates a space for the top text for the intro screen to go
textRect.center = ( X//2, Y//2)

textRect2 = bottomtext.get_rect()  # Creates a space for the bottom text for the intro screen to go
textRect2.center = (X//2, Y + 100)

screen.blit(intro_screen, (-500, 0))    # Sets the intro screen's background
screen.blit(toptext, textRect)          # Top text for the intro screen
    
screen.blit(bottomtext, textRect2)      # Bottom text for the intro screen


game_over = pygame.image.load(r'C:\Users\VoegleSR23\Downloads\Game over.png')   # Sets the game over screen's background

over_game = pygame.transform.scale(game_over, (800,800))   # Rescales the game over screen's background image

endtext = endfont.render('GAME OVER', True, white, red)  # Game over screen top text
restart = font.render('Press space to restart', True, white, black)  # Game over screen bottom text
restartRect = restart.get_rect()
restartRect.center = (X//2, Y + 100)
endtextRect = endtext.get_rect()
endtextRect.center = (X//2, Y//2)

pygame.mixer.music.load('Devious Little Smile.mp3')  # Intro music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    if pygame.key.get_pressed()[pygame.K_SPACE] == True:  # Changes from the intro screen to the main game screen when space is pressed, or from the game over screen to the main game screen, depending on the order
        
        screen.blit(sky_surface, (0, -250))
        screen.blit(snowy_ground, (0,730))
        pygame.display.update()
        
        pygame.mixer.music.load('Giveup.mp3')
        pygame.mixer.music.set_volume(0.2)   # Thumping was a bit loud so I had to readjust the volume
        pygame.mixer.music.play()
    if pygame.key.get_pressed()[pygame.K_CAPSLOCK] == True:  # Supplement for however the real game over will be, for now it's accessed by pressing Caps Lock
        screen.blit(over_game, (0, 0))
        screen.blit(endtext, endtextRect)
        screen.blit(restart, restartRect)
        
        pygame.display.update()
        pygame.mixer.music.load('Torture.mp3')   # Literally torturous to the ears, quite fitting for a game over screen
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play()
    if pygame.key.get_pressed()[pygame.K_r] == True:  # Stops the music, especially useful if you don't want to be tortured anymore
        pygame.mixer.music.pause()
    pygame.display.update()
    clock.tick(60)
    
    
