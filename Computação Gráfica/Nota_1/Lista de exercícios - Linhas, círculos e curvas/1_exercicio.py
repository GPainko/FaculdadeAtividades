import math
from matplotlib import pyplot as plt

p1x = int(input("digite o valor de x do ponto 1: "))
p1y = int(input("digite o valor de y do ponto 1: "))

p2x = int(input("digite o valor de x do ponto 2: "))
p2y = int(input("digite o valor de y do ponto 2: "))

p3x = int(input("digite o valor de x do ponto 3: "))
p3y = int(input("digite o valor de y do ponto 3: "))


#ponto 1 a ponto 2
if p1x == p2x:
    print("Reta vertical")
    y = p1y
    while y<=p2y:
        print(p1x,",",y)
        plt.scatter(p1x,y)
        y+=1

else:
    m = (p2y - p1y)/(p2x - p1x)
    b = p1y - m*p1x

    if m<=1:
        print("reta mais deitada")
        x = p1x
        while x<=p2x:
            y =round(m*x+b)
            print(x,",",y)
            plt.scatter(x,y)
            x+=1

    elif m>1:
        print("reta mais de pé")
        y = p1y
        while y<=p2y:
            x = round((y-b)/m)
            print(x,",",y)
            plt.scatter(x,y)
            y+=1


#ponto 1 a ponto 3
if p1x == p3x:
    print("Reta vertical")
    y = p1y
    while y<=p3y:
        print(p1x,",",y)
        plt.scatter(p1x,y)
        y+=1


else:
    m = (p3y - p1y)/(p3x - p1x)
    b = p1y - m*p1x


    if m<=1:
        print("reta mais deitada")
        x = p1x
        while x<=p3x:
            y =round(m*x+b)
            print(x,",",y)
            plt.scatter(x,y)
            x+=1


    elif m>1:
        print("reta mais de pé")
        y = p1y
        while y<=p3y:
            x = round((y-b)/m)
            print(x,",",y)
            plt.scatter(x,y)
            y+=1


#ponto 2 a ponto 3
if p2x == p3x:
    print("Reta vertical")
    y = p2y
    while y<=p3y:
        print(p2x,",",y)
        plt.scatter(p2x,y)
        y+=1


else:
    m = (p3y - p2y)/(p3x - p2x)
    b = p2y - m*p2x


    if m<=1:
        print("reta mais deitada")
        x = p2x
        while x<=p3x:
            y =round(m*x+b)
            print(x,",",y)
            plt.scatter(x,y)
            x+=1


    elif m>1:
        print("reta mais de pé")
        y = p2y
        while y<=p3y:
            x = round((y-b)/m)
            print(x,",",y)
            plt.scatter(x,y)
            y+=1
plt.show()
