from pygame import *
from random import randint
from time import time as timer

window = display.set_mode((700, 500))
display.set_caption("CheckPong")
size_y = 500
size_x = 700
backround = transform.scale(image.load("background.png"), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.dx = 2
        self.dy = 2
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

class Ball(GameSprite):     
    def update(self):
        pass
player_1 = Player("player.png", 15, size_y-250, 15, 65, 10)
player_2 = Player("player.png", size_x-30, size_y-250, 15, 65, 10)
ball = Ball("ballon.png", size_x/2-25, size_y-250, 50, 50, 10)


mixer.init()
# mixer.music.load("2.mp3")
# mixer.music.play()  

score = 0
lose_counter = 0

font.init()
font = font.SysFont(None, 70)
# win = font.render('YOU WIN!', True, (94,204,0))
# lose = font.render('YOU LOSE!', True, (204,0,0))

# count = font.render(f'Счет: {score}', True, (255,255,255))
# loss = font.render(f'Пропущено: {lose_counter}', True, (255,255,255))

# kick = mixer.Sound('fire.ogg') 

finish = False

game = True

from time import sleep

while game:
        # if len(player.bullets_) > 0:
        #     for i in player.bullets_:
        #         i.reset()
        #         i.update()

    for e in event.get():
        if e.type == QUIT:
            game = False
        
        # elif e.type == KEYDOWN and e.key == K_SPACE:
        #     if num_fire < 5 and not rel_time:
        #         num_fire += 1 
        #         kick.play()
        #         player.fire()
        #     if num_fire >= 5 and not rel_time:
        #         last_time =  timer()
        #         rel_time = True
    if finish != True:
        window.blit(backround, (0, 0))
        # text_life = font.render(f'Жизни: {str(life)}', 1, (255,255,255))
        # window.blit(text_life, (10, 120))
        # loss = font.render(f'Пропущено: {lose_counter}', True, (255,255,255))
        # count = font.render(f'Счет: {score}', True, (255,255,255))  
        # window.blit(count, (10, 10))
        # window.blit(loss, (10, 60))
        # monsters.update()
        player_1.update_left()
        player_1.reset()
        player_2.update_right()
        player_2.reset()
        ball.update()
        ball.reset()
        # if rel_time:
        #     now_time = timer()

        #     if now_time - last_time > 3:
        #         pass
        #     else:
        #         num_fire = 0
        #         rel_time = False

        # colides = sprite.groupcollide(monsters, bullets, True, True)
        # for c in colides:
        #     score +=1
        #     monster = Enemy("ufo.png", randint(80, size_x - 80), -40, 80, 50, randint(5,10))
        #     monsters.add(monster)

        # if sprite.spritecollide(player, asteroids, True) or sprite.spritecollide(player, monsters, True):
        #     life -= 1
        # if score >= 15:
        #     window.blit(win, (50, 50))
        #     finish = True
        # elif lose_counter >= 15 :
        #     window.blit(lose, (50, 50)) 
        #     finish = True
        # elif life <= 0 :
        #     window.blit(lose, (50, 50)) 
        #     finish = True

        display.update()
    else :
        finish = False
        score = 0
        life =3
        # for b in bullets :
        #     b.kill()
        # for m in monsters :
        #     m.kill()
        # for a in asteroids :
        #     a.kill()
        
        time.delay(3000)

        # for i in range(1, 6):
        #     monster = Enemy("ufo.png", randint(80, size_x - 80), -40, 80, 50, randint(5,10))
        #     monsters.add(monster)

        # for i in range(1, 6):
        #     asteroid = Enemy("asteroid.png", randint(80, size_x - 80), -40, 80, 50, 2)
        #     asteroids.add(asteroid)   

    time.delay(30)
