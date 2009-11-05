#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

def main(debug=1,csv_bool=0,windows=0):
    import pygame,sys
    pygame.init()

# 啟動字型
    print "啟動字型測試 ..." + str(pygame.font.get_init())
    if windows == 0 : font = pygame.font.Font("/usr/share/fonts/truetype/arphic/uming.ttc",18)
    else : font = pygame.font.SysFont("新細明體",18)
    font_text = u"中文測試"
    font_text_old = u""
    ren = font.render(font_text,1,(127,127,127))

#   speed = [2,2]
#   gray = (127,127,127)
#   angle = 0.0

# 標題
    pygame.display.set_caption('uimeter') 

# FPS 偵測起始化
    clock = pygame.time.Clock()

# 框架大小
    framesize = (640, 480)
    screen = pygame.display.set_mode(framesize)

## 影片和圖形來源
    movie = pygame.movie.Movie('demo.mpg')

# 圖形需存成 tga 加速影像轉換

    background = pygame.image.load("background.tga")
    fakewindow = pygame.image.load("img/123.tga")
    minfakewindow = pygame.image.load("minfakewindow.tga")
    workbar_0 = pygame.image.load("img/640x50a.tga")
    workbar_1 = pygame.image.load("img/640x50b.tga")
    workbar_2 = pygame.image.load("img/640x50c.tga") #630x432

# 滑鼠位置
    pos = (0,0)
    lastpos = (0,0)

# 載入外部視窗和初始化
    import Image
    im = Image.open("img/123.tga")
    print im.format, im.size, im.mode
    points = [(50, 50), (im.size[0]+50, 50), (im.size[0]+50, im.size[1]+50), (50, im.size[0]+50)]
    moves = []
    hide = 0
    max_workbar = 0

# Mouse 工作冷卻
    mouse_timeout = 0

# 顯示現在已經過秒數 (初始化)
    import time

# CSV 資料庫格式
    if csv_bool == 1:
        import csv
        csv_file = csv.writer(open("csv_file.csv", "wb"),delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    else:
        pass
# 播放影片
#    movie.play()
#    pygame.time.wait(2500)
    
    begin_time = time.time()
# 主程式正式開始, 若按 ESC 則跳出結束
    while not (pygame.key.get_pressed()[pygame.K_ESCAPE]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                moves.append(event.rel)
            elif event.type == pygame.KEYDOWN:
                for i in range(pygame.K_a, pygame.K_z + 1) :
                    if pygame.key.get_pressed()[i] == 1 :
                        print chr(i) + ' '                
                        font_text = font_text + chr(i)
                if windows == 0 :
                    if event.unicode != u'\x1b' :
                        print event.unicode
                        font_text = font_text + event.unicode
            else: pass
# 顯示現在狀態, 秒數和工作事件
        if debug == 1: print u'經過時間 : %f 秒, FPS : %f page/sec, 事件 : %s' % (time.time()-begin_time, clock.get_fps(), event)
        if csv_bool == 1: csv_file.writerows([str(time.time()-begin_time), str(clock.get_fps()), str(event)])

        screen.blit(background, (0, 0))

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()

        min_x = points[0][0]
        max_x = points[1][0]
        min_y = points[0][1]
        max_y = points[2][1]


        if max_workbar == 1:
            screen.blit(workbar_0, (0,480-50))
            screen.blit(workbar_2,(0,0))
            if pygame.mouse.get_pressed()[0]:
                if mouse_timeout > 50:
                    if 630-100+30 <= mouse_pos[0] <= 630-100+30+25 and 0 <= mouse_pos[1] <= 0+20:
                        max_workbar = 0
                    elif 630-100 <= mouse_pos[0] <= 630-100+30 and 0 <= mouse_pos[1] <= 0+20:
                        max_workbar = 0
                        hide = 1
                    mouse_timeout = 0
                else:
                    pass
        else:
            if hide == 0: 
                screen.blit(fakewindow, (points[0][0],points[0][1]))
                screen.blit(workbar_0, (0,480-50))
                if pygame.mouse.get_pressed()[0]:
                    if mouse_timeout > 50:
                        if max_x-100 <= mouse_pos[0] <= max_x-100+30 and min_y <= mouse_pos[1] <= min_y+20:
                            if hide == 0: hide = 1
                            elif hide == 1: hide = 0
                            else: pass                            
                        elif max_x-100+30 <= mouse_pos[0] <= max_x-100+30+25 and min_y <= mouse_pos[1] <= min_y+20:
                            max_workbar = 1
                            print max_workbar
                        else: pass
                        mouse_timeout = 0
                    else:
                        pass
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
                    else:
                        pass
                    lastpos = pos
            else:
                screen.blit(workbar_1, (0,480-50))
                if pygame.mouse.get_pressed()[0]:
                    if 578 <= mouse_pos[0] <= 640 and 430 <= mouse_pos[1] <= 480:
                        hide = 0
    
## 滑鼠冷卻
        mouse_timeout = mouse_timeout + 1
        if mouse_timeout > 30000: mouse_timeout = 0

# 繪製字型
        if font_text != font_text_old: 
            ren = font.render(font_text,1,(127,127,127))
            if len(font_text) > 30:
                font_text = u"字太多...變少了"
        else:
            pass
        screen.blit(ren, (0,0))
        font_text_old = font_text
# 將資料寫至螢幕
        pygame.display.flip()
        clock.tick(100)
#       print clock.get_fps()
#       pygame.display.set_caption("uimeter , fps: " + str(clock.get_fps()))


if __name__ == "__main__":

    try:
       import pygame
    except:
       print "pygame 尚未安裝"

    try:
       import Image
    except:
       print "Python Imaging Libary 尚未安裝"

    import sys
    if sys.platform == "win32" or sys.platform == "cygwin" : windows = 1
    else : windows = 0

    main(windows=windows)
