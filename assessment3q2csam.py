import numpy as np
import matplotlib.pyplot as plt
from printSoln import *
import run_kut4 as rk
import scipy.integrate as scpi

def F(t,y):
	E = 10.0
	F = np.zeros(2)
	F[0] = y[1]
	F[1] = -y[0]-E*(y[0]**2-1)*y[1]
	return F

# y = your variables (eg [x,z]
# F = your differentiated values [x', z']

t = 0.0
y = np.array([0.5,0.])
tStop = 10*(np.pi)
h = 0.02
h1 = 0.05
h2 = 0.1

#plotting for h=0.02
T,X1 = rk.integrate(F,t,y,tStop,h)
Freq=1
Figure1 = plt.figure()
plt.plot(T,X1[:,0])
plt.title('Assessment 3 Q2 plot for h=0.02')
plt.xlabel('Time')
plt.ylabel('X')
plt.grid()

#h=0.05
T,X2 = rk.integrate(F,t,y,tStop,h1)
Fig2 = plt.figure()
plt.plot(T,X2[:,0],'r')
plt.title('Assessment 3 Q2 Plot for h = 0.05')
plt.xlabel('Time')
plt.ylabel('X')
plt.grid()

#h=0.1
T,X3 = rk.integrate(F,t,y,tStop,h2)
Fig3 = plt.figure()
plt.plot(T,X3[:,0],'g')
plt.title('Assessment 3 Q2 plot for h=0.1')
plt.xlabel('Time')
plt.ylabel('X')
plt.grid()
plt.show()

def F2(y,t):
	E = 10.0
	F2 = np.zeros(2)
	F2[0] = y[1]
	F2[1] = -y[0]-E*(y[0]**2-1)*y[1]
	return F2

#print G
tode=np.linspace(0.0,10*np.pi,num=1000)
tode1=np.linspace(0.0,10*np.pi,num=1572)
tode2=np.linspace(0.0,10*np.pi,num=630)
tode3=np.linspace(0.0,10*np.pi,num=316)



q = scpi.odeint(F2,y,tode)
q1 = scpi.odeint(F2,y,tode1)
q2 = scpi.odeint(F2,y,tode2)
q3 = scpi.odeint(F2,y,tode3)
#print q
fig4 = plt.figure()
plt.plot(tode,q[:,0],'m')
plt.title('Assessment 3 Q2 plot for odeint')
plt.xlabel('Time')
plt.ylabel('X')
plt.grid()
#plt.close('all')

#errors
error1 = q1[:,0]-X1[:,0]
error2 = q2[:,0]-X2[:,0]
error3 = q3[:,0]-X3[:,0]

logerror1 = np.log(error1)
logerror2 = np.log(error2)
logerror3 = np.log(error3)

fig5 = plt.figure()
plt.plot(tode1,logerror1,'b',label='Error when h=0.02')
plt.title('Assessment 3 Q2 plot for Error') 
plt.xlabel('Time')
plt.ylabel('ln(Error)')
plt.legend()
plt.grid()
#plt.close('all')


fig6 = plt.figure()
plt.plot(tode2,logerror2,'r',label='Error when h=0.05')
plt.title('Assessment 3 Q2 plot for Error')
plt.xlabel('Time')
plt.ylabel('ln(Error)')
plt.legend()
plt.grid()

fig7 = plt.figure()
plt.plot(tode3,logerror3,'g',label='Error when h=0.1')
plt.title('Assessment 3 Q2 plot for Error')
plt.xlabel('Time')
plt.ylabel('ln(Error)')
plt.legend()
plt.grid()
plt.show()


