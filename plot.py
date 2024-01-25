import numpy as np
import matplotlib.pyplot as plt

#make a random plot and assign different colors to x and y

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.scatter(x,y,c=x,cmap='viridis')
plt.colorbar()
plt.savefig('plot.png')
plt.show()
