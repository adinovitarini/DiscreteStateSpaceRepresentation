import numpy as np
def StateMatrix(g):
    a = np.zeros((int(g),int(g)))
    for i in range(0,int(g)):
        for j in range(0,int(g)):
            a[i,j]=input("Enter your value : ")
    return a
def InOutMatrix(g,h):
    b = np.zeros((int(g),int(h)))
    for i in range(0,int(g)):
        for j in range(0,int(h)):
            b[i,j]=input("Enter your value : ")
    return b
def initialCond(g,h):
    x = np.zeros((int(g),int(h)))
    for i in range(0,int(g)):
        for j in range(0,int(h)):
            x[i,j]=input("Enter initial condition of the system : ")
    return x
