#Demonstration of tidal locking in the Moon's orbit
##

from visual import *
import math
import time

win=700
scene = display(title="Moon's Orbit", width=win, height=win)

earth = sphere()
earth.pos = vector(0,0,0)
earth.radius = 1.5
earth.color = color.blue

moon = sphere()
moon.radius = 0.5
moon.color = color.red
moon.a = 5          #Semi-major axis
moon.e = 0.0    #eccentricity of orbit (0=circle)
moon.pos = (moon.a*(1-moon.e),0,0)
startpos = (moon.a*(1-moon.e),0,0)

moon.sidperiod = 27.321661     #Sidereal Period (moon's 'year', in Earth days)
moon.rotperiod = 27.321661   #Length of the planets sidereal day, in Earth days
marrow = arrow(pos=moon.pos, axis=(-1,0,0))

tlabel=label(pos=(7,7,0), text='', xoffset=0, yoffset=0, box=0)

stheta=0.0
rtheta=0.0
dt=0.01
t=0.0


time.sleep(2)  #Pause for a bit before starting

while 1: #Do the animation
  rate(100)
  t=t+dt
  moon.pos=rotate(startpos, angle=stheta)
  moon.pos.mag=moon.a*(1-moon.e*moon.e)/(1+moon.e*math.cos(stheta))
  marrow.pos=moon.pos
  marrow.axis=rotate((-1,0,0), angle=rtheta)
  tlabel.text="Time (days) %06.2f" % t

  stheta=stheta+(dt/moon.sidperiod)*2*math.pi
  rtheta=rtheta+(dt/moon.rotperiod)*2*math.pi
  if stheta>2*math.pi:
      stheta=stheta-2*math.pi
  if rtheta>2*math.pi:
      rtheta=rtheta-2*math.pi
      
  