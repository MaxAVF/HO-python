import matplotlib.pyplot as plt
import numpy as np

def pol(x):
  return x**3+x**2-4*x+4

#def der(x):
#  return 3*x**2+2*x-4


x=np.arange(-10,10,0.1)
y=[pol(t) for t in x]
z= np.diff(y)
print(z)
plt.plot(x,y)
plt.plot(x,z,color='red')
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.grid()
plt.legend(['Polinomio','Derivada'])
plt.show()

print(np.c_[x, y].shape)
#with open('pol_data.txt','w') as file:
file= open('pol_data.txt','w')
np.savetxt(file, np.c_[x, y], fmt='%f', delimiter='\t', header="x #f(x)")

file.close()

