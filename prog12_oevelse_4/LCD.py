# A simple rotary encoder test program
from machine import Pin, PWM
from time import sleep
#LCD hd44780 display - basic kodeeksempel
from machine import Pin
from gpio_lcd import GpioLcd

# Instans af LCD Objekt
lcd = GpioLcd(rs_pin=Pin(27), enable_pin=Pin(25),
              d4_pin=Pin(33), d5_pin=Pin(32),
              d6_pin=Pin(21), d7_pin=Pin(22),
              num_lines=4, num_columns=20)
###########################################################
# CONFIGURATION
# Rotary encoder pins, actual A or B depends the rotary encoder hardware. If backwards swap the pin numpers
pin_enc_a = 36
pin_enc_b = 39

#########################################################################
# OBJECTS
rotenc_A = Pin(pin_enc_a, Pin.IN, Pin.PULL_UP)
rotenc_B = Pin(pin_enc_b, Pin.IN, Pin.PULL_UP)


brightness_Pin = Pin(13, Pin.OUT) #Opretter Pin Objekt
lcd_brightness = PWM(brightness_Pin, duty = 0) #Opretter PWM Objekt og sætter duty til 0

#########################################################################
# VARIABLES and CONSTANTS
enc_state = 0                          # Encoder state control variable

counter = 0                            # A counter that is incremented/decremented vs rotation

CW = 1                                 # Constant clock wise rotation
CCW = -1                               # Constant counter clock wise rotation

max = 10 #
min = 0  # 

###########################################################
# FUNCTIONS
# Rotary encoder truth table, which one to use depends the actual rotary encoder hardware
def re_half_step():
    global enc_state
    
    encTableHalfStep = [
        [0x03, 0x02, 0x01, 0x00],
        [0x23, 0x00, 0x01, 0x00],
        [0x13, 0x02, 0x00, 0x00],
        [0x03, 0x05, 0x04, 0x00],
        [0x03, 0x03, 0x04, 0x10],
        [0x03, 0x05, 0x03, 0x20]]    
    
    enc_state = encTableHalfStep[enc_state & 0x0F][(rotenc_B.value() << 1) | rotenc_A.value()]
 
    # -1: Left/CCW, 0: No rotation, 1: Right/CW
    result = enc_state & 0x30
    if (result == 0x10):
        return CW
    elif (result == 0x20):
        return CCW
    else:
        return 0


def re_full_step():
    global enc_state

    encTableFullStep = [
        [0x00, 0x02, 0x04, 0x00],
        [0x03, 0x00, 0x01, 0x10],
        [0x03, 0x02, 0x00, 0x00],
        [0x03, 0x02, 0x01, 0x00],
        [0x06, 0x00, 0x04, 0x00],
        [0x06, 0x05, 0x00, 0x20],
        [0x06, 0x05, 0x04, 0x00]]

    enc_state = encTableFullStep[enc_state & 0x0F][(rotenc_B.value() << 1) | rotenc_A.value()]
 
    # -1: Left/CCW, 0: No rotation, 1: Right/CW
    result = enc_state & 0x30
    if (result == 0x10):
        return CW
    elif (result == 0x20):
        return CCW
    else:
        return 0
### My Functions
    
def change_lcd_brightness(brightness):
    steps = max - min #Sikre at max og min værdier på rotary encoder passer til LCD brightness
    if brightness == 0:
        lcd_brightness.duty(0)
    else:
        lcd_brightness.duty(int( 1023 / steps * brightness))
    
def write(linje, kolonne, tekst, ikon = "   "):
    lcd.move_to(kolonne, linje) #move_to flytter markøren til 2. kolonne, linje 2
    lcd.putstr(str(tekst) + str(ikon) + "  ")
    
def clear():
    lcd.clear()
    
def start_rotary_encoder_and_LCD_display():
    print("Du kan nu skrue på Rotary Encoderen :)")

    global rotarySteps #Kan åbenbart ikke laves på samme linje
    rotarySteps = 0
    
def run_rotary_encoder():
    global rotarySteps
    #sleep(0.5)
    # Read the rotary encoder
    res = re_full_step()               # or: re_half_step()

    # Direction and counter    
    if res == CW:
        rotarySteps += res
        if rotarySteps >= 10:
             rotarySteps = 10
        change_lcd_brightness(rotarySteps)
    elif res == CCW:
        rotarySteps += res
        if rotarySteps <= 0:
             rotarySteps = 0
        change_lcd_brightness(rotarySteps)
