# plays an alarm after x seconds always enter a value  greater than 1
# the only requirements other than this is VLC media player
import os
import subprocess
import time
while 1:
    current_time = time.localtime()
    if current_time.tm_sec % 2 == 0: # in place of 2 enter value of interval
        pro = subprocess.Popen(['cvlc','alarm.mp3'])  #use cvlc for interface-less mode
        time.sleep(1)
        pro.kill() # killing the process so that only a starting beep can be heard