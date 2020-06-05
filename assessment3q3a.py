import matplotlib.pyplot as plt
import numpy 

Dowdata=numpy.loadtxt('dow.txt')#this loadtxt command accesses data from text files. 

fig1=plt.figure()
plt.plot(Dowdata,'b-',label='Data from text file')
plt.xlabel('t, (Days)')
plt.ylabel('Closing Value')

plt.show()

FT=numpy.fft.rfft(Dowdata,1024)#this sets up the fourier transform of the data,1024 because the original data contains 1024 points.
FT1=numpy.copy(FT)#2copies
FT2=numpy.copy(FT)

#print FT

for i in range(0,513): #loop to make all but first 10% of elements 0.513 because half of 1024+1 (1/2N+1)
	if i<=11: #51=10% of 513 
		continue
	if i>11:
		FT1[i]=0

FT10 = numpy.fft.irfft(FT1) #Inverse transform of new array (with 90% zeros)

plt.plot(FT10,'r-',label='First 2% of Fourier coefficients')
plt.legend()
