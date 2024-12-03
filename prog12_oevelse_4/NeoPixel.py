#NeoPixel
from machine import Pin, ADC
from time import sleep
from neopixel import NeoPixel

n = 24 # number of pixels in the Neopixel ring
p = 12 # pin atached to Neopixel ring

np = NeoPixel(Pin(p, Pin.OUT), n) # create NeoPixel instance

def OnOff(r = 0, g = 0, b = 0):
    for x in range(n):
        np[x] = (r,g,b)
        np.write()
        
def SpecificPixel(neopixel, r = 0, g = 0, b = 0):
    np[neopixel] = (r , g , b)
    np.write()