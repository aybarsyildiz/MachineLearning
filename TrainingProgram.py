import numpy as np
import math

def NN(m1,m2,m3,m4,w1,w2,w3,w4,b):
    z = m1*w1 + m2*w2 + m3*w3 + m4*w4 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/1+np.exp(-x)

def cost(b,target):
    return (b-target)**2

def slope(b,target):
    return 2*(b-target)


w1 = np.random.randn()
w2 = np.random.randn()
w3 = np.random.randn()
w4 = np.random.randn()
b = np.random.randn()

target = 1.0
count = 0


z = NN(5.9,3.0,5.1,1.8,w1,w2,w3,w4,b)
print("Before training: ",z," \n\n")
while(math.sqrt((z-target)**2)>=0.001):    #training data loop
    b = b - 0.1 * slope(b,target)
    w1 = w1 - 0.1 * slope(w1,target)
    w2 = w2 - 0.1 * slope(w2,target)
    w3 = w3 - 0.1 * slope(w3,target)
    w4 = w4 - 0.1 * slope(w4,target)
    z = NN(5.9,3.0,5.1,1.8,w1,w2,w3,w4,b)
    count += 1
    print(z)
    print(count,"Times trained.")
    print("Target was: ",target)

array = [0,0,0,0]
print("\nEnter numbers to testout trained program: ")
for i in range(0,4):

    try:
        array[i] = float(input("\nValue: "))

    except ValueError:
        print("You broke it fool!")

z = NN(array[0],array[1],array[2],array[3],w1,w2,w3,w4,b)
print("\nTrained program results: ")
print(z)


if(abs(z-target)>0.1):
    print("\n\nTraining again...\n")
    while(math.sqrt((z-target)**2)>=0.001):    #training data loop
        b = b - 0.1 * slope(b,target)
        w1 = w1 - 0.1 * slope(w1,target)
        w2 = w2 - 0.1 * slope(w2,target)
        w3 = w3 - 0.1 * slope(w3,target)
        w4 = w4 - 0.1 * slope(w4,target)
        z = NN(array[0],array[1],array[2],array[3],w1,w2,w3,w4,b)
        count += 1
        print(z)
        print(count, "Times trained.")
        print("Target was: ",target)
