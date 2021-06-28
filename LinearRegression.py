import pandas as pd
import numpy as np
import math

def mean(data):
    data=data
    n=len(data)
    sum=0
    for i in range(0,n):
        sum=sum+data[i]
    mean= sum/n
    return mean

def Difference(a,b):
    a=a
    b=b
    n=len(a)
    c=[]
    for i in range(0,n):
        c.append(a[i]-b)
    return c

def Square(a):
    a=a
    n=len(a)
    sum_sqr=0
    for i in range(0,n):
        sum_sqr= sum_sqr+(a[i]*a[i])
    return sum_sqr

def multiply(a,b):
    a=a
    b=b
    n=len(a)
    sum_multiply=0
    for i in range(0,n):
        sum_multiply= sum_multiply+(a[i]*b[i])
    return sum_multiply

def r2_score(Y_mean,Y_predict, c):
    Y_mean=Y_mean
    Y_predict=np.array(Y_predict)
    c=c
    sum=0
    n=len(Y_predict)
    for i in range(0,n):
        sum=sum+((Y_predict[i]-Y_mean)*(Y_predict[i]-Y_mean))
    r2_score=sum/c
    print("The R2 Score is:"+str(r2_score))

    
    
def LinearRegression(X_test,Y_test):
    X=X_test
    Y=Y_test
    X_mean=mean(X)
    Y_mean=mean(Y)
    X_mean_Difference= Difference(X,X_mean)
    Y_mean_Difference= Difference(Y,Y_mean)
    X_mean_Difference_Square= Square(X_mean_Difference)
    Y_mean_Difference_Square= Square(Y_mean_Difference)
    Y_mean_Difference_multiply_X_mean_Difference= multiply(Y_mean_Difference,X_mean_Difference)
    #print(Y_mean_Difference_multiply_X_mean_Difference)
    teta_1= (Y_mean_Difference_multiply_X_mean_Difference/X_mean_Difference_Square)
    teta_0= Y_mean - (teta_1*X_mean)
    return [ teta_1,teta_0,Y_mean,X_mean, Y_mean_Difference_Square  ]
    

def predict(X_predict):
    url= "./Real_Estate.csv"
    df = pd.read_csv(url)
    Linear_Reg= LinearRegression(df['area'],df['price'])
    teta_0= Linear_Reg[1]
    teta_1= Linear_Reg[0]
    Y_mean_Difference_Square= Linear_Reg[4]
    X_mean= Linear_Reg[3]
    Y_mean= Linear_Reg[2]
    X_predict=np.array(X_predict)
    Y_predict=[]
    if len(X_predict)>2:
        for i in range(0,len(X_predict)):
            Y_predict.append(math.floor(teta_0+(teta_1*X_predict[i])))
        r2_score(Y_mean,Y_predict, Y_mean_Difference_Square)
        return Y_predict
    else:
        Y_prediction=math.floor(teta_0+(teta_1*X_predict))
        return Y_prediction

url= "./Real_Estate.csv"
df = pd.read_csv(url)
x1= [3422]
predict2=predict(x1)
print("Th price of area whihc is "+str(x1[0])+" sqr feet is:"+str(predict2))
predict=predict(df['area'])

#print("The R2 Score or accuracy of prediction is:"+str(r2_score))