print("Started Optimizing JWL------------------------")
print("Using Levenberg Marquardt Algorithm")
import pandas as pd
import numpy as np
#import scipy
from scipy.optimize import curve_fit
path=input("Enter Complete Path Of File : ")
df=pd.read_csv(path)
def JWL(V,r1,r2,A,B,C):
  w=0.5
  return A*(np.exp(-(r1*V)))+B*(np.exp(-(r2*V)))+C*V**(-w-1)

def JWL_slope(V,r1,r2,A,B,C):
  w=0.5
  return -A*r1*(np.exp(-(r1*V)))-r2*B*(np.exp(-(r2*V)))-(w+1)*C*V**(-(w+2))
P=df.P/1e+6
V=df.V
def optim():
    opt,cov=curve_fit(JWL,V,P,(1,2,23247,33548,4324),method='lm')
    return opt

opt=optim()
print("Optimization Successfull----------------------------")
print("Optimized Parameter")
print("r1:"+str(opt[0]))
print("r2:"+str(opt[1]))
print("A:"+str(opt[2]))
print("B:"+str(opt[3]))
print("C:"+str(opt[4]))
#print("w:"+str(opt[5]))
pred=JWL(V,*opt)
d=pd.DataFrame()
opt1=[4.10,1.0,5.814e+5,0.068e+5,0.00234e+05]
d["Pressure(Mpa)"]=P
d["Volume(v/v0)"]=V
d["Predicted Pressure"]=pred
d["Error"]=pred-P
d["slope"]=JWL_slope(V,*opt)
d["slope2"]=JWL_slope(V,*opt1)
print(d)
import matplotlib.pyplot as plt 
plt.plot(V,pred)
plt.scatter(V,pred)

plt.plot(V,JWL(V,*opt1))
plt.scatter(V,JWL(V,*opt1))
plt.scatter(0.754142,39326.78)
plt.xscale('log')
plt.show()

print()
a="Enter Any number to exit"
input(a)