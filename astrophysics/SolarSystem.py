from visual import *
import solardat
r=reshape(solardat.r,(10,3)) # reshape to array of 10 vectors
v=reshape(solardat.v,(10,3))
Gm=solardat.Gm
nbodyused=len(Gm)
centre=0
a=zeros((nbodyused,3))  # acceleration of ith by jth
planet=range(nbodyused)
for i in range(nbodyused):
    planet[i]=sphere( pos=r[i]-r[centre],radius = 0.2,color=(0,1.5,1) )
    planet[i].trail=curve( color=(1.,7,2))
planet[0].color=color.yellow  # colour the sun...
planet[3].color=(0.7,0.7,1.0)  # colour the earth...
dt=0.1
for nn in range(100*365 ):
    # get new interplanet acceleration vectors
    for i in range(nbodyused):  # N is number of bodies: loop over all
        a[i]=vector(0,0,0) # initialise acceleration of body i to 0
        for j in range(nbodyused): # loop over bodies exerting force
            if i == j: continue  # body doesn't exert force on self
            R = r[i]-r[j]  # displacement
            a[i]=a[i]-Gm[j]*R/mag(R)**3
    # update v and r
    v=v+a*dt
    r=r+v*dt
    # move everything
    for i in range(nbodyused):
        planet[i].pos=r[i]-r[centre]
        planet[i].trail.append( pos=planet[i].pos )


