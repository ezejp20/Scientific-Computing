#Assessment 2 Question 4(b)
import scipy as sci
from scipy import integrate as int
import numpy as np

kB=1.3806488*(10**-23)
print "kB is the Botlzmann's constant, =", kB
c=2.99792458*(10**8)
print 'c is the speed of light, =', c
hbar=((6.62606957*(10**-34))/(2*np.pi))
print "h-bar is Planck's constant divided by 2 pi,=", hbar

def I(x):
	I=(x**3)/(np.exp(x)-1)
	return I
integral=sci.integrate.quad(I,0,np.inf)
print 'The integral=', integral

#4(c)
s=((kB**4)/(4.*((np.pi)**2)*(c**2)*(hbar**3)))*integral[0]
print 'sigma equals', s,'W/m^2 K^4'
