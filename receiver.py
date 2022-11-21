import network
import espnow
from machine import Pin
from time import sleep
import neopixel

np = neopixel.NeoPixel(Pin(25), 12)

sta = network.WLAN(network.STA_IF)
sta.active(True)

e = espnow.ESPNow()
e.active(True)

peer = b'\x0C\xB8\x15\xC4\x04\x80'
e.add_peer(peer)

def turn_off_neo():
    for i in range(12):
        np[i] = (0,0,0,0)
        np.write()

turn_off_neo()

while True:
    host, msg = e.recv()
    msg = msg.decode('utf-8')
    if msg:
        j_data_split = msg.split(',')
        print(j_data_split)
        x = j_data_split[0]
        y = j_data_split[1]
        btn = j_data_split[2]
        #op 4095,1900
        #ned 0,1900
        #højre 1900,0
        #venstre 1900,4095
        
        if int(x) > 4000 and int(y) < 2000:
            turn_off_neo()
            np[0] = (255,0,0,255)
            np.write()
        elif int(x) < 100 and int(y) < 2000:
            turn_off_neo()
            np[6] = (255,0,0,255)
            np.write()
        elif int(x) < 2000 and int(y) < 100:
            turn_off_neo()
            np[3] = (255,0,0,255)
            np.write()
        elif int(x) < 2000 and int(y) > 4000:
            turn_off_neo()
            np[9] = (255,0,0,255)
            np.write()
        elif int(btn) == 1:
            turn_off_neo()
            for i in range(12):
                np[i] = (0,255,0,255)
                np.write()
        

            

        


