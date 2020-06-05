from numpy import *
from math import *
from ridder import *
from scipy import *
G=6.674*(10**(-11))
M=5.974*(10**24)
m=7.348*(10**22)
R=3.844*(10**8)
w=2.662*(10**(-6))

def f(r):
	f=(r**5)-(2*R*(r**4))+((R**2)*(r**3))+(2*R*r)-(((G*M*(R**2))-(G*M))/(w**2))
	return f
root1=ridder(f,1.,6e8,tol=1.0e-4)
print 'According to the Ridder method, the distance r, from the Earth to the L1 point=',root1,'m; accurate to 12 significant figures'
