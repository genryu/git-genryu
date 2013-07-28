from visual import *

r=5.0
theta=0.0
dtheta=0.01
sun=sphere(color=color.yellow)
earth=sphere(pos=(r,0,0),color=color.blue)
while 1:
    rate(20)
    theta=theta+dtheta
    x=r*cos(theta)
    y=r*sin(theta)
    earth.pos=(x,y,0)