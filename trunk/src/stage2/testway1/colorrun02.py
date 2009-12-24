#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

'''
測試目的：背景色對人判斷的影響

測試方法：1.出現3個顏色各不同的等大方框，裡面放入數量相等的『H』字。
	  
	  2.要求測試對象點選最容易分辨的方框；
	    因為背景色和文字顏色的影響，清晰度會不同，再把背景色和文字顏變更測試一次，
	    多次採樣獲取結果。	
'''

def main(debug=1,csv_bool=0):
    import pygame,sys
    pygame.init()

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
    im = Image.open("img/B1.tga")
    fakeicon1 = pygame.image.load("img/B1.tga")
    print im.format, im.size, im.mode
    points = [(50, 150), (im.size[0]+50, 150), (im.size[0]+150, im.size[1]+150), (50, im.size[0]+150)]
    moves = []
    hide = 0

    fakeicon2 = pygame.image.load("img/B2.tga")
    fakeicon3 = pygame.image.load("img/B3.tga")

    fakeicon1_big =  pygame.transform.scale(fakeicon1, (150, 150))
    fakeicon2_big =  pygame.transform.scale(fakeicon2, (150, 150))
    fakeicon3_big =  pygame.transform.scale(fakeicon3, (150, 150))

    title = pygame.image.load("img/title.tga")

# 螢幕擷取
    image_counter = 0

# 顯示線段
    show_lines = 1
    lines_move = []
    lines_press = []

# Mouse 工作冷卻
    cooldown = 0

# 顯示現在已經過秒數 (初始化)
    import time

    a = time.time()

# CSV 資料庫格式
    if csv_bool == 1:
        import csv
        csv_file = csv.writer(open("csv_file_c02.csv", "wb"),delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    else:
        pass
# 播放影片

# 主程式正式開始, 若按 ESC 則跳出結束
    while not (pygame.key.get_pressed()[pygame.K_ESCAPE]):
# 事件判別
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                moves.append(event.rel)
            elif event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_1]:
                    if show_lines == 1 : show_lines = 0
                    else : show_lines = 1
            elif event.type == pygame.MOUSEBUTTONDOWN:
		try:
                    lines_press.append(mouse_pos)
                except:
                    pass
                pygame.image.save(screen, 'screenshot/c02_' +str(image_counter)+'.png')
                image_counter += 1
        else: pass
# 顯示現在狀態, 秒數和工作事件
        b = time.time()
        if debug == 1: print u'經過時間 : %f 秒, FPS : %f page/sec , 事件 : %s' % (b-a, clock.get_fps(), event)
        if csv_bool == 1 :csv_file.writerows([str(b-a), str(clock.get_fps()), str(event)])

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()

        min_x = points[0][0]
        max_x = points[1][0]
        min_y = points[0][1]
        max_y = points[2][1]

#       if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
#       if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))
        screen.fill((255, 255, 255))
        screen.blit(title, (0,0))
        screen.blit(fakeicon1, (points[0][0],points[0][1]))
        screen.blit(fakeicon2, (points[0][0]+200,points[0][1]))
        screen.blit(fakeicon3, (points[0][0]+400,points[0][1]))

        if pygame.mouse.get_pressed()[0]:
            if min_x <= mouse_pos[0] <= max_x and min_y <= mouse_pos[1] <= max_y:
                screen.blit(fakeicon1_big, (points[0][0],points[0][1]))
                print "mouse_on_0"
                break
            if min_x+200 <= mouse_pos[0] <= max_x+200 and min_y <= mouse_pos[1] <= max_y:
                screen.blit(fakeicon2_big, (points[0][0]+200,points[0][1]))
                print "mouse_on_1"
                break
            if min_x+400 <= mouse_pos[0] <= max_x+400 and min_y <= mouse_pos[1] <= max_y:
                screen.blit(fakeicon3_big, (points[0][0]+400,points[0][1]))
                print "mouse_on_2"
                break

# 繪製路徑
        lines_move.append(mouse_pos)

        if show_lines == 1:
            try:
                pygame.draw.lines(screen, (255,0,0), 0, lines_move)
                pygame.draw.lines(screen, (0,255,0), 0, lines_press)
            except:
                pass

## 滑鼠冷卻


        cooldown = cooldown + 1
        if cooldown > 140000: cooldown = 0


# 將資料寫至螢幕
        pygame.display.flip()
        clock.tick(100)

if __name__ == "__main__":
    try:
       import pygame
    except:
       print u"pygame 尚未安裝"

    try:
       import Image
    except:
       print u"Python Imaging Libary 尚未安裝"

    main(csv_bool=1)
