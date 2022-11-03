# content from kids can code: http://kidscancode.org/blog/

# sources
# getting mouse position: https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos
# shorthand for loops (used in getting mouse collision with sprite): https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable

#  design
'''
Innovation:

Fire projectile from player
If health hits 0 game ends 
Mob count 

Goal: destroy all mobs without running out of health

Rules: 
shoot: space bar 
move: wsad 
jump: space 

Don't run out of health 

Fredoms: 
Move and jump around whenever and where ever within the map
Game does not end after all mobs are killed
No limit to how long you can play 
You do not have to kill all the Mobs

Goals rules feedback freedom!!!


'''

# import libraries and modules
# from platform import platform
from ast import Break
from turtle import width
import pygame as pg
# import settings
# sdyguiew
from settings import *
from pygame.sprite import Sprite
import random
from random import randint

# defines the vectors that help control the player sprite 
vec = pg.math.Vector2

# weufyh
# game settings 
WIDTH = 660
HEIGHT = 660
FPS = 30
mpos = (0,0)

# fps refresh rate of sprites and systems

# player settings
PLAYER_GRAV = 0.9
PLAYER_FRIC = 0.1


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# prints text on the video game box defines color location 

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)
# defines the random colors for mobs players
def colorbyte():
    return random.randint(0,255)

# sprites... how pygame works and uses different classes to do different things within the game 
# init self defines how the player sprite moves and what it looks like on the screen 
# controls how the player moves the player sprite 
# the update part constantly updates the player movement and how they move 
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.r = 0
        self.g = 0
        self.b = 255
        self.image.fill((self.r,self.g,self.b))
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(660,660)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 5
    def controls(self):
        keys = pg.key.get_pressed()
        # if keys[pg.K_w]:
        #     self.acc.y = -5
        if keys[pg.K_a]:
            self.acc.x = -1
        # if keys[pg.K_s]:
        #     self.acc.y = 5
        if keys[pg.K_d]:
            self.acc.x = 1
    def jump(self):
        self.rect.x += 0.5
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -0.5
        if hits:
            self.vel.y = -15
    def draw(self):
        pass
    def inbounds(self):
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        # self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.inbounds()
        self.rect.midbottom = self.pos

# platforms width height color and location on the game and defines funtcions of the platforms 
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
# projectiles what the actual projectiles do and how they move and update is how they move 
# if loops for when they move past the barries of the game it removes them or kills them 
class Pewpew(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def update(self):
        self.rect.y -= self.speed
        if (self.rect.y < 0):
            self.kill()
            print(pewpews)

# mob the enemy class against the player sprite 
# update talks about movement right to left and when it hits a barrier and moves side to side 
class Mob(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
    def update(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH or self.rect.x < 0:
            self.speed *= -1
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
pewpews = pg.sprite.Group()

# instantiate classes and where we define the locations of the plats 
player = Player()
plat = Platform(180, 380, 100, 35)
plat2 = Platform(289, 180, 100, 35)
plat3 = Platform(500,400,200,45)
plat4 = Platform(50, 480, 130, 45)
plat5 = Platform(70,300, 120,35)
ground = Platform(0, HEIGHT-40, WIDTH, 40)

# spawns the mobs at random locations and with random colors under 550 on they y axis so they don't spawn on top of the player 
# and kill him instantly for unfair game play 
for i in range(45):
    m = Mob(randint(0,WIDTH), randint(0,550), 25, 25, (colorbyte(),colorbyte(),colorbyte()))
    all_sprites.add(m)
    mobs.add(m)
    print(m)
print(mobs)

# add things to groups...
all_sprites.add(player, plat, plat2, plat3, plat4, plat5, ground)
all_plats.add(plat, plat2, plat3, plat4, plat5, ground)

# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)

    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
    # what happens when projectiles collide with mobs it kills them and when they hit plats and kills the projectiles 
    pewpewhits = pg.sprite.groupcollide(pewpews, mobs, True, True)
    pewpewhplat = pg.sprite.groupcollide(pewpews, all_plats, True, False)
# takes health from player when mobs collide with player sprite 
    mobhits = pg.sprite.spritecollide(player, mobs, True)
    if mobhits:
        player.health -= 1
        if player.r < 255:
            player.r += 15 

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
        # check for mouse and control shooting 
        if event.type == pg.MOUSEBUTTONUP:
            p = Pewpew(player.rect.midtop[0], player.rect.midtop[1], 10, 10)
            all_sprites.add(p)
            pewpews.add(p)
            mpos = pg.mouse.get_pos()
            print(mpos)
            

            # print(clicked_sprites)k 
        # check for keys
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                player.jump()
        
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
      
    screen.fill(BLACK)
    # screen.fill(BLACK)

    # draw text
    draw_text("HEALTH: " + str(player.health), 22, WHITE, WIDTH / 2, HEIGHT / 10)
    draw_text("Mobs left: " + str(mobs), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    # pg.draw.polygon(screen,BROWN,[(player.rect.x, player.rect.y), (152, 230), (1056, 230),(1056, 190)])
    
    # draw player color
    player.image.fill((player.r,player.g,player.b))

    
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()
    if player.health == (0) :
        print ("GAME OVER")
        break
    

pg.quit()