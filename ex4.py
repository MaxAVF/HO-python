import matplotlib.pyplot as plt
import numpy as np


data=np.loadtxt('lista.txt',delimiter=' ')
x=data.T[0]
y=data.T[1]


plt.scatter(x,y)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
for i, txt in enumerate(zip(x,y)):
    plt.annotate(txt, (x[i], y[i]))
plt.show()

