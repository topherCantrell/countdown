import RPi.GPIO as GPIO
import spidev  # https://github.com/doceme/py-spidev

PIN_BT_UP   = 13
PIN_BT_SET  = 19
PIN_BT_DOWN = 26

SPI_DEV  = 0 # The pi only has one
SPI_CHAN = 0 # CE0 as chip select

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_BT_UP,  GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(PIN_BT_SET, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(PIN_BT_DOWN,GPIO.IN,GPIO.PUD_DOWN)

spi = spidev.SpiDev()
spi.open(SPI_DEV,SPI_CHAN) 

spi.max_speed_hz = 1000000 # 10MHz max

#spi.xfer([0xFF,0x00])

#spi.xfer2([0x0C,0x01]) # Normal mode
#spi.xfer2([0x09,0xFF]) # BCD all digits
#spi.xfer2([0x0F,0x00]) # No test
#spi.xfer2([0x0A,0xFF]) # Full intensity
#spi.xfer2([0x0B,0xFF]) # All digits on
#spi.xfer2([0x08,0x09])
#spi.xfer2([0x07,0x02])
#spi.xfer2([0x06,0x03])
#spi.xfer2([0x05,0x04])
#spi.xfer2([0x04,0x05])
#spi.xfer2([0x03,0x06])
#spi.xfer2([0x02,0x07])
#spi.xfer2([0x01,0x09])

def get_button_up():
    return GPIO.input(PIN_BT_UP)

def get_button_set():
    return GPIO.input(PIN_BT_SET)

def get_button_down():
    return GPIO.input(PIN_BT_DOWN)

def send_to_display(data:list):
    spi.writebytes2(data)

def set_segments(data:list):
    # Raw segment/period data -- 8 values
    pass

def set_digits(data:list):
    # Data for 8 digits.
    # List of tuples: (num,True) -- digit value and period
    pass
