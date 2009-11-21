#!/usr/bin/env python
# -*- coding: utf-8 -*-
#UIMeter - heatmap
#License: GNU General Public License v2
#Author: Shan-Bin Chen <dreamerwolf.tw@gmail.com>
#Ref : http://gnuplot.sourceforge.net/demo_4.3/heatmaps.html

try:
    print '嘗試載入 Gnuplot ...',
    import Gnuplot
    print '成功'
except:
    print '載入 Gnuplot 失敗... 檢查原因'
    try:
        import numpy
    except:
        print '請先安裝 NumPy, 再安裝 Gnuplot'

g = Gnuplot.Gnuplot(debug=1)

# 從 http://gnuplot.sourceforge.net/demo_4.3/heatmaps.html 來的 demo
g.title("Heat Map generated from a file containing Z values only")

g('unset key')
g('set tic scale 0')

# Color runs from white to green
g('set palette rgbformula -7,2,-7')
g('set cbrange [0:5]')
g('set cblabel "Score"')
g('unset cbtics')

g('set xrange [-0.5:4.5]')
g('set yrange [-0.5:4.5]')

g('set view map')
g("splot '-' matrix with image")
g('''
5 4 3 1 0
2 2 0 0 1
0 0 0 1 0
0 0 0 2 3
0 1 2 4 3
''')
g('e')
raw_input('Please press return to exit...\n')
