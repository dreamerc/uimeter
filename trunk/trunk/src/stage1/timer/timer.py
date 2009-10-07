# encoding: utf8
import timeit

times = 10000
time0 = []

for i in [1,2]:
    
    print "BASIS TEST %d:" % i
    print "start machine test..."


    if(i==1):
        a = 'bcolor=0,key="q"'
    if(i==2):
        a = 'bcolor=40,key="p"'
    t = timeit.Timer('test.run('+ a + ')',"import test")
    t_time = t.timeit(number=times)/times
    print "%.8f sec/pass" % t_time
    time0.append(t_time)


    print "start human test..."

    t = timeit.Timer('test.run(loop=1,'+ a +')',"import test")
    t_time = t.timeit(number=2)/2
    print "%.8f sec/pass" % t_time
    if (t_time<0.1):
        print "test failed. Please restart."
        import sys
        sys.exit()
    time0.append(t_time)

import csv
testout = csv.writer(open('test.csv', 'a'), delimiter=' ',quotechar='|',quoting=2)
testout.writerow(time0)
