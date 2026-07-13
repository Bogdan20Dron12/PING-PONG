from pygame import *

class GameSprate(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, width, height, player_speed):
        super(). __init__()
        self.width = width
        self.height = height
        self.image = transform.scale(image.load(player_image), (self.width, self.height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprate):
    def update_left(self):
        keys_pressed =  key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and  self.rect.y < 350:
            self.rect.y += self.speed
    def update_right(self):
        keys_pressed =  key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and  self.rect.y < 350:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
window.fill((200, 255, 255))

racket_left = Player('racket.png', 30, 200, 50, 150, 4)
racket_right = Player('racket.png', 615, 200, 50, 160, 4)
ball = GameSprate('tenis_ball.png', 200, 200, 50, 50, 5)
font.init()
font = font.Font(None, 70)
loose_1 = font.render('PLAYER 1 LOOSER!!!', True, (255, 0, 0))
loose_2 = font.render('PLAYER 2 LOOSER!!!', True, (255, 0, 0))

speed_x = 5
speed_y = 5
clock = time.Clock()
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.fill((200, 255, 255))
        racket_left.update_left()
        racket_right.update_right()
        racket_left.reset()
        racket_right.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_left, ball) or sprite.collide_rect(racket_right, ball):
            speed_x *= -1
        ball.reset()
        if ball.rect.x < 0:
            finish = True
            window.blit(loose_1, (200, 200))
        if ball.rect.x > 650:
            finish = True
            window.blit(loose_2, (200, 200))    

    display.update()
    clock.tick(60)    