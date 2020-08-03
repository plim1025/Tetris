from threading import Timer
from time import sleep

def setTimeout(callback, time):
    for i in range(time):    
        sleep(time)
        callback()