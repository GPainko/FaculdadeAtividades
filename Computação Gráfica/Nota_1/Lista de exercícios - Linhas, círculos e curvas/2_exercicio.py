import math
from matplotlib import pyplot as plt

r =int(input("digite o raio: "))

x = int(input("digite o ponto central: "))

limite = r*math.cos(math.radians(45))
while x<=limite:
    y = round(+math.sqrt(r*r - x*x))

    print("(",x,",",y,")")
    plt.scatter(x,y)
    print("(",y,",",x,")")
    plt.scatter(y,x)
    print("(",y,",",-x,")")
    plt.scatter(y,-x)
    print("(",x,",",-y,")")
    plt.scatter(x,-y)
    print("(",-x,",",-y,")")
    plt.scatter(-x,-y)
    print("(",-y,",",-x,")")
    plt.scatter(-y,-x)
    print("(",-y,",",x,")")
    plt.scatter(-y,x)
    print("(",-x,",",y,")")
    plt.scatter(-x,y)
    x+=1
plt.show()