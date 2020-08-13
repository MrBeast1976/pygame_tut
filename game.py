import pygame, sys, random
from pygame import mixer
import os
import pygame.image
pygame.init()
mixer.init()
width = 800
height = 600
score = 0

win = pygame.display.set_mode((width, height))

ability = open('ability.txt', 'r')
super = ability.read()
ability.close()
pygame.display.set_caption("The Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 35)
class Player():
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = (x, y, size,size)
        self.vel = 10
        file = open('skin.txt', 'r')
        self.skin = int(file.read())
        file.close()
        file = open('ability.txt', 'r')
        ability = int(file.read())
        file.close()
        z = 0
        while z < ability:
            self.vel += 5
            z += 1

    def draw(self):
        if self.skin  == 1:
            self.color = (128,0,128)
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel



        self.rect = (self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, self.rect)
class enemy():
    def __init__(self, x, y, color, size):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.rect = (x, y, size,size)
        self.vel = 10
    def draw(self):
        pygame.draw.rect(win, self.color, self.rect)
    def move(self, score):
        self.y += self.vel
        self.rect = (self.x, self.y, self.size, self.size)
        pygame.draw.rect(win, self.color, self.rect)
        if score >= 100:
            self.vel = 25

        if score >= 200:
            self.vel = 30

        if score >= 300:
            self.vel = 35

        if score >= 400:
            self.vel = 40
        if score >= 500:
            self.vel = 1000

def redrawWindow(win, Player, enemylist=[]):

    win.fill((0,0,0))
    Player.draw()
    for enemys in enemylist:
        enemys.draw()

    pygame.display.update()

def collisioncheck(a, b, c, d, e, g, h, i, j, k, p):
    lst = [a, b, c, d, e, g, h, i, j, k]
    y = False
    for enem in lst:
        if (enem.x >= p.x and enem.x < (p.x + 50)) or (p.x >= enem.x and p.x < (enem.x + 50)):
            if (enem.y >= p.y and enem.y < (p.y + 50)) or (p.y >= enem.y and p.y < (enem.y + 50)):
                y = True
    return y

def mainloop(score):

    p = Player(370, 550, (0,255,0), 50)
    a = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    b = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    c = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    d = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    e = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    g = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    h = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    i = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    j = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    k = enemy(random.randint(0, 750), random.randint(-1150, 0), (0,0,255), 50)
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        redrawWindow(win, p, [a, b, c, d, e, g, h, i, j, k])
        p.move()
        a.move(score)
        b.move(score)
        c.move(score)
        d.move(score)
        e.move(score)
        g.move(score)
        h.move(score)
        i.move(score)
        j.move(score)
        k.move(score)
        allenemy = [a, b, c, d, e, g, h, i, j, k]
        for enemies in allenemy:
            if enemies.y >= 600:
                enemies.y = 0
                enemies.x = random.randint(0, 750)
                score+=1
        if p.x <= 10:
            p.x = 0
        if p.x >= 760:
            p.x = 750

        if collisioncheck(a, b, c, d, e, g, h, i, j, k, p):

            print('SCORE:' + str(score))
            file = open('scores.txt', 'r')
            current_high_score = file.read()
            file.close()
            file = open('scores.txt', 'w')
            if score > int(current_high_score):
                highscore = score
            else:
                highscore = current_high_score
            file.write(str(highscore))
            file.close()
            print('HIGH SCORE:' + str(highscore))
            file = open('coins.txt', 'r')
            coins = file.read()
            file.close()
            file = open('coins.txt', 'w')
            total_coins = int(coins) + round(score/10)
            file.write(str(total_coins))


            break

        if score >= 30000:
            print('You won!!')
            print('SCORE: ' + str(score))
            file = open('coins.txt', 'r')
            coins = file.read()
            file.close()
            file = open('coins.txt', 'w')
            total_coins = int(coins) + 3000
            file.write(str(total_coins))

            break
        text = "Score:" + str(score)
        label = font.render(text, 1, (255, 255, 255))
        win.blit(label, (width-200, height-40))
        pygame.display.update()


        clock.tick(60)
mainloop(score)

pygame.quit()
sys.exit()
