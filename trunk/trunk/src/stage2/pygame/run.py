#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

import pygame,sys
pygame.init()

speed = [2,2]
gray = (127,127,127)
angle = 0.0

pygame.display.set_caption('uimeter') 
screen = pygame.display.set_mode((640,480))

# 圖形需存成 tga 加速影像轉換
background = pygame.image.load("background.tga")
ball = pygame.image.load("test.tga")
ball2 = pygame.image.load("test2.tga")
fakewindow = pygame.image.load("fakewindow.tga")
minfakewindow = pygame.image.load("minfakewindow.tga")

pos = (0,0)
lastpos = (0,0)
ballrect = ball.get_rect()

# Fake Window
points = [(200, 200), (200+320, 200), (200+320, 200+200), (200, 200+200)]
moves = []
hide = 1

import time

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos
            moves.append(event.rel)
        else: pass

    print u'%f, %s' % (time.clock(), event)
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > 640:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > 480:
        speed[1] = -speed[1]

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(ball,ballrect)

    mouse_pos = pygame.mouse.get_pos()

    min_x = min(points[0][0], points[1][0], points[2][0], points[3][0])
    max_x = max(points[0][0], points[1][0], points[2][0], points[3][0])
    min_y = min(points[0][1], points[1][1], points[2][1], points[3][1])
    max_y = max(points[0][1], points[1][1], points[2][1], points[3][1])

    if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
    if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))

    if pygame.mouse.get_pressed()[0]:
        if min_x <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= max_y:
            if lastpos != pos:
                for i in range(4):
                    x = points[i][0] + moves[-1][0]
                    y = points[i][1] + moves[-1][1]
                    points[i] = (x, y)
        if min_x+275 <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= max_y-175:
            if hide == 1: hide = 0
            elif hide == 0: hide = 1
            else: pass
#                   print points
        lastpos = pos

# 旋轉 30 度印出

    rotat = pygame.transform.rotozoom(ball2, angle,1)
    px = (rotat.get_width() - 50) / 2
    py = (rotat.get_height() - 50) / 2
    fix = 31
    screen.blit(rotat, (320-px-fix,200-py-fix))
    angle += 5
    angle %= 360

# 滑鼠游標
#   x, y = pos
#   screen.blit(rotat, (x-px-fix, y-py-fix))

# 將資料寫至螢幕
    pygame.display.flip()

