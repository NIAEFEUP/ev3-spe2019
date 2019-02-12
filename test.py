from base import am, bm, sm
from time import sleep


#Rotação do motor do sensor
sm.move_back(100)

for i in range(2):
    sm.move(500)
    sleep(0.5)
    sm.move(80)
    sleep(0.5)
    sm.move_back(580)
    sleep(0.5)

#Rotação ainda não está certa

sm.reset()