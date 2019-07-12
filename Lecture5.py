import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('data.csv',header=None) #Read data from file

point=list(map(float,data.values[1: ,0])) # Convert to array
check=list(map(float,data.values[1: ,1])) # Convert to array

def sigmol(z):
    return 1/(1+np.exp(-z))
def sum_loss(point,check,w): # caculate sum loss with w
    sum = 0
    for x,y in zip(point,check):
        y_loss = sigmol(x*w+bios)
        sum = sum + (y*np.log(y_loss) + (1-y)*(np.log(1-y_loss)))
    return -sum/len(point)

def loss(x,y,w):
    y_loss = sigmol(x*w)
    return -(y*np.log(y_loss) + (1-y)*(np.log(1-y_loss)))


def gradient(x,y,w):
    y_pre= sigmol(x*w)
    return (y_pre-y)*x

w_array=[]
l_array=[]
def update_weight(w):
    for count in range(100):
        for x,y in zip(point,check):
            gd=gradient(x,y,w)
            w=w-0.1*gd
            l=loss(x,y,w)
        print(l)
    return w

w=update_weight(1)

fu= 23*w
print(sigmol(fu))
