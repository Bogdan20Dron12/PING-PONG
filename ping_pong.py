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
        if keys_pressed[K_s] and  self.rect.y < 610:
            self.rect.y += self.speed
    def update_right(self):
        keys_pressed =  key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and  self.rect.y < 610:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
display.set_caption('Пинг-Понг')
window.fill((200, 255, 255))

clock = time.Clock()
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        
    
    
    display.update()
    clock.tick(60)    
