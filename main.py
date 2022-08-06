import os
import pygame 
import random

game_Folder = os.path.dirname(__file__)
img_folder = os.path.join(game_Folder,"img")
player_img = pygame.image.load(os.path.join(img_folder, "normal_Bird.png")).convert_alpha

WIDTH = 1280
HEIGHT = 720
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# initialize pygame and create window
pygame.display.set_caption("Shotty Bird")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
color = (233,220,201)
screen.fill(color)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update(self):
        self.rect.y += 5
        if self.rect.bottom > WIDTH:
            self.rect.top = 0
# Game loop
pygame.sprite.Group = all_sprites
Player = Player()
all_sprites.add(Player)
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(color)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()
    all_sprites.update()

pygame.quit()
