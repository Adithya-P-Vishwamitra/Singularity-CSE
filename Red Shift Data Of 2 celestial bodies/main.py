import pandas as pd
from astropy.constants import c
from astropy.cosmology import Planck18

data = pd.read_csv('star_classification.csv')
data=data[data['redshift']>0].dropna(subset='redshift')

g1=data.iloc[0]
g2=data.iloc[1]

def velocity_distance(z):
    v=((1 + z)**2 - 1) / ((1 + z)**2 + 1)*c.to('km/s').value
    d=Planck18.luminosity_distance(z)
    return v,d

z1=g1['redshift']
z2=g2['redshift']

v1,d1=velocity_distance(z1)
v2,d2=velocity_distance(z2)

print(f"Galaxy 1 (objid={g1['obj_ID']}):")
print(f"  Redshift (z): {z1}")
print(f"  Velocity: {v1:.2f} km/s")
print(f"  Distance: {d1:.2f} \n")

print(f"Galaxy 2 (objid={g2['obj_ID']}):")
print(f"  Redshift (z): {z2}")
print(f"  Velocity: {v2:.2f} km/s")
print(f"  Distance: {d2:.2f} ")

summary = pd.DataFrame({
    'Galaxy': ['Galaxy 1', 'Galaxy 2'],
    'objid': [{g1["obj_ID"]},{g2["obj_ID"]}],
    'Redshift (z)': [z1, z2],
    'Velocity (km/s)': [v1, v2],
    'Distance (Mpc)': [d1.value, d2.value]
})

print(summary)
print('Hence , we can see that more the redshift more farther and faster the galaxies move away from us')