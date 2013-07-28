import math
import astronomy as astr

#test date 21/10/1990 for Budapest, Hungary. 14:15 UT

y = 1990
m = 10
d = 21

#time in UT (GMT)
hour = 14
minute = 15
second = 0

t = hour+minute/60.0+second/3600.0

astr.geolon = -19.05 #positive westwards from Greenwich # e.g. Palomar Observatory: 116.8638
astr.geolat = 47.472 #necessary for parallax computations #e.g. Palomar Observatory: 33.356111	
astr.altitude = 100	#necessary for parallax computations #e.g. Palomar Observatory: 1706

#according to Meeus deltaT (is in sec of time) should be added to the t.
# JDE should be calculated from that by calling calcJD
# but this should be the same, since 84400 is the number of seconds in a day
# 24*60*60

JD = astr.calcJD(y, m, d, t)
print ('JD=%f' % JD)

deltaT = astr.calcDeltaT(y, m, d) #deltaT = TD-UT
JDE = JD+deltaT/86400.0
print 'deltaT=%f' % deltaT
#print 'deltaT=%f (in days)' % deltaT/86400.0
print 'JDE=%f' % JDE

#variables that affect the computation (these are the defaults. See the top of astronomy.py for details)
#astr.center = astr.GEO
#astr.coordsystem = astr.ECLIPTICAL
#flags = 0 #nothing
#astr.center = astr.HELIO
astr.flags = astr.FL_NUTATION | astr.FL_ABERRATION# | astr.FL_FK5 | astr.FL_PARALLAX

# The funtions below store the result in the corresponding variables that will be used later in astronomy.py (e.g. calcNutation fills astr.nutinlon and astr.nutinobl)

nutInLon, nutInObl = astr.calcNutation(JDE) #JDE differs from JD by deltaT
print 'nutInLon=%f nuInObl=%f (in ")' % (nutInLon, nutInObl)

#needs nutInObl in ", so it's ok
obl = astr.calcOblEcl(JDE)
#print 'obl=%f (in ")' % obl
obl /= 3600.0 # to degrees
#od, om, os = astr.arcsecToDeg(obl)# result in ". calc arcsecToDeg!!
dd, mm, ss = astr.decToDeg(obl)
print 'obl=%dd %02dm %fs' % (dd, mm, ss)

sidtimeGRW = astr.calcSidTime(JD)
dd, mm, ss = astr.decToDeg(sidtimeGRW) 
print 'siderealtime=%d:%02d:%f (in Greenwich)' % (dd, mm, ss)
#Local sidtime
sidtimeLCL = astr.calcLocalSidTime() #uses astr.sidtime
dd, mm, ss = astr.decToDeg(sidtimeLCL)
print 'siderealtime=%d:%02d:%f (LOCAL)' % (dd, mm, ss)

#MC
MC, ARMC = astr.calcMC(sidtimeLCL)
dd, mm, ss = astr.decToDeg(MC)
print 'MC=%dd %02dm %fs' % (dd, mm, ss)
dd, mm, ss = astr.decToDeg(ARMC)
print 'ARMC=%dd %02dm %fs' % (dd, mm, ss)

rARMC = math.radians(ARMC)
robl = math.radians(obl)

#Asc
Asc = astr.calcAsc(ARMC, obl)
dd, mm, ss = astr.decToDeg(Asc)
print 'Asc=%dd %02dm %fs' % (dd, mm, ss)


#Planets
names = ('Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'AscNode')
for i in range(astr.PLNUM):
	lon, lat, rad = astr.calcPlanet(i, JDE)
	print '*** %s ***' % names[i]
	dd, mm, ss = astr.decToDeg(lon)
	print 'lon=%dd %02dm %f' % (dd, mm, ss)
	dd, mm, ss = astr.decToDeg(lat)
	print 'lat=%dd %02dm %02ds' % (dd, mm, ss)
	print 'rad=%f' % rad
	print

#ecl2equ, equ2hor can be called from here in order to have equatorial or horizontal coords






