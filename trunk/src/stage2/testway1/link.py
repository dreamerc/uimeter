#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

'''
五秒延遲是為了讓程式不會一次結束
'''

print u'按 ESC 可退出, 每次間隔會暫停三秒, 請耐心等候'
import time
time.sleep(3)

import colorrun01
colorrun01.main()

time.sleep(3)

import colorrun02
colorrun02.main()

time.sleep(3)

import colorrun03
colorrun03.main()

print u"測試點圖形, 請勿按住滑鼠"
time.sleep(3)

import run03
run03.main()
