import scipy
import numpy
import matplotlib.pylab as plt
from scipy import *
from numpy.linalg import solve
import matplotlib.pylab as plt
from scipy import *
from scipy import interpolate
import polyFit
from polyFit import *
Pi=numpy.array([1.0000,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])
hi=numpy.array([0.0000,1.5250,3.0500,4.5750,6.1000,7.6250,9.1500])
h=numpy.linspace(0,9.15,100)
P=scipy.interpolate.barycentric_interpolate(hi,Pi,h)
f=scipy.interpolate.interp1d(hi,Pi, kind='cubic')
Pnew=f(h)

plt.plot(h, Pnew, 'r-',label='Cubic')
plt.plot(h,P,'b--',label='Polynomial fit')
plt.plot(hi,Pi,'go',label='Data Points')
L=polyFit(hi,Pi,2)

Pnew2=L[0]+L[1]*h+L[2]*h**2
plt.plot(h,Pnew2,'y--',label='Quadratic least-squares fit')

plt.title('Relative density of air at various altitudes')
plt.xlabel('Altitude, h, (Km)')
plt.ylabel('Relative density of air, rho')
plt.legend()
plt.show()
h2=2.0000
h5=5.0000
rho2p=scipy.interpolate.barycentric_interpolate(hi,Pi,h2)
rho5p=scipy.interpolate.barycentric_interpolate(hi,Pi,h5)
rho2c=f(h2)
rho5c=f(h5)
PLS2=L[0]+L[1]*2+L[2]*2**2
PLS5=L[0]+L[1]*5+L[2]*5**2
print ("Relative density of air at 2km according to polynomial interpolation=",rho2p)
print ("Relative density of air at 5km according to polynomial interpolation=",rho5p)
print ("Relative density of air at 2km according to cubic spline interpolation=",rho2c)
print ("Relative density of air at 5km according to cubic spline interpolation=",rho5c)
print ("Relative density of air at 2km according to Least-Squares Quadratic=",PLS2)
print ("Relative density of air at 5km according to Least-Squares Quadratic=",PLS5)


