def run(fcolor=31,bcolor=40,loop=0,key="q"):
    print 'Please press \033[0;%d;%dm%s\033[m key' % (fcolor,bcolor,key)

    import sys

    try:
        import msvcrt
        getkey = msvcrt.getch
    except:
        import tty, termios
        TERMIOS = termios
        def getkey():
            file = sys.stdin.fileno()
            mode = termios.tcgetattr(file)
            try:
                tty.setraw(file, TERMIOS.TCSANOW)
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(file, TERMIOS.TCSANOW, mode)
            return ch

    while loop:
        ch = getkey()
        if ch == key:
            break
        print ch,
