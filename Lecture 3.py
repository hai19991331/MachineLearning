import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('sample.csv',header=None) #Read data from file

hours=list(map(float,data.values[1: ,0])) # Convert to array
point=list(map(float,data.values[1: ,1])) # Convert to array
w=1
def model(x,w): # the inital model
    return x*w

def loss(w,x,y): # caculate loss
    y_loss=model(x,w)
    return (y_loss-y)**2
def gradient(x,y,w):
    return 2*x*(x*w-y)

def sum_loss(hours,point,w): # caculate sum loss with w
    sum = 0
    for x,y in zip(hours,point):
        sum = sum + loss(w,x,y)
    return sum/len(hours)

loss_array=[]
w_array=[]
def plot_data():
    for w in range(80):
        w_array.append(w)
        loss_array.append(sum_loss(hours,point,w))

def caculate_data(w):
    for count in range(100):
        for x,y in zip(hours,point):
            gd=gradient(x,y,w)
            w=w-0.1*gd
            l = loss(x, y, w)
        print(l)
    return w

plot_data()

print(model(5,caculate_data(w)))
