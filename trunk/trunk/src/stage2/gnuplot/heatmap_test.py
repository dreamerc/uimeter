import random
file = open('heatmap.dat','wb')
for i in range(1000):
    for j in range(1000):
        file.write(str(random.randint(0,1000)) + ' ')
    file.write('\n')
file.close()
