#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

print u"按 ESC 可退出, 更換畫面期間會暫停"
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

time.sleep(3)

print u"測試點圖形"
import run03
run03.main()
