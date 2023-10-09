import time, sys #import the libraries needed

try:
    import bext
except ImportError: #if Bext is not installed, send them to website
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()
print('Press Ctrl-C to stop.')
time.sleep(3) #pause 3 seconds before beginning
indent = 0 #how many spaces to indent
indentIncreasing = True #whether indentation is increasing or not
try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red') #fg is asking 'what color do you want me to make this'
        print('##', end='')
        bext.fg('yellow')
        print('##', end ='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##', end='')

        if indentIncreasing:
            #increase the number of spaces:
            indent = indent + 1
            if indent == 60: # once we reach 60 go back to 0
                indentIncreasing = False

        else:
            #decrease the number of spaces
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

        time.sleep(0.02)
except KeyboardInterrupt:
    sys.exit()
