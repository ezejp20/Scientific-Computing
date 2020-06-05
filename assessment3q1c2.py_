import numpy
import run_kut4 as RK
from run_kut4 import *
import matplotlib.pyplot as plt
from printSoln import *
#F is array containing primes of variables x' and z', y is array of variables x,z
#dx/dt=z
def F(t,y):
	F=numpy.zeros(2)
	F[0]=y[1]
	F[1]=(-w**2)*(y[0]**3)#this is saying z'=-w^2x^3, setting up differential equation.
	return F
y=numpy.array([1,0])#initial conditions 
w=1
t=0.#initial value of t
tStop=20.#final value of t
h=0.001#h=size of steps
freq=1
T,Y=RK.integrate(F,t,y,tStop,h)#need to integrate this is in order to use it
printSoln(T,Y,freq)

fig2=plt.figure()

plt.plot(Y[:,0],Y[:,1], label='Velocity against position for an anharmonic oscillator')#since second column in Y was dx/dt and first column was x.
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.title ('Velocity of oscillator against its position')

def G(t2,y2):
	G=numpy.zeros(2)
	G[0]=y2[1]
	G[1]=(-w**2)*(y2[0])#this is saying z'=-w^2x, setting up differential equation.
	return G
y2=numpy.array([1,0])#initial conditions 
w=1
t2=0.#initial value of t
t2Stop=20.#final value of t
h=0.001#h=size of steps
freq=1
T2,Y2=RK.integrate(G,t2,y2,t2Stop,h)#need to integrate this is in order to use it
printSoln(T2,Y2,freq)

plt.plot(Y2[:,0],Y2[:,1], label='Velocity against position for a harmonic oscillator')#since second column in Y was dx/dt and first column was x.
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('dx/dt')
plt.title ('Velocity of oscillator against its position')
plt.legend()
plt.show()

