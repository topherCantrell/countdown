import datetime
import time
import hardware

# This is the target date
date = datetime.datetime.now()
date = date.replace(year=2020,month=3,day=6,hour=9,minute=0,second=0,microsecond=0)

while True:

    # This is now
    now = datetime.datetime.now()
    
    # Number of seconds until target
    delta = date-now
    delta = int(delta.total_seconds())    
    
    # Update the display
    hardware.set_digits(str(delta))
    
    # Wait for changes
    time.sleep(0.5) # Wait for changes (Nyquist rate)
