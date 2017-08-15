import numpy as np 
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 1000) 
y = (np.sin(x)) 
z = (np.cos(x)) 
     
plt.figure(figsize=(10,4)) 
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2) 
plt.plot(x,z,"b--",label="$cos(x)$",color="blue") 
plt.xlabel("Time(s)") 
plt.ylabel("Volt") 
plt.title("PyPlot Sin/Cos Curve") 
plt.ylim(-1.2,1.2) 
plt.legend() 
plt.show()