import datetime
import time
import hardware

def int_to_string(value,pad_to,pad_char='*'):
    ret = str(value)
    while len(ret)<pad_to:
        ret = pad_char+ret
    return ret

def show_date(date):
    now_month = int_to_string(date.month,2,'0')
    now_day = int_to_string(date.day,2,'0')
    now_year = int_to_string(date.year,4,'0')
    #
    now_hour = int_to_string(date.hour,2,'0')
    now_minute = int_to_string(date.minute,2,'0')
    now_second = int_to_string(date.second,2,'0')
    
    hardware.set_digits(now_month+now_day+now_year)
    time.sleep(5)
    hardware.set_digits(now_hour+now_minute+now_second)
    time.sleep(5)

date = datetime.datetime.now()
show_date(date)

# This is the target date
date = date.replace(year=2020,month=3,day=6,hour=9,minute=0,second=0,microsecond=0)
show_date(date)

while True:

    # This is now
    now = datetime.datetime.now()
    
    # Total number of seconds until target
    delta = date-now
    delta = int(delta.total_seconds())
    total_seconds = delta
    #print(total_seconds)
    
    # Days, hours, minutes, seconds
    delta_seconds = delta % 60
    delta = int(delta/60)
    delta_minutes = delta % 60
    delta = int(delta/60)
    delta_hours = delta % 24
    delta = int(delta/24)
    delta_days = delta    
    #print('days='+str(delta_days),'hours='+str(delta_hours),'mins='+str(delta_minutes),'secs='+str(delta_seconds))       
    
    # Update the display
    #display = str(total_seconds)    
    display = int_to_string(delta_days,2,'0') + int_to_string(delta_hours,2,'0') + int_to_string(delta_minutes,2,'0') + int_to_string(delta_seconds,2,'0')
    hardware.set_digits(display)
    
    # Wait for changes
    time.sleep(0.5) # Wait for changes (Nyquist rate)
