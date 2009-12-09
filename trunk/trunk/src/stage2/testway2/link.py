#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>

'''
五秒延遲是為了讓程式不會一次結束
'''

print u'按 ESC 可退出, 每次間隔會暫停五秒, 請耐心等候'
import time
time.sleep(5)

import run1
run1.main()

time.sleep(5)

import run2
run2.main()

time.sleep(5)

import run
run.main()
