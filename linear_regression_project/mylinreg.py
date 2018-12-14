import numpy as np
import csv


mssubclassData = open("msslubclass.txt","r")
overallData = open("overallqual.txt","r")
mssubclass = mssubclassData.read().split(",\n")
overallqual = overallData.read().split(",\n")


def FindSum(dataList):
    sum = 0
    for i in range(len(dataList)):
        sum += int(dataList[i])
    return sum



def SquaredSum(dataList):
    sum = 0
    for i in range(len(dataList)):
        sum += int(dataList[i]) ** 2
    return sum



def DataMultiply(dataList1,dataList2):
    sum = 0
    for i in range(len(dataList1)):
        sum += int(dataList1[i]) * int(dataList2[i])
    return sum


def FindSlope(mult,x,y,xsqr):
    return (mult-(x*y)) / (xsqr - (x)**2)

def FindB(mult,x,y,xsqr):
    return ((xsqr * y) - (x * mult)) / (xsqr - (x)**2)




#we are going to find the slope of that function to create a linear regression.
#IDEA: create a line with random values and random slope, then train it untill it fits the data
# y = slope * x + (where the line cuts y axis(we'll call it b))

sumSubClass = FindSum(mssubclass)
sumOverAll = FindSum(overallqual)
sumSquareSubClass = SquaredSum(mssubclass)
sumOverallMultiply = DataMultiply(mssubclass,overallqual)

print("Slope of regression is: ",FindSlope(sumOverallMultiply, sumSubClass, sumOverAll, sumSquareSubClass))
print("\n\nPoint where the regression cuts y axis is: ",FindB(sumOverallMultiply, sumSubClass, sumOverAll, sumSquareSubClass))






