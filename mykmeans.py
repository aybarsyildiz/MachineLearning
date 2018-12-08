import math
from copy import deepcopy
import random
import numpy as np



checkforend = []
check = [1,1,1]

class1 = []
class2 = []
class3 = []
data = np.array([[5.1,3.5,1.4,0.2],
                [4.9,3.0,1.4,0.2],
                [4.7,3.2,1.3,0.2],
                [4.6,3.1,1.5,0.2],
                [5.0,3.6,1.4,0.2],
                [5.4,3.9,1.7,0.4],
                [4.6,3.4,1.4,0.3],
                [5.0,3.4,1.5,0.2],
                [4.4,2.9,1.4,0.2],
                [4.9,3.1,1.5,0.1],
                [5.4,3.7,1.5,0.2],
                [4.8,3.4,1.6,0.2],
                [4.8,3.0,1.4,0.1],
                [4.3,3.0,1.1,0.1],
                [5.8,4.0,1.2,0.2],
                [5.7,4.4,1.5,0.4],
                [5.4,3.9,1.3,0.4],
                [5.1,3.5,1.4,0.3],
                [5.7,3.8,1.7,0.3],
                [5.1,3.8,1.5,0.3],
                [5.4,3.4,1.7,0.2],
                [5.1,3.7,1.5,0.4],
                [4.6,3.6,1.0,0.2],
                [5.1,3.3,1.7,0.5],
                [4.8,3.4,1.9,0.2],
                [5.0,3.0,1.6,0.2],
                [5.0,3.4,1.6,0.4],
                [5.2,3.5,1.5,0.2],
                [5.2,3.4,1.4,0.2],
                [4.7,3.2,1.6,0.2],
                [4.8,3.1,1.6,0.2],
                [5.4,3.4,1.5,0.4],
                [5.2,4.1,1.5,0.1],
                [5.5,4.2,1.4,0.2],
                [4.9,3.1,1.5,0.1],
                [5.0,3.2,1.2,0.2],
                [5.5,3.5,1.3,0.2],
                [4.9,3.1,1.5,0.1],
                [4.4,3.0,1.3,0.2],
                [5.1,3.4,1.5,0.2],
                [5.0,3.5,1.3,0.3],
                [4.5,2.3,1.3,0.3],
                [4.4,3.2,1.3,0.2],
                [5.0,3.5,1.6,0.6],
                [5.1,3.8,1.9,0.4],
                [4.8,3.0,1.4,0.3],
                [5.1,3.8,1.6,0.2],
                [4.6,3.2,1.4,0.2],
                [5.3,3.7,1.5,0.2],
                [5.0,3.3,1.4,0.2],
                [7.0,3.2,4.7,1.4],
                [6.4,3.2,4.5,1.5],
                [6.9,3.1,4.9,1.5],
                [5.5,2.3,4.0,1.3],
                [6.5,2.8,4.6,1.5],
                [5.7,2.8,4.5,1.3],
                [6.3,3.3,4.7,1.6],
                [4.9,2.4,3.3,1.0],
                [6.6,2.9,4.6,1.3],
                [5.2,2.7,3.9,1.4],
                [5.0,2.0,3.5,1.0],
                [5.9,3.0,4.2,1.5],
                [6.0,2.2,4.0,1.0],
                [6.1,2.9,4.7,1.4],
                [5.6,2.9,3.6,1.3],
                [6.7,3.1,4.4,1.4],
                [5.6,3.0,4.5,1.5],
                [5.8,2.7,4.1,1.0],
                [6.2,2.2,4.5,1.5],
                [5.6,2.5,3.9,1.1],
                [5.9,3.2,4.8,1.8],
                [6.1,2.8,4.0,1.3],
                [6.3,2.5,4.9,1.5],
                [6.1,2.8,4.7,1.2],
                [6.4,2.9,4.3,1.3],
                [6.6,3.0,4.4,1.4],
                [6.8,2.8,4.8,1.4],
                [6.7,3.0,5.0,1.7],
                [6.0,2.9,4.5,1.5],
                [5.7,2.6,3.5,1.0],
                [5.5,2.4,3.8,1.1],
                [5.5,2.4,3.7,1.0],
                [5.8,2.7,3.9,1.2],
                [6.0,2.7,5.1,1.6],
                [5.4,3.0,4.5,1.5],
                [6.0,3.4,4.5,1.6],
                [6.7,3.1,4.7,1.5],
                [6.3,2.3,4.4,1.3],
                [5.6,3.0,4.1,1.3],
                [5.5,2.5,4.0,1.3],
                [5.5,2.6,4.4,1.2],
                [6.1,3.0,4.6,1.4],
                [5.8,2.6,4.0,1.2],
                [5.0,2.3,3.3,1.0],
                [5.6,2.7,4.2,1.3],
                [5.7,3.0,4.2,1.2],
                [5.7,2.9,4.2,1.3],
                [6.2,2.9,4.3,1.3],
                [5.1,2.5,3.0,1.1],
                [5.7,2.8,4.1,1.3],
                [6.3,3.3,6.0,2.5],
                [5.8,2.7,5.1,1.9],
                [7.1,3.0,5.9,2.1],
                [6.3,2.9,5.6,1.8],
                [6.5,3.0,5.8,2.2],
                [7.6,3.0,6.6,2.1],
                [4.9,2.5,4.5,1.7],
                [7.3,2.9,6.3,1.8],
                [6.7,2.5,5.8,1.8],
                [7.2,3.6,6.1,2.5],
                [6.5,3.2,5.1,2.0],
                [6.4,2.7,5.3,1.9],
                [6.8,3.0,5.5,2.1],
                [5.7,2.5,5.0,2.0],
                [5.8,2.8,5.1,2.4],
                [6.4,3.2,5.3,2.3],
                [6.5,3.0,5.5,1.8],
                [7.7,3.8,6.7,2.2],
                [7.7,2.6,6.9,2.3],
                [6.0,2.2,5.0,1.5],
                [6.9,3.2,5.7,2.3],
                [5.6,2.8,4.9,2.0],
                [7.7,2.8,6.7,2.0],
                [6.3,2.7,4.9,1.8],
                [6.7,3.3,5.7,2.1],
                [7.2,3.2,6.0,1.8],
                [6.2,2.8,4.8,1.8],
                [6.1,3.0,4.9,1.8],
                [6.4,2.8,5.6,2.1],
                [7.2,3.0,5.8,1.6],
                [7.4,2.8,6.1,1.9],
                [7.9,3.8,6.4,2.0],
                [6.4,2.8,5.6,2.2],
                [6.3,2.8,5.1,1.5],
                [6.1,2.6,5.6,1.4],
                [7.7,3.0,6.1,2.3],
                [6.3,3.4,5.6,2.4],
                [6.4,3.1,5.5,1.8],
                [6.0,3.0,4.8,1.8],
                [6.9,3.1,5.4,2.1],
                [6.7,3.1,5.6,2.4],
                [6.9,3.1,5.1,2.3],
                [5.8,2.7,5.1,1.9],
                [6.8,3.2,5.9,2.3],
                [6.7,3.3,5.7,2.5],
                [6.7,3.0,5.2,2.3],
                [6.3,2.5,5.0,1.9],
                [6.5,3.0,5.2,2.0],
                [6.2,3.4,5.4,2.3],
                [5.9,3.0,5.1,1.8]]) 


center1 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]
center2 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]#giving centers random values.
center3 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]
    
def CenterCreate():              
    center1 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]
    center2 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]#giving centers random values.
    center3 = [random.uniform(0,10),random.uniform(0,10),random.uniform(0,10),random.uniform(0,10)]
    return center1, center2,center3


def SummaryOfClasses(classw,k):
    temp = 0
    for i in range(0,len(classw)):
        j = k
        temp += classw[i][j]

    return temp
        



def FindDistance(cenvalue1,cenvalue2,cenvalue3,cenvalue4,value1,value2,value3,value4): #a function that uses Euclidean Algorithm to find the distance between values and centers
   return np.sqrt((cenvalue1-value1)**2 + (cenvalue2-value2)**2 + (cenvalue3-value3)**2 + (cenvalue4-value4)**2)


def Update(centeri,classq): #updating new centers
    centers_old = deepcopy(centeri)# store old centers
    centeri[0] = SummaryOfClasses(classq,0)+centeri[0]/(len(classq)+1)
    centeri[1] = SummaryOfClasses(classq,1)+centeri[1]/(len(classq)+1)
    centeri[2] = SummaryOfClasses(classq,2)+centeri[2]/(len(classq)+1)
    centeri[3] = SummaryOfClasses(classq,3)+centeri[3]/(len(classq)+1)
    if (centers_old == centeri): #compare old and new centers
        checkforend.append(1) 
                              #created two arrays, one of them inclues three "1" values, 
                              #whenever the old center values and the new ones are the same, we add "1" to the empty array.
                              #at the end, we check if they are the same.
                              #if arrays are the same, then we exit the program.
                              #so that when clustering over and centers doesn't change anymore,
                              #program exits automaticly.
    
                               
    

def Classing(center1,center2,center3,data):
    #add a loop here to check for datas in matrix named "data"
    for i in range(0,len(data)):
            j = 0
            apclass1 = FindDistance(center1[0],center1[1],center1[2],center1[3],data[i][j],data[i][j+1],data[i][j+2],data[i][j+3])
            apclass2 = FindDistance(center2[0],center2[1],center2[2],center2[3],data[i][j],data[i][j+1],data[i][j+2],data[i][j+3])
            apclass3 = FindDistance(center3[0],center3[1],center3[2],center3[3],data[i][j],data[i][j+1],data[i][j+2],data[i][j+3])
    #finds the distances between centers and values with the function that we have created.
            values = [data[i][j],data[i][j+1],data[i][j+2],data[i][j+3]] #we store values to append them into classes

            if apclass1<apclass2 and apclass1<apclass3:
                if (values in class1)==False: #if class includes the values, it is going to skip the appending part.
                    class1.append(values)
                Update(center1,class1)
            elif apclass2<apclass1 and apclass2<apclass3: #be careful, used numpy logical and
                if ((values in class2)==False):
                    class2.append(values)
                Update(center2,class2)
            elif apclass3<apclass1 and apclass3<apclass2:
                if ((values in class3)==False):
                    class3.append(values)   #we append the values to class where the distance is lowest.
                Update(center3,class3)
            
            
            values = []
            
            

CenterCreate()

while(True):
    CenterCreate()
    if (center1 == center2 or center2 == center3 or center1 == center3):
        continue
    elif (center1 != center2 and center2 != center3 and center1 != center3):
        break


while(True): #check if the centers are the same as their old values.
    
    Classing(center1,center2,center3,data)
    print(center1) #check for instant center movement.
    print(" ")
    print(center2)
    print(" ")
    print(center3)
    print("**")
    if (all(elem in checkforend for elem in [1,1,1,1,1,1,1,1,1,1,1,1]))==True:
        break

print("\n\nRESULTS OF CLUSTERING: ") 
print("Center 1: ",center1)
print("**")
print("Center 2: ",center2)
print("**")
print("Center 3: ",center3)
print("**")


print("\nCLASSES:")
print("\nClass1: ",len(class1))
print("\nClass2: ",len(class2))
print("\nClass3: ",len(class3))



