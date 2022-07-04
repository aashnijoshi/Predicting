# Importing the required libraries
import ephem
from datetime import datetime, timedelta

# Setting start and end time
curtime = datetime(2001, 1, 1, 0, 0, 0)
endtime = datetime(2100, 12, 31, 23, 59, 59)


moon = ephem.Moon()
sun = ephem.Sun()
observer = ephem.Observer()

# Setting the observer at the centre of the Earth
observer.elevation = -6371000

# Setting pressure as 0 to avoid any effects due to pressure
observer.pressure = 0


while curtime <= endtime:
  
    observer.date = curtime
    moon.compute(observer)
    sun.compute(observer)

    # A lunar eclipse occurs 
    sep = abs((float(ephem.separation(moon, sun))
        / 0.01745329252) - 180)


    if sep < 0.9:
        print(curtime.strftime('%Y/%m/%d %H:%M:%S'), sep)
        curtime += timedelta(days = 1)
    else:
        curtime += timedelta(hours = 1)
