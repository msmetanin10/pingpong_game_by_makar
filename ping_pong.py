from pygame import *
from random import *
from time import time as AndreiSpidranTaimerPravda

img_back = "background.jpg"
img_player = "palka.png"
img_ball = "eto_miach!!!!!!!!Pravda12345%.png"

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def updatel(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def updater(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        pass
        
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("ping pong game pravda 102%")

background = transform.scale(image.load(img_back), (win_width,win_height))
window.blit(background,(0,0))

playerl = Player(img_player,30,win_height - 270,10,150,5)
playerr = Player(img_player,win_width - 35,win_height - 270,10,150,5)

font.init()
font1 = font.SysFont('Arial',70)
win_text = font1.render('YOU WIN!', True, (255,215,0))

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_r and finish == True:
                #PEREZAPUSK!!!
                finish = False

    if finish != True:
        window.blit(background,(0,0))

        playerl.updatel()
        playerr.updater()

        playerl.reset()
        playerr.reset()

        display.update()
    clock.tick(FPS)