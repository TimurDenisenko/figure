import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10) 
y=[(2/27)*(x**2)-3 for x in x]
x1= np.arange(-10,1)
y1=[0.04*(x**2)-3 for x in x1]
x2=np.arange(-9,-2)
y2=[(2/9)*((x+6)**2) + 1 for x in x2]
x3=np.arange(-3,10)
y3=[(-1/12)*((x-3)**2)+6 for x in x3]
x4=np.arange(5,8.3)
y4=[(1/9)*((x-5)**2) +2 for x in x4]
x5=np.arange(5,8.5)
y5=[(1/8)*((x-7)**2)+1.5 for x in x5]
x6=np.arange(-13,-8)
y6=[-0.75 *((x+11)**2)+6 for x in x6]
x7=np.arange(-15,-12)
y7=[-0.5*((x+13)**2)+3 for x in x7]
x8=np.arange(-15,-9)
y8=[1,1,1,1,1,1]
x9=np.arange(3,5)
y9=[3,3]
plt.title("...")
plt.xlabel("x") 
plt.ylabel("y") 
plt.grid()      
plt.plot(x,y) 
plt.plot(x1,y1) 
plt.plot(x2,y2) 
plt.plot(x3,y3) 
plt.plot(x4,y4) 
plt.plot(x5,y5) 
plt.plot(x6,y6) 
plt.plot(x7,y7) 
plt.plot(x8,y8) 
plt.plot(x9,y9) 
plt.show()

