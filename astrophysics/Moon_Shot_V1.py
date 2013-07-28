from visual.graph import *
#  file  moon_shot_demo.py
#  Earth-Moon Voyage program shell:  Problem 4.2
#
#
# Create objects for display
moonlocation=vector(4.0e8,0,0)
scene=display(title="Voyage to the Moon",
              width=800,height=400,
              center=moonlocation/1.5)
earth = sphere(pos=(0,0,0), radius=6.4e6, color=color.blue)
moon  = sphere( pos=moonlocation,radius=1.76e6, color=color.cyan)
ship = cylinder( axis=(5e6,0,0), radius=2e6)
trail = curve(color=ship.color)
#
# Create Graphs for the energy and work display.
#
energyplot = gdisplay(x=0,y=200,xmin=0,xmax=1.2*moonlocation.x,
                      ymin=-2E10,ymax=2E10,
                      title='Energy versus position',
                      xtitle='Ship Position',
                      ytitle='Energy')
U_Graph=gcurve(color=color.blue)
K_Graph=gcurve(color=color.green)
W_Graph=gcurve(color=color.yellow)
KU_Graph=gcurve(color=color.red)

#
# Set constants
G=6.67E-11
initial_speed = 12500.  #Edit to change initial speed
earth.mass = 6.0e24
moon.mass = 7.0e22        #Edit after getting program going
moon.radius= 1.76e3       #Edit after getting program going
ship.mass = 173
dt= 100
scene.autoscale=0
#
# set initial values for things that change
ship.pos=vector( +(earth.radius+50000),0,0)         #50 km above surface
ship.Vmomentum=vector(ship.mass*initial_speed,0,0)
t = 0
Work=0.
crash=0     #used by program to signal crash
while (crash==0):
    #
    rate(100)
    Vr1=ship.pos-earth.pos
    VForceEarth = -G*earth.mass*ship.mass*ship.pos/mag(ship.pos)**3 
    Vr2=ship.pos-moon.pos
    VForceMoon  = -G*moon.mass*ship.mass*Vr2/mag(Vr2)**3
    ship.Vforce    = VForceEarth + VForceMoon
    Vdelta_r = (ship.Vmomentum/ship.mass)*dt
    ship.Vmomentum = ship.Vmomentum + ship.Vforce*dt
    ship.pos      = ship.pos + Vdelta_r
#
# compute potential energy, kinetic energy, and work done
    UEarthShip= -G*earth.mass*ship.mass/mag(ship.pos) 
    UMoonShip = -G*moon.mass*ship.mass/mag(Vr2)
    U=UEarthShip+UMoonShip
    K = mag(ship.Vmomentum)**2/(2.*ship.mass)
    Work = Work + dot(ship.Vforce,Vdelta_r)
# plot points in graph display
    U_Graph.plot(pos=(ship.x,U))
    K_Graph.plot(pos=(ship.x,K))
    KU_Graph.plot(pos=(ship.x,K+U))
    W_Graph.plot(pos=(ship.x,Work))

    trail.append(pos=ship.pos)
    t=t+dt
    #
    # Check if we fell back to the earth or hit the moon:
    #
    if (mag(ship.pos-earth.pos) <= earth.radius ):
        print("ship crashed back on the earth")
        crash=1
    elif (mag(ship.pos -moon.pos )< (moon.radius+50000) ) :
        print("ship crashed on the moon at time ",t, "seconds")
        print("ship's initial speed ", initial_speed)
        print("ship's final speed ", abs(ship.Vmomentum)/ship.mass)
        crash=1
        
#
#
#
