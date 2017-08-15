from matplotlib import pyplot as plt
import cv2
import numpy as np

t=np.linspace(-1,0,500)
r=10*(1+t)
x=(r*np.sin(t*2*np.pi))
y=(r*np.cos(t*2*np.pi))

plt.figure(figsize=(6,6))
plt.plot(x,y)
plt.show()
