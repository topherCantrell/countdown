
import RPi.GPIO as GPIO
import spidev  # https://github.com/doceme/py-spidev


PIN_BT_UP   = GPIO_13
PIN_BT_SET  = GPIO_19
PIN_BT_DOWN = GPIO_26

SPI_DEV  = 0 # The pi only has one
SPI_CHAN = 0 # CE0 as chip select

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_BT_UP,  GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(PIN_BT_SET, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(PIN_BT_DOWN,GPIO.IN,GPIO.PUD_DOWN)

spi = spidev.SpiDev()
spi.open(SPI_DEV,SPI_CHAN) 

# Default settings
#spi.bits_per_word = 8
#spi.cshigh = False
#spi.loop = False
#spi.no_cs = False
#spi.lsbfirst = False
#spi.max_speed_hz = 125_000_000
#spi.mode = 0 # CPOL/CPHA -> b00, b01, b10, b11
#spi.threewire = False

spi.lsbfirst = False
spi.bits_per_word = 8
spi.mode = 0
spi.no_cs = True
spi.max_speed_hz = 500000 
spi.threewire = False

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