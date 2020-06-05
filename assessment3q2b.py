import run_kut4 as RK
import numpy 
import matplotlib.pyplot as plt
import scipy
from scipy import integrate 
from scipy.integrate import odeint
from printSoln import *



def F(x,y):#setting up our differential equations
	F = numpy.zeros(2)
	F[0]=y[1]#dx/dt
	F[1] = -y[0]-E*(y[0]**2-1)*y[1]#dy/dt
	return F
	
#initial conditions
x = 0.#initial value of x
x2=numpy.linspace(0,(10*(numpy.pi)),10000)
y=numpy.array([0.5,0.])	
xStop = (10*(numpy.pi))#final value of x 
h1=0.02
h2=0.05
h3=0.1
E=10.

X,Y1 = RK.integrate(F,x,y,xStop,h1)#setting up plot for h1
Fig1 = plt.figure()
plt.plot(X,Y1[:,0],'r-',label= 'f(x,t) for h=0.02')
plt.title('Displacement vs. Time using Runge-Kutta method of 4th order for h=0.02')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()


X,Y2 = RK.integrate(F,x,y,xStop,h2)#setting up plot for h2
Fig3 = plt.figure()
plt.plot(X,Y2[:,0],label= 'f(x,t) for h=0.05')
plt.title('Displacement vs. Time using Runge-Kutta method of 4th order for h=0.05')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()


X,Y3 = RK.integrate(F,x,y,xStop,h3)#setting up plot for h3
Fig4 = plt.figure()
plt.plot(X,Y3[:,0],label= 'f(x,t) for h=0.1')
plt.title('Displacement vs. Time using Runge-Kutta method of 4th order for h=0.1')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()

def G(y,x):#we need to redefine function to use odeint
	E=10.
	G=numpy.zeros(2)
	G[0]=y[1]
	G[1] = -y[0]-E*((y[0]**2)-1)*y[1]
	return G
#plot using scipy.integrate.odeint
	
a=odeint(G,y,x2)
fig5=plt.figure()
plt.plot(x2,a[:,0], label='f(x,t,) using odeint')
plt.title('Displacement vs. Time using scipy odeint function')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()

#plot of errors
H1=numpy.linspace(0.,(10*numpy.pi),1572)#10pi/0.02=1571
H2=numpy.linspace(0.,(10*numpy.pi),630)#10pi/0.05=628
H3=numpy.linspace(0.,(10*numpy.pi),316)#10pi/0.1=314
O1=odeint(G,y,H1)
O2=odeint(G,y,H2)
O3=odeint(G,y,H3)
e1=O1[:,0]-Y1[:,0]
e2=O2[:,0]-Y2[:,0]
e3=O3[:,0]-Y3[:,0]#setting up what the errors actually are

le1=numpy.log(e1)
le2=numpy.log(e2)
le3=numpy.log(e3)#creating logs of errors

#for h=0.02:

fig6=plt.figure()
plt.plot(H1,le1,label='Error in Runge-Kutta approximation when h=0.02')
plt.xlabel('t')
plt.ylabel('log(error)')
plt.legend()

#for h=0.05:
fig7=plt.figure()
plt.plot(H2,le2,label='Error in Runge-Kutta approximation when h=0.05')
plt.xlabel('t')
plt.ylabel('log(error)')
plt.legend()

#for h=0.1
fig8=plt.figure()
plt.plot(H3,le3,label='Error in Runge-Kutta approximation when h=0.1')
plt.xlabel('t')
plt.ylabel('log(error)')
plt.legend()

plt.show()

