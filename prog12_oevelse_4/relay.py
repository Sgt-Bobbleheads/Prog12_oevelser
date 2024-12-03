#Relay
from machine import Pin

relay = Pin(17, Pin.OUT)

def relayOnOff(ged):
    relay.value(ged)
    return None