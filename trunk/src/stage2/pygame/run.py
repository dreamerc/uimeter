#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

def main():
    import pygame,sys
    pygame.init()

    speed = [2,2]
    gray = (127,127,127)
    angle = 0.0

    pygame.display.set_caption('uimeter') 

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((640,480))

    movie = pygame.movie.Movie('demo.mpg')

# 圖形需存成 tga 加速影像轉換
    background = pygame.image.load("background.tga")
    ball = pygame.image.load("test.tga")
    ball2 = pygame.image.load("test2.tga")
#fakewindow = pygame.image.load("fakewindow.tga")
    fakewindow = pygame.image.load("img/word.tga")
    minfakewindow = pygame.image.load("minfakewindow.tga")

    pos = (0,0)
    lastpos = (0,0)
#ballrect = ball.get_rect()

# Fake Window
    import Image
    im = Image.open("img/word.tga")
    print im.format, im.size, im.mode
    points = [(50, 50), (im.size[0]+50, 50), (im.size[0]+50, im.size[1]+50), (50, im.size[0]+50)]
    moves = []
    hide = 1

# Mouse
    cooldown = 0

    import time,csv

# 播放影片
    movie.play()
    pygame.time.wait(2500)

# 主程式正式開始, 若按 ESC 則跳出結束
    while not (pygame.key.get_pressed()[pygame.K_ESCAPE]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                moves.append(event.rel)
        else: pass

#        print u'%f, %s' % (time.clock(), event)


#    ballrect = ballrect.move(speed)
#    if ballrect.left < 0 or ballrect.right > 640:
#       speed[0] = -speed[0]
#    if ballrect.top < 0 or ballrect.bottom > 480:
#        speed[1] = -speed[1]

#    screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
#    screen.blit(ball,ballrect)

        mouse_pos = pygame.mouse.get_pos()

        min_x = points[0][0]
        max_x = points[1][0]
        min_y = points[0][1]
        max_y = points[2][1]

        if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
        if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))

        if pygame.mouse.get_pressed()[0]:
            if min_x <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= max_y:
                if max_x > 640 or max_y > 480 or min_x < 0 or min_y < 0:
                    for i in range(4):
                        x = points[i][0] - moves[-1][0]
                        y = points[i][1] - moves[-1][1]
                        points[i] = (x, y)
                else:
                    if lastpos != pos:
                        for i in range(4):
                            x = points[i][0] + moves[-1][0]
                            y = points[i][1] + moves[-1][1]
                            points[i] = (x, y)

            if max_x-100 <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= min_y+100:
                if cooldown > 300:
                    if hide == 1: hide = 0
                    elif hide == 0: hide = 1
                    else: pass
                    cooldown = 0
                else:
                    pass
            lastpos = pos

        cooldown = cooldown + 1
        if cooldown > 30000: cooldown = 0
# 旋轉 30 度印出

#   rotat = pygame.transform.rotozoom(ball2, angle,1)
#   px = (rotat.get_width() - 50) / 2
#   py = (rotat.get_height() - 50) / 2
#   fix = 31
#   screen.blit(rotat, (320-px-fix,200-py-fix))
#   angle += 5
#   angle %= 360

# 滑鼠游標
#   x, y = pos
#   screen.blit(rotat, (x-px-fix, y-py-fix))

# 將資料寫至螢幕
        pygame.display.flip()
        clock.tick(100)
        pygame.display.set_caption("uimeter , fps: " + str(clock.get_fps()))


if __name__ == "__main__":
#   try:
    main()
#   except:
#       pass
