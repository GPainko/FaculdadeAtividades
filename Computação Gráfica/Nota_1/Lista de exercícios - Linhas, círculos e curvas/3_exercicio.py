import math
from matplotlib import pyplot as plt

raio = int(input('\nInsira um valor para o raio da circunferência: '))
print('Raio da circunferência inserido:', raio, '\n')

valorX = int(input('Insira um valor para x do ponto a ser analisado: '))
valorY = int(input('Insira um valor para y do ponto a ser analisado: '))
print('Ponto: (', valorX, ',', valorY, ')')
print('Ponto Central: ( 0 , 0 )\n')




x = 0 
limite = raio * math.cos(math.radians(45))

bool_pertence = False 

while x <= limite:
    y = round(+math.sqrt(raio * raio - x * x))
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
    print()


    if valorX <= x and valorY <= y:
        bool_pertence = True 
        break
    elif valorX <= x and valorY <= -y:
        bool_pertence = True
        break
    elif valorX <= -x and valorY <= y:
        bool_pertence = True
        break
    elif valorX <= -x and valorY <= -y:
        bool_pertence = True
        break
    elif x > limite:
        print('O ponto não pertence.')
    else:
        pass

    x += 1


if bool_pertence == True:
    print('O ponto pertence.')
else:
    print('O ponto não pertence.')

plt.scatter(valorX,valorY)
plt.show()