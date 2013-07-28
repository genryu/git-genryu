#Demonstration of Mars-Earth oppositions in Mars orbit
#
# Hopelessly out of proper scale, of course, it's meant to illustrate the motion
#
#There's an opposition every 780 days, but the orbits are eccentric, so 'favourable'
#oppositions, where mars is near perihelion, occur about every 15 years or so
#
#Michael Jones 2012

from visual import *
import math
import time

win=700
scene = display(title="Mars Orbit", width=win, height=win, range=2)

sun = sphere()
sun.pos = vector(0,0,0)
sun.radius = 0.2
sun.color = color.yellow

earth = sphere()
earth.radius = 0.07
earth.color = color.blue
earth.a = 1.0          #Semi-major axis
earth.e = 0.017    #eccentricity of orbit (0=circle)
earth.pos = (earth.a*(1-earth.e),0,0)
earthstart = (earth.a*(1-earth.e),0,0)

earth.sidperiod = 365.246     #Sidereal Period (planet's year, in Earth days)
#earth.rotperiod = 1.000   #Length of the planets sidereal day, in Earth days
#eartharrow = arrow(pos=earth.pos, axis=(-0.1,0,0))

mars = sphere()
mars.radius = 0.035
mars.color = color.red
mars.a = 1.5    #semi-major axis
mars.e = 0.093    #eccentricity of orbit (0=circle)
mars.pos = (mars.a*(1-mars.e),0,0)
marsstart = (mars.a*(1-mars.e),0,0)

mars.sidperiod = 686.98     #Sidereal Period (planet's year, in Earth days)
#mars.rotperiod = 1.025949   #Length of the planets sidereal day, in Earth days
#marsarrow = arrow(pos=mars.pos, axis=(-0.1,0,0))

tlabel=label(pos=(0,1.6,0), text='', xoffset=0, yoffset=0, box=0)

autoscale=0
autocenter=0

estheta=0.0
ertheta=0.0
mstheta=0.0
mrtheta=0.0
dt=1.0
t=0.0


time.sleep(1)  #Pause for a bit before starting

while 1: #Do the animation
  rate(100)
  t=t+dt
  earth.pos=rotate(earthstart, angle=estheta)
  earth.pos.mag=earth.a*(1-earth.e*earth.e)/(1+earth.e*math.cos(estheta))
#  eartharrow.pos=earth.pos
#  eartharrow.axis=rotate((-0.1,0,0), angle=ertheta)

  mars.pos=rotate(marsstart, angle=mstheta)
  mars.pos.mag=mars.a*(1-mars.e*mars.e)/(1+mars.e*math.cos(mstheta))
#  marsarrow.pos=mars.pos
#  marsarrow.axis=rotate((-0.1,0,0), angle=mrtheta)


  tlabel.text="Time %06.2f (days) = %6.4f (years) " % (t, t/365.246)

  estheta=estheta+(dt/earth.sidperiod)*2*math.pi
  if estheta>2*math.pi:
      estheta=estheta-2*math.pi
#  ertheta=ertheta+(dt/earth.rotperiod)*2*math.pi
#  if ertheta>2*math.pi:
#      ertheta=ertheta-2*math.pi
  
  mstheta=mstheta+(dt/mars.sidperiod)*2*math.pi
  if mstheta>2*math.pi:
      mstheta=mstheta-2*math.pi
#  mrtheta=mrtheta+(dt/mars.rotperiod)*2*math.pi
#  if mrtheta>2*math.pi:
#      mrtheta=mrtheta-2*math.pi