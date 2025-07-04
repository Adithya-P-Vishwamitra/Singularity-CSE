import matplotlib.pyplot as plt
from astropy.coordinates import get_body, solar_system_ephemeris
from astropy.time import Time
import astropy.units as u

time = Time(['2024-11-01']) + range(180) * u.day  

ra = []

with solar_system_ephemeris.set('jpl'):
    for t in time:
        mars = get_body('mars', t)
        ra.append(mars.ra.deg)


retrograde_days = []
for i in range(1, len(ra)):
    if ra[i] < ra[i - 1]<ra[i-2]: 
        retrograde_days.append(time[i].iso)

plt.figure(figsize=(10, 5))
for x,y in zip(time.datetime,ra):
    if Time(x).iso in retrograde_days:
        plt.plot(x, y, 'ro') 
    else:
        plt.plot(x, y, 'bo') 

plt.title("Retrograde Motion of Mars")
plt.xlabel("Date")
plt.ylabel("Right Ascension")
plt.show()
