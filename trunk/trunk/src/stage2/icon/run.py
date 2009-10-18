#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

def main():
    import pygame,sys
    pygame.init()

#   speed = [2,2]
#   gray = (127,127,127)
#   angle = 0.0

# 標題
    pygame.display.set_caption('catch icon') 

# FPS 偵測起始化
    clock = pygame.time.Clock()

# 框架大小
    framesize = (640, 480)
    screen = pygame.display.set_mode(framesize)

# 滑鼠位置
    pos = (0,0)
    lastpos = (0,0)


# 載入外部視窗和初始化
    import Image
    im = Image.open("img/banana.jpg")
    fakeicon = pygame.image.load("img/banana.jpg")
    print im.format, im.size, im.mode
    points = [(50, 50), (im.size[0]+50, 50), (im.size[0]+50, im.size[1]+50), (50, im.size[0]+50)]
    moves = []
    hide = 1

# Mouse 工作冷卻
    cooldown = 0

# 顯示現在已經過秒數 (初始化)
    import time

    a = time.time()
# 播放影片

# 主程式正式開始, 若按 ESC 則跳出結束
    while not (pygame.key.get_pressed()[pygame.K_ESCAPE]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                moves.append(event.rel)
        else: pass
# 顯示現在狀態, 秒數和工作事件
        b = time.time()
        print u'經過時間 : %f 秒, FPS : %f page/sec , 事件 : %s' % (b-a, clock.get_fps(), event)

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()

        min_x = points[0][0]
        max_x = points[1][0]
        min_y = points[0][1]
        max_y = points[2][1]

#       if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
#       if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))
        screen.fill((0, 0, 0))
        screen.blit(fakeicon, (points[0][0],points[0][1]))

        if pygame.mouse.get_pressed()[0]:
            if min_x <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= max_y:
                if min_x < 0 : points = [(0, min_y), (im.size[0], min_y), (im.size[0], im.size[1]+ min_y), (0, im.size[0]+min_y)]
                elif min_y < 0 : points = [(min_x, 0), (im.size[0]+min_x, 0), (im.size[0]+min_x, im.size[1]), (min_x, im.size[0]+min_y)]
                elif max_x > framesize[0] : points = [(framesize[0]-im.size[0] , max_y-im.size[1]), (framesize[0] , max_y-im.size[1]), (framesize[0] , max_y), (framesize[0]-im.size[0] , max_y)]
                elif max_y > framesize[1] : points = [(max_x-im.size[0] , framesize[1]-im.size[1]), (max_x , framesize[1]-im.size[1]), (max_x , framesize[1]), (max_x-im.size[0] , framesize[1])]
                else:
                    if lastpos != pos:
                        for i in range(4):
                            x = points[i][0] + moves[-1][0]
                            y = points[i][1] + moves[-1][1]
                            points[i] = (x, y)

            if max_x-100 <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= min_y+100:
                if cooldown > 50:
                    if hide == 1: hide = 0
                    elif hide == 0: hide = 1
                    else: pass
                    cooldown = 0
                else:
                    pass
            lastpos = pos

## 滑鼠冷卻
        cooldown = cooldown + 1
        if cooldown > 30000: cooldown = 0


# 將資料寫至螢幕
        pygame.display.flip()
        clock.tick(100)
#       print clock.get_fps()
#       pygame.display.set_caption("uimeter , fps: " + str(clock.get_fps()))


if __name__ == "__main__":
#   try:
    main()
#   except:
#       pass
