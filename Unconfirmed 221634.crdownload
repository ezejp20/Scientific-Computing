from run_kut4 import *
import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint

# defining first-order differential equations

def F(t,y):
	E = 10.
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -y[0]-E*((y[0]**2)-1)*y[1]
	return F

#initial conditions:

t = 0.
t2 = np.linspace(0,10*(np.pi),num=1000) # to use for odeint
y = np.array([0.5,0.])
tStop = 10*(np.pi)
h1 = 0.02
h2 = 0.05
h3 = 0.1

#plotting for h=0.02
T,Y1 = integrate(F,t,y,tStop,h1)
Figure1 = pl.figure()
pl.plot(T,Y1[:,0])
pl.title("rk4 displacement x vs. time for h=0.02")
pl.xlabel("Time t")
pl.ylabel("Displacement x")

#h=0.05
T,Y2 = integrate(F,t,y,tStop,h2)
Figure2 = pl.figure()
pl.plot(T,Y2[:,0])
pl.title("rk4 displacement x vs. time for h=0.05")
pl.xlabel("Time t")
pl.ylabel("Displacement x")

#h=0.1
T,Y3 = integrate(F,t,y,tStop,h3)
Figure3 = pl.figure()
pl.plot(T,Y3[:,0])
pl.title("rk4 displacement x vs. time for h=0.1")
pl.xlabel("Time t")
pl.ylabel("Displacement x")

#using odeint

def F2(y,t): #function has to be redefined as odeint wants arguments the other way around
	E = 10.
	F2 = np.zeros(2)
	F2[0] = y[1]
	F2[1] = -y[0]-E*((y[0]**2)-1)*y[1]
	return F2

z = odeint(F2,y,t2)
Figure4 = pl.figure()
pl.plot(t2,z[:,0])
pl.title("solution obtained from odeint")
pl.xlabel("Time t")
pl.ylabel("Displacement x")
pl.show()
