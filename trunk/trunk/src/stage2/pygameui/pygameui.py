#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter - pygameui
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

class surface_text:
    def __init__(self):
        print "working..."
        self.text_list = [(u"Hello 中文 World")]
        self.text_color_list = [(127,127,127)]
        self.surface_text_list = [(font.render(self.text_list[0], 1, self.text_color_list[0]))]

    def test():
        print "啟動字型測試 ..." ,
        if pygame.font.get_init() == 1 : print "OK"
        else : print "Failed"

        print "載入字型..." ,
        if windows == 0 :
            try :
                print "嘗試載入 Arphic Uming...",
                font = pygame.font.Font("/usr/share/fonts/truetype/arphic/uming.ttc",24)
                print "成功"
            except :
                print "失敗, 改用系統內建字型"
        else:
            try :
                print "嘗試載入新細明體...",
                font = pygame.font.SysFont("新細明體",24)
                print "成功"
            except :
                print "失敗, 改用系統內建字型"

def main(debug=1, csv_bool=0, windows=0):


    import pygame, sys
    pygame.init()
    
    print "aaa"
    surface_text.test()

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
