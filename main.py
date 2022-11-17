# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random

vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -5
            # print(self.vel)
        if keys[pg.K_RIGHT]:
            self.acc.x = 5
    def update(self):
        self.acc = vec(.1*random.choice([-1,1]),.1*random.choice([-1,1]))
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos

    class Platform(Sprite):
        def __init__(self):
         self.image = pg.surface


        
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()

# instantiate the player class
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 100, 35)

# add player to all sprites group
all_sprites.add(player)
all_sprites.add(plat)


# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
    screen.fill(BLACK)
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()