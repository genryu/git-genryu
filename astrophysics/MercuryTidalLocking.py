
#Michael Jones, 2012

from visual import *
import math
import time

win=700
scene = display(title="Mercury's Orbit", width=win, height=win)

sun = sphere()
sun.pos = vector(0,0,0)
sun.radius = 1.5
sun.color = color.yellow

planet = sphere()
planet.radius = 0.5
planet.color = color.red
planet.a = 5          #Semi-major axis
planet.e = 0.20562    #eccentricity of orbit (0=circle)
planet.pos = (planet.a*(1-planet.e),0,0)
startpos = (planet.a*(1-planet.e),0,0)

planet.sidperiod = 87.97     #Sidereal Period (planet's year, in Earth days)
planet.rotperiod = 58.6462   #Length of the planets sidereal day, in Earth days
parrow = arrow(pos=planet.pos, axis=(-1,0,0))

tlabel=label(pos=(7,7,0), text='', xoffset=0, yoffset=0, box=0)

stheta=0.0
rtheta=0.0
dt=0.04
t=0.0


time.sleep(5)  #Pause for a bit before starting

while 1: #Do the animation
  rate(100)
  t=t+dt
  planet.pos=rotate(startpos, angle=stheta)
  planet.pos.mag=planet.a*(1-planet.e*planet.e)/(1+planet.e*math.cos(stheta))
  parrow.pos=planet.pos
  parrow.axis=rotate((-1,0,0), angle=rtheta)
  tlabel.text="Time (days) %06.2f" % t

  stheta=stheta+(dt/planet.sidperiod)*2*math.pi
  rtheta=rtheta+(dt/planet.rotperiod)*2*math.pi
  if stheta>2*math.pi:
      stheta=stheta-2*math.pi
  if rtheta>2*math.pi:
      rtheta=rtheta-2*math.pi
      
  