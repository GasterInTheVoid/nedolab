from pygame import *

screen = display.set_mode((700,500))
display.set_caption("MY FIRST GAME")

player_image = 'Hero.png'

back = (0, 255, 255)
screen.fill(back)
run = True

win_width = 700
win_hight = 500

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x,self.rect.y))



finish = False

class Heroes(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
        self.x_speed = 0
        self.y_speed = 0
    def update(self):
        if Main_Hero.rect.x <= win_width-50 and Main_Hero.x_speed > 0 or Main_Hero.rect.x >= 0 and Main_Hero.x_speed <0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if Main_Hero.rect.y <= win_hight-50 and Main_Hero.y_speed > 0 or Main_Hero.rect.y >= 0 and Main_Hero.y_speed < 0:
            self.rect.y += self.y_speed
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)


class Enemy(GameSprite):
    def __init__(player_image, player_x, player_y, size_x, size_y, speed, direction, max_y, min_y):
        super().__init__(player_image, player_x, player_y, size_x, size_y)
    def update(self):
        direction = 'up'
        if direction == 'up' and self.player_y >= max_y:
            self.rect.y += self.speed
            direction = 'down'
        if direction == 'down' and self.player_y <= min_y:
            self.rect.y -= self.speed
            direction = 'up'


game_over = transform.scale(image.load('thumb.jpg'),(700,500))
Main_Hero = Heroes(player_image,0,380,50,50)
wall1 = GameSprite('platform_v.png', 150, 255,30,250)
wall2 = GameSprite('platform_h.png', -5, 125,250,30)
wall3 = GameSprite('platform_v.png', 550,-5,30,250)
wall4 = GameSprite('platform_h.png', 306, 215 ,250,30)

Evil = GameSprite('enemy.png', 135, 190, 75,75)
Evil2 = GameSprite('enemy.png', 450, 275, 150,150)
Evil3 = GameSprite('enemy.png', 300, 325, 150,150)
final_pic = GameSprite('Final.png',615,0,50,60)

VRAGINI = sprite.Group()
VRAGINI.add(Evil)
VRAGINI.add(Evil2)
VRAGINI.add(Evil3)

barriers = sprite.Group()
barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_w:
                Main_Hero.y_speed -= 10
            if e.key == K_s:
                Main_Hero.y_speed += 10
            if e.key == K_a:
                Main_Hero.x_speed -= 10
            if e.key == K_d:
                Main_Hero.x_speed += 10
        if e.type == KEYUP:
            if e.key == K_w:
                Main_Hero.y_speed = 0
            if e.key == K_s:
                Main_Hero.y_speed = 0
            if e.key == K_a:
                Main_Hero.x_speed = 0
            if e.key == K_d:
                Main_Hero.x_speed = 0
    if finish != True:
        Evil.reset()
        Evil2.reset()
        Evil3.reset()
        Evil.update()
        Evil2.update()
        Evil3.update()
        VRAGINI.update()
        final_pic.reset()
        barriers.draw(screen)
        Main_Hero.update()
        Main_Hero.reset()
    if sprite.collide_rect(Main_Hero, final_pic) == True:
            finish = True
            screen.blit(game_over,(0,0))
    time.delay(50)
    display.update()
    screen.fill(back)


