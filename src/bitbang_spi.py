
import RPi.GPIO as GPIO
import time

PIN_CLK  = 19
PIN_CS   = 26
PIN_MOSI = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN_CLK,GPIO.OUT)
GPIO.setup(PIN_CS,GPIO.OUT)
GPIO.setup(PIN_MOSI,GPIO.OUT)

GPIO.output(PIN_CS,GPIO.HIGH)


def bitbang(data):
    data = format(data,"b")
    while len(data)<16:
        data = '0'+data
    pos = 0
    GPIO.output(PIN_CS,GPIO.HIGH)        # CS high (off)
    GPIO.output(PIN_CLK,GPIO.LOW)        # CLK low (off)    
    GPIO.output(PIN_CS,GPIO.LOW)         # Activate chip
    for _ in range(16):
        if data[pos]=='1':
            GPIO.output(PIN_MOSI,GPIO.HIGH)            
        else:
            GPIO.output(PIN_MOSI,GPIO.LOW)            
        GPIO.output(PIN_CLK,GPIO.HIGH)   # CLOCK HIGH
        GPIO.output(PIN_CLK,GPIO.LOW)    # CLOCK LOW
        pos+=1
    time.sleep(0.01)
    GPIO.output(PIN_CS,GPIO.HIGH)        # Deactivate chip
    


bitbang(0x0C01) # Normal mode
bitbang(0x09FF) # BCD all digits
bitbang(0x0F00) # No test
bitbang(0x0AFF) # Full intensity
bitbang(0x0BFF) # All digits on

bitbang(0x0801)
bitbang(0x0702)
bitbang(0x0603)
bitbang(0x0504)
bitbang(0x0405)
bitbang(0x0306)
bitbang(0x0207)
bitbang(0x0108)

#
#
#bitbang(0x01AA)
#bitbang(0x09FF)
#bitbang(0x03AA)
