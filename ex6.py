import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFunc(t, a, b, c):
    return a*t**2+b*t+c

data=np.loadtxt('lista.txt',delimiter=' ')
t=data.T[0]
y=data.T[1]


fitParams, fitCovariances = curve_fit(fitFunc, t, y)
print(fitParams)
print(fitCovariances)

plt.ylabel('Temperature (C)', fontsize = 16)
plt.xlabel('time (s)', fontsize = 16)
#plt.xlim(0,4.1)
# plot the data as red circles with errorbars in the vertical direction
plt.errorbar(t, y, fmt = 'ro', yerr = 0.2)
# now plot the best fit curve and also +- 3 sigma curves
# the square root of the diagonal covariance matrix element 
# is the uncertianty on the corresponding fit parameter.
sigma = [fitCovariances[0,0], fitCovariances[1,1], fitCovariances[2,2] ]
plt.plot(t, fitFunc(t, fitParams[0], fitParams[1], fitParams[2]),\
         t, fitFunc(t, fitParams[0] + sigma[0], fitParams[1] - sigma[1], fitParams[2] + sigma[2]),\
         t, fitFunc(t, fitParams[0] - sigma[0], fitParams[1] + sigma[1], fitParams[2] - sigma[2])\
         )
plt.show()
# save plot to a file
#savefig('dataFitted.pdf', bbox_inches=0, dpi=600)
