from visual import *

win=1000
scene = display(title="Orbit", width=win, height=win, range=4e11, forward=(0,-1,0), up=(-1,0,0) )

giant = sphere()
giant.pos = vector(-1e11,0,0)
giant.radius = 2e10
giant.color = color.red
giant.mass = 1e30
giant.p = vector(0, 0, -1e2) * giant.mass

dwarf = sphere()
dwarf.pos = vector(1.5e11,0,0)
dwarf.radius = 1e10
dwarf.color = color.yellow
dwarf.mass = 1e28
dwarf.p = -giant.p

for a in [giant, dwarf]:
  a.orbit = curve(color=a.color, radius = 2e9)

dt = 86400

autoscale=0
autocenter=0

startbar=None
endbar=None
starttick=-1

while 1:
  rate(100)

  dist = dwarf.pos - giant.pos
  force = 6.7e-11 * giant.mass * dwarf.mass * dist / mag(dist)**3
  giant.p = giant.p + force*dt
  dwarf.p = dwarf.p - force*dt

  for a in [giant, dwarf]:
    a.pos = a.pos + a.p/a.mass * dt
    a.orbit.append(pos=a.pos)

  starttick=starttick-1
  if starttick==0:
    endbar=cylinder(pos=giant.pos, axis=(dwarf.pos-giant.pos), radius=3e9)

  if scene.mouse.events:
    m=scene.mouse.getevent()
    if m.click == "left":
      if startbar:
        startbar.visible=0
      startbar=cylinder(pos=giant.pos, axis=(dwarf.pos-giant.pos), radius=3e9)
      if endbar:
        endbar.visible=0
      starttick=50
      
      
