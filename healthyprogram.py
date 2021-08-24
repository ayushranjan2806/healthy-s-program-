import datetime
import time
import pygame
from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper :
            mixer.music.stop()
            break

def log_now(msg):
    with open ("timetable.txt","a") as f:
        f.write(f"{msg} ,{datetime.now()}")

if __name__ == '__main__':
    watersecs=10
    exsecs=20
    eyessecs=15
    water_time=time.time()
    eye_time=time.time()
    excer_time=time.time()

    while True:
        if time.time()-water_time > watersecs :
            print("water drinking time .enter 'DRANK'to stop the alarm")
            musiconloop('water.mp3.mp3','drank')
            water_time=time.time()
            log_now("drank water at ")
        if time.time()-excer_time > exsecs :
            print("type 'rukaja' to stop the alarm")
            musiconloop('pubg.mp3.mp3','rukaja')
            excer_time=time.time()
            log_now("excerise done at ")
        if time.time()-eye_time > eyessecs:
            print("type 'DONE' to stop the alarm")
            musiconloop('eyes.mp3.mp3','drank')
            eye_time=time.time()
            log_now("eyesmonitoring done at ")    
                



   
    