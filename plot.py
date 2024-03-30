import numpy as np
import matplotlib.pyplot as plt

#make a random plot and assign different colors to x and y

x = np.random.randn(1000)
y = np.random.randn(1000)

plt.scatter(x,y,c=x,cmap='viridis')
plt.colorbar()
plt.savefig('outputs/plot.png')
plt.show()

plt.plot(x//2, y, 'r')
plt.savefig('outputs/line_plot')
plt.show()


def factoial(n):
    if n<=1:
        return 1
    return n*factoial(n-1)

ls = [factoial(i) for i in range(10)]

plt.plot(ls)
plt.xlabel('n values')
plt.ylabel('factorial values')
plt.title('factorial plot')
plt.savefig('outputs/factorial_plot.png')
plt.show()


