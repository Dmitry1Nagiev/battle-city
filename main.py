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
lvl = 'menu'
from load import *

font = pygame.font.SysFont('Aria', 40)
def startMenu():
    sc.fill('grey')
    button_group.draw(sc)
    button_group.update()
    pygame.display.update()

def startWinMenu():
    sc.fill('black')
    button_win_group.draw(sc)
    button_win_group.update()
    pygame.display.update()


class Button(pygame.sprite.Sprite):
    def __init__(self,image,pos,nect_lvl,text):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.next_lvl = nect_lvl
        self.text = text
    def update(self):
        global lvl
        text_render = font.render(self.text,True,'white')
        if self.text=="Back to menu":
            sc.blit(text_render, (self.rect.x + 12, self.rect.y + 4))
        else:
            sc.blit(text_render,(self.rect.x + 80 , self.rect.y + 5))


        click = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.left < click[0] < self.rect.right and self.rect.top < click[1]<self.rect.bottom:
                lvl = self.next_lvl
                if lvl == 'game':
                    restart()
                    drawMaps('1.txt')
                if lvl == 'back' :
                    lvl = 'menu'



def lvlGame():
    sc.fill('black')
    brick_group.update()
    brick_group.draw(sc)

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
    bullet_enemy_group.update()
    bullet_enemy_group.draw(sc)
    bullet_player_group.update()
    bullet_player_group.draw(sc)
    bush_group.update()
    bush_group.draw(sc)
    pygame.display.update()


def restart():
    global water_group, iron_group, brick_group,bush_group,player_group,enemy_group,bullet_player_group,bullet_enemy_group,flag_group,player
    bullet_player_group = pygame.sprite.Group()
    bullet_enemy_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    bush_group = pygame.sprite.Group()
    iron_group = pygame.sprite.Group()
    water_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    flag_group = pygame.sprite.Group()
    player = Player(player_image[1], (1000, 80))
    player_group.add(player)
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
    def update(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            if player.dir == "down":
                player.rect.bottom = self.rect.top



class Bush(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            if player.dir == "down":
                player.rect.bottom = self.rect.top


class Iron(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            if player.dir == "down":
                player.rect.bottom = self.rect.top

class Water(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self,):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            if player.dir == "down":
                player.rect.bottom = self.rect.top

class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = 3
        self.dir = 'top'
        self.timer_shot = 0
        self.frame = 0
        self.timer_anime = 0
        self.anime = False

    def update(self):
        self.timer_shot += 1
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.anime = True
            self.image = pygame.transform.rotate(player_image[self.frame],90)
            self.rect.x -= self.speed
            self.dir = 'left'

        elif key[pygame.K_w]:
            self.anime = True
            self.image = pygame.transform.rotate(player_image[self.frame], 360)
            self.rect.y -= self.speed
            self.dir = 'top'

        elif key[pygame.K_d]:
            self.anime = True
            self.image = pygame.transform.rotate(player_image[self.frame], 270)
            self.rect.x += self.speed
            self.dir = 'right'

        elif key[pygame.K_s]:
            self.anime = True
            self.image = pygame.transform.rotate(player_image[self.frame], 180)
            self.rect.y += self.speed
            self.dir = 'down'

        if key[pygame.K_SPACE] and self.timer_shot / FPS > 1:
            bullet = Bullet_player(player_bullet,self.rect.center, self.dir)
            bullet_player_group.add(bullet)
            self.timer_shot = 0
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(player_image) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0


class Bullet_player(pygame.sprite.Sprite):
    def __init__(self,image,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir
        self.speed = 5
        self.frame = 0
        self.timer_anime = 0
        self.anime = False


    def update(self):
        global lvl
        if self.dir == 'top':
            self.rect.y -= self.speed
        elif self.dir == 'down':
            self.rect.y += self.speed
        elif self.dir == 'left':
            self.rect.x -= self.speed
        elif self.dir == 'right':
            self.rect.x += self.speed
        if pygame.sprite.groupcollide(bullet_player_group, brick_group, True, True) \
                or pygame.sprite.groupcollide(bullet_player_group, enemy_group, True,True):
                self.kill()
        if pygame.sprite.spritecollide(self,enemy_group, True):
                self.anime = True
                self.speed = 0
        if self.anime:
            self.timer_anime += 1
            if self.timer_anime / FPS > 0.1:
                if self.frame == len(bullet_image) - 1:
                    self.frame = 0
                    self.rect.center = (-1000,0)
                    self.kill()
                else:
                    self.frame += 1
                self.timer_anime = 0
            self.image = bullet_image[self.frame]
        if pygame.sprite.groupcollide(bullet_player_group, flag_group, True,True):
            lvl = 'win'
        if pygame.sprite.groupcollide(bullet_player_group,iron_group,False,False):
            Bullet_player.kill(self)

















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
        self.timer_shot = 0


    def update(self):
        self.timer_move += 1
        self.timer_shot += 1
        if self.timer_shot / FPS > 1:
            bullet_en = Bullet_enemy(enemy_bullet, self.rect.center, self.dir)
            bullet_enemy_group.add(bullet_en)
            self.timer_shot = 0
        d = random.randint(1,4)
        if self.timer_move / FPS > 2:
            if d == 1:
                self.dir = 'top'
            if d == 3:
                self.dir = 'right'
            if d == 4:
                self.dir = 'bottom'
            if d == 2:
                self.dir = 'left'
            self.timer_move = 0
        if self.dir == 'top':
            self.image = pygame.transform.rotate(enemy_image,360)
            self.rect.y -= self.speed
        elif self.dir == 'bottom':
            self.image = pygame.transform.rotate(enemy_image, 180)
            self.rect.y += self.speed
        if self.dir == 'right':
            self.image = pygame.transform.rotate(enemy_image, 270)
            self.rect.x += self.speed
        elif self.dir == 'left':
            self.image = pygame.transform.rotate(enemy_image, 90)
            self.rect.x -= self.speed

        if (pygame.sprite.spritecollide(self,brick_group,False)
            or pygame.sprite.spritecollide(self,water_group,False)) \
                or pygame.sprite.spritecollide(self,bush_group,False) \
                or pygame.sprite.spritecollide(self, iron_group, False) :
            self.timer_move = 0
            if self.dir == 'top':
                self.dir = 'bottom'
            elif self.dir == 'bottom':
                self.dir = 'top'
            elif self.dir == 'left' :
                self.dir = 'right'
            elif self.dir == 'right':
                self.dir = 'left'



class Bullet_enemy(pygame.sprite.Sprite):
    def __init__(self,image,pos,dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.dir = dir
        self.speed = 5
        self.timer_shot = 0


    def update(self):
        global lvl
        if self.dir == 'top':
            self.rect.y -= self.speed
        elif self.dir == 'bottom':
            self.rect.y += self.speed
        elif self.dir == 'left':
            self.rect.x -= self.speed
        elif self.dir == 'right':
            self.rect.x += self.speed
        if pygame.sprite.groupcollide(bullet_enemy_group, brick_group, True, True):
            self.kill()
        if pygame.sprite.groupcollide(bullet_enemy_group, player_group, True, True):
            lvl = 'menu'
        if pygame.sprite.groupcollide(bullet_enemy_group, iron_group, False, False):
            Bullet_enemy.kill(self)
        if self.rect.x >= WIDTH or self.rect.y >= HEIGHT or self.rect.y <= 0 or self.rect.x <= 0:
            self.kill()





class Flag(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
    def update(self):
        if pygame.sprite.spritecollide(self,player_group,False):
            if player.dir == "left":
                player.rect.left = self.rect.right
            if player.dir == "right":
                player.rect.right = self.rect.left
            if player.dir == "top":
                player.rect.top = self.rect.bottom
            if player.dir == "down":
                player.rect.bottom = self.rect.top




button_group = pygame.sprite.Group()

button_start = Button(button_image,(500,100),'game','start')
button_group.add(button_start)

button_exit = Button(button_image,(500,180),'end','exit')
button_group.add(button_exit)

button_win_group = pygame.sprite.Group()
#button_win = Button(button_image,(HEIGHT/2,WIDTH/2),'rest','Restart')
#button_win_group.add(button_win)

button_back = Button(button_image,(500,280),'back','Back to menu')
button_win_group.add(button_back)




#drawMaps('1.txt')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if lvl == 'game':
        lvlGame()
    elif lvl == 'menu':
        startMenu()
    elif lvl == 'end':
        pygame.quit()
        sys.exit()
    elif lvl == 'win':
        startWinMenu()
    clock.tick(FPS)













