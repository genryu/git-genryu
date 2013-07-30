from visual import*
#
#  Physics 33.111 
#  Neptune and Pluto Orbits Program
#
#
#  The planets and Sun objects are defined as Spheres. Note that the
#  radius values are not to scale so that we can actually see
#  them in the plot.
#
#
#  The "breakout code" at the bottom of the loop will allow us to break
#  out of the orbit after a fixed number of orbits.  This can be modified.
#  Note that the program assumes the planets start on the positive x-axis
#  moving in the positive y direction.

#The following "scene" lines setup the display.  Don't worry abou them.
scene.title = 'Planetary Orbit'
scene.width= 800
scene.height= 800
scene.autoscale=0                    ##turn off display autoscaling
scene.range=vector(1.e13,1.e13,1.e13)

#create objects for display
sun = sphere(pos=(0,0,0), radius=2e11, color=color.yellow)

planet1 = sphere(pos=(0,0,0), radius=2.0e11, color=color.cyan)
trail1= curve()

planet2 = sphere(pos=(0,0,0), radius=1.0e11, color=color.blue)
ForceArrow2= arrow(shaftwidth=4.0,color=color.red)
MomentumArrow2= arrow(shaftwidth=4.0,color=color.green)
trail2= curve(color=color.yellow)

# Setup initial conditions and constants before starting loop
#Sun
G=6.7E-11
sun.mass   = 2.0E30
sun.pos = vector(0,0,0)
sun.momentum = vector(0,0,0)

#Neptune
planet1.mass = 1.0E26
OrbitRadius1=4.5e12        
speed1=5469                  ##Edit  PUT IN CORRECT INITIAL SPEED
planet1.pos = vector(OrbitRadius1,0,0)
planet1.momentum = vector(0,speed1*planet1.mass,0)

#Pluto
planet2.mass = 1.3e21
OrbitRadius2= 4.3e12       ##Edit
speed2= 4737+1564               ##Edit  PUT IN CORRECT INITIAL SPEED
planet2.pos = vector(OrbitRadius2,0,0)
planet2.momentum = vector(0,speed2*planet2.mass,0)

print("Planet 1")
print("  initial speed is    ",speed1)
print("  initial position is ",planet1.pos)
print("  initial momentum is ",planet1.momentum)
print("Planet 2")
print("  initial speed is    ",speed2)
print("  initial position is ",planet2.pos)
print("  initial momentum is ",planet2.momentum)


Time=0.0
dt=200000.          #Edit to change time step
NumberOrbits=0      #Used to count number of Orbits
quad=0              #Quandrant flag used to help count orbits
CrashFlag=0         #Set to one if planet gets too near the Sun

while (NumberOrbits<1 and CrashFlag==0):
    rate(5000)
#update Neptune position and momentum
    planet1.force=     -G*(sun.mass*planet1.mass*planet1.pos)/(mag(planet1.pos)**3)    ##Edit
    planet1.momentum = planet1.momentum+ dt*(planet1.force)
    planet1.pos =      planet1.pos + dt*planet1.momentum/planet1.mass
    trail1.append(pos=planet1.pos)           ##add to trajectory "trail"
  
#update Pluto position an momentum
    planet2.force=     -G*sun.mass*planet2.mass*planet2.pos/(mag(planet2.pos)**3)    ##Edit
    planet2.momentum = planet2.momentum+ dt*(planet2.force)
    planet2.pos =      planet2.pos + dt*planet2.momentum/planet2.mass
    trail2.append(pos=planet2.pos)
    
#update Pluto's Momentum and Force Vectors   
    MomentumArrow2.pos=planet2.pos
    MomentumArrow2.axis=planet2.momentum*2e-13
    ForceArrow2.pos=planet2.pos
    ForceArrow2.axis= planet2.force*2.e-4
    
#update Time
    Time=Time+dt

    if (quad==0)and(planet2.pos.x > 0.0)and(planet2.pos.y<0) :
        quad=1
    if (quad==1)and(planet2.pos.x >=0.0)and(planet2.pos.y>=0.0):
        quad=0
        NumberOrbits=NumberOrbits+1
    if (mag(planet1.pos)<2.e11) :
        CrashFlag=1      #got to near the sun.  Set collision flag
#
# Breakout, we are done.
#

if(CrashFlag==1):
    Years=Time/(365*24*60*60)
    print("Crash into Sun at", Time, "seconds ",Years," Years")
else :
    Time=Time/NumberOrbits
    Years=Time/(365*24*60*60)
    print("Number of orbits ", NumberOrbits)
    print("Planet 2 Period (time per orbit is)", Time, "seconds ",Years," Years")
#

    