import random
print ( "My name is Ellen Punter and I think I should get 9 marks for this assesment. I have not attempted the bonus part." )
print ( "Academy award nominees 2014:" )

names = ( 'Christian Bale', 'Chiwetel Ejiofor', 'Bruce Dern', 'Matthew McConaughey', 'Leonardo DiCaprio', 'Amy Adams', 'Judi Dench', 'Cate Blanchett', 'Meryl Streep', 'Sandra Bullock', 'Barkhad Abdi', 'Jonah Hill', 'Bradley Cooper', 'Jared Leto', 'Michael Fassbender', 'Sally Hawkins', 'Julia Roberts', 'Jennifer Lawrence', 'June Squibb', "Lupita Nyong'o" )
print ( names )
print ( "Have they been nominated before?" )
ynames= ('Christian Bale', 'Bruce Dern', 'Leonardo Dicaprio', 'Amy Adams', 'Judi Dench', 'Cate Balnchett', 'Meryl Streep', 'Sandra Bullock', 'Jonah Hill', 'Bradley Cooper', 'Julia Roberts', 'Jennifer Lawrence')

for word in ynames:
	print ( word , "Yes" )
nnames= ('Chiwetel Ejiofor', 'Matthew McConaughey', 'Barkhad Abdi', 'Jared Leto', 'Michael Fassbender', 'Sally Hawkins', 'June Squibb', "Lupita Nyong'o")
for word in nnames:
	print ( word , "No" )

print ("Here are 4 Academy Award nominees from 2014")
print ( random.choice(names) )
print ( random.choice(names) )
print ( random.choice(names) )
print ( random.choice(names) )

print "Would you like to see another name?"

a = str(raw_input("Yes/No: "))
b = ("Yes","yes")


while a in b:
	print( random.choice(names) )
	print "Would you like to see another name?"
	a = str(raw_input("Yes/No: "))
else:
	print('Cool')
from random import *
import matplotlib
import numpy
import scipy
from math import *
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

figure (1)

range = np.arange(-3.2,3.2,0.1)
plt.plot(range, norm.pdf(range,0,2))
	
figure (2)

x = np.arange(-5,5,0.1)	
y=cos(x-(pi/2))
plot(x,y)

title( 'Graph of y=cos(x-(pi/2))' )
xlabel( 'This is the x axis' )
ylabel( 'This is the y axis' )

xlim(-5,5)
ylim(-1.2,1.2)

figure (3)

t = np.arange(0,5,0.1)
y=exp(-t)*cos((2*pi(-1))
plot(t,y)

title( 'Damped Oscillator' )
xlabel( 'Time' )
ylabel( 'Displacement' )

y=exp(-t)
plot(t,y,"r--")
plt.show()
