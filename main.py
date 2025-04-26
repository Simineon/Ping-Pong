from pygame import *
from random import *

win_width = 800
win_height = 600
window = display.set_mode((win_width, win_height), flags=RESIZABLE)
display.set_caption("Звёздные войны в Китае")
backgr = transform.scale(image.load("stalin.jpg"), (800, 600))

player_image = "roketka1.png"
fps = 60
clock = time.Clock()


# класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (70, 90))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)

    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if key_pressed[K_s] and self.rect.y < 500:
            self.rect.y += 10


class Enemy(GameSprite):
    def update(self):
        self.rect.y += randint(1, 4)
        if self.rect.y > 600:
            self.rect.y = 0
            self.rect.x = randint(0, 700)

player = Player(player_image, 50, 400, 5)

pt = True
while pt:
    clock.tick(fps)
    window.blit(backgr, (0, 0))
    player.reset()
    player.move()

    for e in event.get():
        if e.type == QUIT:
            pt = False

    display.update()