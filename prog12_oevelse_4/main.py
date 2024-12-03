#main.py
from time import ticks_ms #Nonblocking delays

import NeoPixel
import API
import Relay
import LCD

#nonblocking delay API config
start_time_API = ticks_ms() # Starter tiden
threshold_API = 5000 #5 sekunder

LCD.clear()

while True:
    if ticks_ms() - start_time_API > threshold_API:
        green_power = API.fetch_CO2Emis() #Henter fra API.py
        price_power = API.fetch_elspot() #Henter fra API.py
        #green_power = 55
        if green_power < 50:
            print("Der er grøn strøm:", green_power , "CO2/kwh")
            NeoPixel.OnOff(0,255,0) #Neopixels NeoPixel.py
            Relay.relayOnOff(1) #Relæ Relay.py
        elif green_power >= 50:
            print("Der er ikke grøn strøm:", green_power , " CO2/kwh")
            NeoPixel.OnOff(255,0,0)
            Relay.relayOnOff(0)
        else:
            print("Mistake happend i think")
            
        #     Række,Kolonne, Tekst, Ikon
        LCD.write(0,0, green_power, " CO2/kwh") #LCD display LCD.py
        LCD.write(1,0, price_power, " dkk/mwh") #LCD display LCD.py
            
        start_time_API = ticks_ms() #Resetter timeren