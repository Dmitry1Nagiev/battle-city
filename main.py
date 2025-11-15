import pygame
import os
import sys
import random


pygame.init()
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 1200
HEIGHT = 800
FPS = 60
sc = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
lvl = 'game'
from load import *

def lvlGame():
    sc.fill('black')
    brick_group.update()
    brick_group.draw(sc)
    bush_group.update()
    bush_group.draw(sc)
    iron_group.update()
    iron_group.draw(sc)
    water_group.update()
    water_group.draw(sc)
    enemy_group.update()
    enemy_group.draw(sc)
    player_group.update()
    player_group.draw(sc)
    flag_group.update()
    flag_group.draw(sc)
    pygame.display.update()
def drawMaps(nameFile):
    maps = []
    sourse = 'game lvl/'+str(nameFile)
    with open(sourse,"r") as file:
        for i in range(0,20):
            maps.append(file.readline().replace("\n","").split(',')[0:-1])

    pos = [0,0]
    for i in range(0,len(maps)):
        pos[1] = i*40
        for j in range(0,len(maps[0])):
            pos[0] = 40 * j
            if maps[i][j] == '1':
                brick = Brick(brick_image,pos)
                brick_group.add(brick)
            elif maps[i][j] == '2':
                bush = Bush(bush_image,pos)
                bush_group.add(bush)
            elif maps[i][j] == '3':
                iron = Iron(iron_image,pos)
                iron_group.add(iron)
            elif maps[i][j] == '5':
                water = Water(water_image,pos)
                water_group.add(water)
            elif maps[i][j] == '6':
                enemy = Enemy(enemy_image,pos)
                enemy_group.add(enemy)
            elif maps[i][j] == '4':
                flag = Flag(flag_image,pos)
                flag_group.add(flag)
class Brick(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Bush(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,image,pos):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right


class Iron(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,image,pos):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right

class Water(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,image,pos):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,image,pos):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right

class Enemy(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 1
        self.dir = "top"
        self.timer_move = 0
    def update(self,image,pos):
        self.timer_move += 1
        if self.timer_move / FPS > 2:
            if random.randint(1,4) == 1:
                self.dir = 'top'
            if self.dir == 'top':
                self.image = pygame.transform.rotate(enemy_image,0)
                self.rect.y -= self.speed
class Flag(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,image,pos):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 5
        self.dir = "top"
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.image = pygame.transform.rotate(player_image,90)
            self.rect.x -= self.speed
            self.dir = "left"






brick_group = pygame.sprite.Group()
bush_group = pygame.sprite.Group()
iron_group = pygame.sprite.Group()
water_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
flag_group = pygame.sprite.Group()
player = Player(player_image,(1000,80))
player_group.add(player)

drawMaps('1.txt')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl == 'game':
        lvlGame()
    clock.tick(FPS)













