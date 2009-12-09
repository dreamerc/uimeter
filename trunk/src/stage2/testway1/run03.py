#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

'''
測試目的：方形和圓形點擊的方便度。

測試方法：1.先測方的
		第一次出現1個，位置不定，要求點擊
		第二次出現2個，位置不定，要求各點擊1次
		第三次出現3個，位置不定，要求各點擊1次
		以次類推
	  2.再測圓的
		方法同上
	在限定時間下，因為圖形大小，會造成點擊圖形的誤點率
	依所得資料可得結果。
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

    points = []
    moves = []
    hide = 0


# Mouse 工作冷卻
    cooldown = 0

# 顯示現在已經過秒數 (初始化)
    import time

    a = time.time()

# CSV 資料庫格式
    if csv_bool == 1:
        import csv
        csv_file = csv.writer(open("csv_file.csv", "wb"),delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    else:
        pass

# 隨機產生矩形大小
# x 座標 , y 座標 , x 大小 , y 大小
    import random
    rect = []
    rect_color = []
    rect_hit = []
    counter = 0
    mark = 0
# 圓
    mark_circle = 0
    circle = []
    circle_color = []
    circle_rad = []
    circle_hit = []

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
        if debug == 1: print u'經過時間 : %f 秒, FPS : %f page/sec , 事件 : %s' % (b-a, clock.get_fps(), event)
        if csv_bool == 1 :csv_file.writerows([str(time.time()-begin_time), str(clock.get_fps()), str(event)])

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()


#       if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
#       if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))
        screen.fill((255, 255, 255))
        if mark == 0:
            counter += 1
            if counter == 11:
                counter = 1
                if mark_circle == 1: mark_circle = 0
                else: mark_circle = 1
            if mark_circle == 0:
                rect = []
                rect_hit = []
                for i in range(counter):
                    rect.append((random.randint(0,600), random.randint(0,380), random.randint(5,100), random.randint(5,100) ))
                    rect_hit.append(0)
                    a1 = random.randint(0,200)
                    rect_color.append((a1,a1,a1))
                rect.sort()
            else:
                circle = []
                circle_rad = []
                circle_hit = []
                for i in range(counter):
                    circle.append((random.randint(50,600), random.randint(50,380)))
                    circle_rad.append(random.randint(5,50))
                    circle_hit.append(0)
                    a1 = random.randint(0,200)
                    circle_color.append((a1,a1,a1))
                circle_rad.sort(reverse=True)
            mark = 1
            
        if mark_circle == 0:
            for i in range(counter):
                pygame.draw.rect(screen, rect_color[i] , rect[i])
            if pygame.mouse.get_pressed()[0]:
                j = 0
                for i in rect:
                    if i[0] <= mouse_pos[0] <= i[0]+i[2] and i[1] <= mouse_pos[1] <= i[1]+i[3]:
                        rect_hit[j] = 1
                    j += 1
                k = 0
                for i in range(counter):
                    k += rect_hit[i]
                if debug == 1: print k, counter
                if k == counter : mark = 0
        else:
            for i in range(counter):
                pygame.draw.circle(screen, circle_color[i], circle[i], circle_rad[i])
            if pygame.mouse.get_pressed()[0]:
                for i in range(counter):
                    if (mouse_pos[0]-circle[i][0])**2 +(mouse_pos[1]-circle[i][1])**2 <= circle_rad[i]**2:
                        circle_hit[i] = 1
                k = 0
                for i in range(counter):
                    k += circle_hit[i]
                print k, counter
                if k == counter : mark = 0
## 滑鼠冷卻


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

    main()
