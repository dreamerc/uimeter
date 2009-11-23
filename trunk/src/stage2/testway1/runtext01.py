#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

'''
測試目的:文字的大小、字型和顏色對於始於使用者的影響

測試方法:1.出現數個ICON相同的圖示，並針對可變變因(如:大小、字型和顏色)
	   來對底部文字進行更改‧

	 2.求出對象尋找圖示之所需要的秒數，就可得知哪項變因的影響程度較高
	   而哪向變因的影響程度比較不明顯‧

範例:    大雕   跟    大雕(標準楷)    之間就有明顯的不同  ，可作為明顯判對依據‧
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
    moves = []

# 載入外部視窗和初始化
    import Image
    im = Image.open("imgtext/0.bmp")
    fakeicon1 = pygame.image.load("imgtext/0.bmp")
    print im.format, im.size, im.mode

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
        if debug == 1: print u'經過時間 : %f 秒, FPS : %f page/sec , 事件 : %s' % (b-a, clock.get_fps(), event)
        if csv_bool == 1 :csv_file.writerows([str(time.time()-begin_time), str(clock.get_fps()), str(event)])

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()


#       if hide == 1 : screen.blit(fakewindow, (points[0][0],points[0][1]))
#       if hide == 0 : screen.blit(minfakewindow, (points[1][0]-44,points[0][1]))
        screen.fill((255, 255, 255))
        screen.blit(fakeicon1, (0,0))

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
       print "pygame 尚未安裝"

    try:
       import Image
    except:
       print "Python Imaging Libary 尚未安裝"

    main()
