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
        
win_width = 700
win_height = 500
window = display.set_mode((win_width,win_height))
display.set_caption("ping pong game pravda 102%")

background = transform.scale(image.load(img_back), (win_width,win_height))
window.blit(background,(0,0))

ball = GameSprite(img_ball,324,224,50,50,3)

playerl = Player(img_player,30,win_height - 270,10,150,5)
playerr = Player(img_player,win_width - 35,win_height - 270,10,150,5)

font.init()
font1 = font.Font(None,35)
lose_text_l = font1.render('PLAYER 1 LOSE!', True, (255,0,0))
lose_text_r = font1.render('PLAYER 2 LOSE!', True, (255,0,0))

speed_x = 3
speed_y = 3

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
                speed_x = 3
                speed_y = 3
                ball.rect.x = 324
                ball.rect.y = 224
                playerl.rect.y = win_height - 270
                playerr.rect.y = win_height - 270
                finish = False

    if finish != True:
        window.blit(background,(0,0))

        playerl.updatel()
        playerr.updater()

        if ball.rect.y >= win_height-50 or ball.rect.y <= 0:
            speed_y *= -1.1
            if speed_y > 50:
                speed_y = 50
            if speed_y < -50:
                speed_y = -50

        if ball.rect.x <= 0:
            finish = True
            window.blit(lose_text_l,(200,200))
        if ball.rect.x >= win_width-50:
            finish = True
            window.blit(lose_text_r,(200,200))

        if sprite.collide_rect(ball,playerl) or sprite.collide_rect(ball,playerr):
            speed_x *= -1.1
            if speed_x > 50:
                speed_x = 50
            if speed_x < -50:
                speed_x = -50

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        playerl.reset()
        playerr.reset()
        ball.reset()

        display.update()
    clock.tick(FPS)