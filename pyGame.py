import pygame
from pygame.locals import *
pygame.init()
pygame.event.get()





screen_size =[360, 600]
screen = pygame.display.set_mode(screen_size)
background = pygame.image.load('background.png')
bullet = pygame.image.load('bullet.png')
one = pygame.image.load('one.png')
two = pygame.image.load('two.png')
three = pygame.image.load('three.png')
ship = pygame.image.load('spaceship.png')
clock = pygame.time.Clock()
cycles = 0
planet = ['one.png', 'two.png', 'three.png']
index = 0
keep_alive = True
move_direction = 'right'
planet_x = 150
Fired = False
bullet_y = 500
while keep_alive == True:
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] == True:
            print("Space key pressed")
            keep_alive = False
        if keys[pygame.K_SPACE] == True:
            Fired = True
        
    px = pygame.image.load(planet[index])
    screen.blit(background, [0,0])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(ship, [160, 500])
    screen.blit( px, [planet_x, 50])
    
        

    if move_direction == 'right':
        planet_x = planet_x + 3
        if planet_x >= 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 3
        if planet_x <= 0:
            move_direction = 'right'
    if Fired == True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            Fired = False
            bullet_y = 500
    if bullet_y < 80 and planet_x >120 and planet_x <180:
        index += 1
        planet_x += 10
        bullet_y = 500
        Fired = False
        print("BOOM")
        if index == 3 :
            print("Winner")
            break
    cycles += 1
    pygame.display.update()
    clock.tick(60)