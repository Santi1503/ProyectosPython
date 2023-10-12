from pynput.mouse import Listener

def writeToFile(x,y):
    print('Current position of mouse {0}'.format((x,y)))

with Listener(on_move=writeToFile) as l:
    l.join()