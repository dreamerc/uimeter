#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter - pygameui
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

class surface_text():
    """
    Pygame - text surface
    文字物件部份
    """
    def __init__(self, windows):
        if windows == 0 :
            try :
                print "嘗試載入 Arphic Uming...",
                self.font = pygame.font.Font("/usr/share/fonts/truetype/arphic/uming.ttc",24)
                print "成功"
            except :
                print "失敗, 改用系統內建字型"
        else:
            try :
                print "嘗試載入新細明體...",
                self.font = pygame.font.SysFont("新細明體",24)
                print "成功"
            except :
                print "失敗, 改用系統內建字型"

        self.text_list = [(u"Hello 中文 World")]
        self.text_color_list = [(127,127,127)]
        self.surface_list = [(self.font.render(self.text_list[0], 1, self.text_color_list[0]))]

    def test(self):
        print "啟動字型測試 ..." ,
        if pygame.font.get_init() == 1 : print "OK"
        else : print "Failed"

def main(debug=1, csv_bool=0, windows=0):

    import pygame
    pygame.init()

# 載入字型
    suf_t = surface_text(windows)
    suf_t.test()

# 標題
    pygame.display.set_caption('uimeter - pygameui')

# FPS 偵測起始化
    clock = pygame.time.Clock()

# 框架大小
    framesize = (640, 480)
    screen = pygame.display.set_mode(framesize)

# 顯示用平面
# suface_images.append(pygame.image.load("background.tga"), filepath, size)

# 滑鼠位置
    mouse_pos = [(0,0)]

# 載入外部圖片至顯示用平面
    import Image, os, sys
    path = "imgs/"
    if os.path.isdir(path) :
        print "讀取 " + path + "中"
        for root, dirs, files in os.walk(path) :
            for file in files :
                print os.path.join(root, file) + "....." ,
                try:
                    filepath = os.path.join(root, file)
                    im = Image.open(filepath)
                    print im.format, im.size, im.mode
# 不讓圖片先載入
                    surface_images.append(('',filepath, im.size))
                except:
                    print "X"
        print surface_images
    else :
        print path + " 目錄不存在..."
# 啟動程式
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
    if sys.platform == "win32" or sys.platform == "cygwin" :
        windows = 1
        print "將不支援輸入法"
    else : windows = 0

    main(windows=windows,csv_bool=0)
