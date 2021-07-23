import numpy as np
from BuildState import StateMatrix
from BuildState import InOutMatrix
from BuildState import initialCond
from SimulationTime import UnitStep
import matplotlib.pyplot as plt
import math 
g = 2#input("Total ordo system : ")
h = 1#input("Total input of the system : ")
g = int(g)

print("State Matrix : ")
A = StateMatrix(g)
print(A)
print("Input Matrix : ")
B = InOutMatrix(g,h)
print(B)
print("Output Matrix : ")
C = InOutMatrix(h,g)
print(C)
print("Initial Condition: ")
x = initialCond(g,1)
dx = np.zeros((int(g),int(h)))

t = input("Simulation time : ")
t = int(t)
ts = float(1)
n = int(float(t / ts))
y = np.zeros(n)
#AA=[0,1,-0.21,-1]
#A=np.reshape(AA,(2,2))
#BB=[0,1]
#B=np.reshape(BB,(2,1))
#CC=[1,0]
#C=np.reshape(CC,(1,2))
#Step Response
U = []
Y = []
timesimul = []
for i in range(0,n):
    u = 1
    x = x + dx
    dx = ((A@x)+(B*u))*ts
    y = (C@x)  
    Y.append(y)   
    U.append(u)
    tt = i
    timesimul.append(tt)
Y_new = np.reshape(Y,(1,n))
yy = Y_new.flat
yo = list(yy)

plt.plot(timesimul,yo,label='Output Signal')
plt.plot(timesimul,U,'--r',label='Step Signal')
plt.legend(loc='lower center',frameon=False)
plt.xlabel("Time(sec)")
plt.ylabel("y(k)")
plt.show()

    
 
