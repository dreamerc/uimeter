#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

def main(debug=0,csv_bool=0,windows=0,tmovie=0):
    import pygame,sys
    pygame.init()

# 啟動字型
    print u"啟動字型測試 ..." + str(pygame.font.get_init())
    if windows == 0 : font = pygame.font.Font("/usr/share/fonts/truetype/arphic/uming.ttc",24)
    else : font = pygame.font.SysFont("新細明體",24)
    font_text = u"中文測試"
    font_text_old = u""
    ren = font.render(font_text,1,(127,127,127))

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

# 螢幕擷取
    image_counter = 0

# Mouse 工作冷卻
    mouse_timeout = 0

# 顯示現在已經過秒數 (初始化)
    import time

# CSV 資料庫格式
    if csv_bool == 1:
        import csv
        csv_file = csv.writer(open("csv_file.csv", "wb"), quoting=csv.QUOTE_MINIMAL)
    else:
        pass
# 矩陣輸出
    matrix_move = []
    for i in range(481):
        matrix_move.append([])
        for j in range(641):
            matrix_move[i].append(0)
    matrix_press = []
    for i in range(481):
        matrix_press.append([])
        for j in range(641):
            matrix_press[i].append(0)
# 播放影片
    if tmovie == 1:
        movie.play()
        pygame.time.wait(2500)

# 顯示線段
    show_lines = 0
    lines_move = []
    lines_press = []

# 存入初始時間
    begin_time = time.time()
    
# 主程式正式開始, 若按 ESC 則跳出結束
    while not (pygame.key.get_pressed()[pygame.K_ESCAPE]):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                pos = event.pos
                moves.append(event.rel)
# 儲存滑鼠位置至矩陣
                matrix_move[pygame.mouse.get_pos()[1]][pygame.mouse.get_pos()[0]] = matrix_move[pygame.mouse.get_pos()[1]][pygame.mouse.get_pos()[0]] + 1
            elif event.type == pygame.KEYDOWN:
                if windows == 0 :
                    if event.unicode == u'\x08':
                        font_text = font_text[0:-1]
                    elif event.unicode != u'\x1b' :
                        print event.unicode
                        font_text = font_text + event.unicode
                else:
                    if pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                        font_text = font_text[0:-1]
                    for i in range(pygame.K_a, pygame.K_z + 1) :
                        if pygame.key.get_pressed()[i] == 1 :
                            print chr(i) + ' '                
                            font_text = font_text + chr(i)
                if pygame.key.get_pressed()[pygame.K_1]:
                    if show_lines == 1 : show_lines = 0
                    else : show_lines = 1

            elif event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    lines_press.append(mouse_pos)
                except:
                    pass
                pygame.image.save(screen, 'screenshot/' +str(image_counter)+'.png')
                image_counter += 1
            else: pass
# 顯示現在狀態, 秒數和工作事件
        if debug == 1: print u'經過時間 : %f 秒, FPS : %f page/sec, 事件 : %s' % (time.time()-begin_time, clock.get_fps(), event)
        if csv_bool == 1: csv_file.writerow((str(time.time()-begin_time), str(clock.get_fps()), str(pygame.mouse.get_pos()[0]), str(pygame.mouse.get_pos()[1]), str(event) ))

# 存入按下按鈕
        if pygame.mouse.get_pressed()[0]:
            matrix_press[pygame.mouse.get_pos()[1]][pygame.mouse.get_pos()[0]] = matrix_move[pygame.mouse.get_pos()[1]][pygame.mouse.get_pos()[0]] + 1
        screen.blit(background, (0, 0))

## 視窗偵測與移動
        mouse_pos = pygame.mouse.get_pos()

        min_x = points[0][0]
        max_x = points[2][0]
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
                        if lastpos != pos:
                            for i in range(4):
                                x = points[i][0] + moves[-1][0]
                                y = points[i][1] + moves[-1][1]
                                points[i] = (x, y)
                            min_x = points[0][0]
                            max_x = points[2][0]
                            min_y = points[0][1]
                            max_y = points[2][1]
                        if min_x < 0 : points = [(0, min_y), (im.size[0], min_y), (im.size[0], im.size[1]+ min_y), (0, im.size[0]+min_y)]
                        elif min_y < 0 : points = [(min_x, 0), (im.size[0]+min_x, 0), (im.size[0]+min_x, im.size[1]), (min_x, im.size[0]+min_y)]
                        elif max_x > framesize[0] : points = [(framesize[0]-im.size[0] , max_y-im.size[1]), (framesize[0] , max_y-im.size[1]), (framesize[0] , max_y), (framesize[0]-im.size[0] , max_y)]
                        elif max_y > framesize[1] : points = [(max_x-im.size[0] , framesize[1]-im.size[1]), (max_x , framesize[1]-im.size[1]), (max_x , framesize[1]), (max_x-im.size[0] , framesize[1])]
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
            ren = font.render(font_text,1,(200,200,200))
            if len(font_text) > 25:
                font_text = u"字太多...變少了"
        else:
            pass
        screen.blit(ren, (0,0))
        font_text_old = font_text
# 繪製路徑
        lines_move.append(mouse_pos)

        if show_lines == 1:
            try:
                pygame.draw.lines(screen, (255,0,0), 0, lines_move)
                pygame.draw.lines(screen, (0,255,0), 0, lines_press)
            except:
                pass

# 將資料寫至螢幕
        pygame.display.flip()
        clock.tick(100)

# Mouse_move
# 繪製資料矩陣給 gnuplot 用
    file = open('heatmap.dat','wb')
    for i in matrix_move:
        for j in i:
            file.write(str(j) + ' ')
        file.write('\n')
    file.close()

# Gnuplot 繪圖
    try:
        g = Gnuplot.Gnuplot(debug=1)
        g('unset cbtics')
        g('unset key')
        g('set palette rgbformulae -30,-31,-32')
        g('set view map')
        g('set yrange [] reverse')
#       g("plot 'screenshot/0.png' binary filetype=png origin=(0,0)  dx=0.5 dy=1.5 with rgbimage notitle")
        g("splot 'heatmap.dat' matrix with image")
        raw_input('Please press return to exit...\n')

# Mouse_press
# 繪製資料矩陣給 gnuplot 用
        file = open('heatmap.dat','wb')
        for i in matrix_press:
            for j in i:
                file.write(str(j) + ' ')
            file.write('\n')
        file.close()

# Gnuplot 繪圖
        g = Gnuplot.Gnuplot(debug=1)
        g('unset cbtics')
        g('unset key')
        g('set palette rgbformulae -30,-31,-32')
        g('set view map')
        g('set yrange [] reverse')
        g("splot 'heatmap.dat' matrix with image")
        raw_input('Please press return to exit...\n')
    except:
        print u"無 gnuplot ... 結束程式"

if __name__ == "__main__":

    try:
       import pygame
    except:
       print u"pygame 尚未安裝"

    try:
       import Image
    except:
       print u"Python Imaging Libary 尚未安裝"

    try:
        print u'嘗試載入 Gnuplot ...',
        import Gnuplot
        print u'成功'
    except:
        print u'載入 Gnuplot 失敗... 檢查原因'
        try:
            import numpy
        except:
            print u'請先安裝 NumPy, 再安裝 Gnuplot'

    import sys
    if sys.platform == "win32" or sys.platform == "cygwin" :
        windows = 1
        print u"將不支援輸入法"
    else : windows = 0

    main(windows=windows,csv_bool=1)
