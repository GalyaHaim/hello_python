#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
x = np.linspace(-2, 2, 400)
y = x * x

#%
plt.plot(x, y)
plt.title('Graph of x*x')
plt.xlabel('x')
plt.ylabel('x*x')
plt.grid(True)
plt.show()

#%%
arr = np.arange(0,100, 0.5)
print('hello world')
print(f'This is my new numpy array: {arr}')
# %%
