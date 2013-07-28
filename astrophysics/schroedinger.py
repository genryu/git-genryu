"""
Solve the time dependendt Schroedinger equation using the pseudospectral
method.
The boundary conditions are periodic, so that the TDSE is solved on S^1

A gaussian wave packet collides with a square potential barrier.

The packet is plotted as a point on a local complex plane drawn
perpendicular to the circle. 

"""

from visual import *
from numpy import *
import numpy.fft as FFT

hbarc = 1970.0 # in eV.A
mass  = 5.11e5 # electron, eV

#
# Possible parameter sets:
# maxx=2048 -- fast
# V0=800, xmin= 9.8, xmax=10.2
# V0=600, xmin= 9.9, xmax=10.1
#
maxx = 4096*2
steps = 10 # was: 8
beta = 2.0*mass/hbarc**2 
alpha  = 2.0*mass/hbarc 
xsize = 20.0 # Angstrom
Ke=1000.0*3
V0=600.0*3

# reasonable barrier ...
xmin=9.6
xmax=10.4
xmin2=5.2
xmax2=5.5
scale = (maxx-1)/10.0

item=range(maxx-1)

@vectorize
def packet( x, x0, s, k ):
    """
    returns Gaussian wavepacket for position x at time t=0
    """
    p = complex( exp( -(x-x0)**2/(2.0*s*s) ), 0.0 ) \
             * exp( complex( 0.0, k*x ) )
    return p

@vectorize
def potential( x ):
    """
    returns potential at x
    this version: square well/step located between x=4.5 and 5.0
    """
    if( x >= xmin and x < xmax ):
        pot = V0
    else:
        pot = 0.0
    return pot



# main program code starts

k = sqrt( beta*Ke )     # wave number
voverc = 2.0*k/alpha    # speed i.t.o c

# grid steps
dx = xsize/(maxx-1)     # space step size
dt = 0.5*(xsize/voverc)/(maxx-1)    # time step
dk = 2.0*pi/(maxx*dx)
dtheta = 2.0*pi/maxx
phase = pi/2.

# initialize arrays
x=arange(0.0,float(maxx))*dx
theta=arange(0.0,float(maxx))*dtheta
v=potential(x)
psi=packet(x, 5.0, 0.25, k)
K=arange(0.0,float(maxx))*dk
T=K*K/beta
expT=exp( -1.0j*T*dt/hbarc )
expV=exp( -1.0j*v*dt/(2.0*hbarc))
expT[maxx-1:maxx/2-1:-1]=expT[:maxx/2]

# visualize
unitz=0.35 # mapping between window coordinate and unit circle in complex plane
scene=display(width=800,height=500)
xval = cos(theta+phase)
zval = -sin(theta+phase)
yval = abs(psi*conjugate(psi))
barrier = curve(x=xval,y=0.5*v/abs(V0),z=zval,color=color.green,radius=0.005)
gauss = curve( x=xval*(1+unitz*psi.imag), y=unitz*psi.real,
               z=zval*(1+unitz*psi.imag),color=color.yellow,radius=0.005 )
scene.autoscale=0
scene.forward=vector(0.5,-0.4,-1)
# start
#scene.mouse.getclick()  # wait to start ...
t=0
while t<80.0:
    #rate(500)
    psi=expV*(FFT.fft(expT*FFT.ifft(expV*psi)))
    gauss.y=unitz*psi.real
    a=1.0+unitz*psi.imag
    gauss.x=xval*a
    gauss.z=zval*a
    t+=dt