import run_kut4 as RK
import numpy 
import matplotlib.pyplot as plt
import scipy
from scipy import integrate 
from scipy.integrate import odeint
#initial conditions
x = 0.#initial value of x
x2=numpy.linspace(0,(10*(numpy.pi)),10000)
y=numpy.array([0.5,0.])	
xStop = (10*(numpy.pi))#final value of x 
h1=0.02
h2=0.05
h3=0.1
E=1.

def G(y,x):#we need to redefine function to use odeint
	E=1.
	G=numpy.zeros(2)
	G[0]=y[1]
	G[1] = -y[0]-E*((y[0]**2)-1)*y[1]
	return G
#plot using scipy.integrate.odeint
	
a=odeint(G,y,x2)
fig5=plt.figure()
plt.plot(a[:,0],a[:,1], label='f(x,t,) using odeint')
plt.title('X vs. Velocity using scipy odeint function, for E=1')
plt.xlabel('dx/dt')
plt.ylabel('x')
plt.show()

