#Trabalho realizado por Guilherme Painko e Pedro Cassenote

import numpy as np
import math
from matplotlib import pyplot as plt

#limites da window
#xminw = -1, xmaxw = 1, yminw = -1 e ymaxw = 1.
xminw = -1
yminw = -1
xmaxw = 1
ymaxw = 1

#limites da viewport
# xminv = 0, xmaxv = 500, yminv = 0 e ymaxv = 500.
xminv = 0
yminv = 0
xmaxv = 500
ymaxv = 500

def mapeamento(p):
    plt.xlim(xminv, xmaxv)
    plt.ylim(yminv, ymaxv)
    xvp = (((p[0] - xminw)*(xmaxv - xminv))/(xmaxw - xminw)) + xminv
    yvp = (((p[1] - yminw)*(ymaxv - yminv))/(ymaxw - yminw)) + yminv
    print("(",xvp,",",yvp,")")
    plt.scatter(xvp, yvp)

def mostraPontos(p1, p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8, p9, p10, p11, p12, p13, p14, p15, 
             p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, 
             p29, p30, p31, p32, p33):

    print(p1)
    print(p2)
    print(p3)
    print(p4)
    print(p5)
    print(p6)
    print(p7)
    print(p8)
    print(p9)
    print(p10)
    print(p11)
    print(p12)
    print(p13)
    print(p14)
    print(p15)
    print(p16)
    print(p17)
    print(p18)
    print(p19)
    print(p20)
    print(p21)
    print(p22)
    print(p23)
    print(p24)
    print(p25)
    print(p26)
    print(p27)
    print(p28)
    print(p29)
    print(p30)
    print(p31)
    print(p32)
    print(p33) 

print('\nAplicação que implementa um pipeline de visualização 3D completo\n')

p1 = np.array([0.000000,-1.000000,-1.000000,1.0])
p2 = np.array([0.195090,-1.000000,-0.980785,1.0])
p3 = np.array([0.382683,-1.000000,-0.923880,1.0])
p4 = np.array([0.555570,-1.000000,-0.831470,1.0])
p5 = np.array([0.707107,-1.000000,-0.707107,1.0])
p6 = np.array([0.831470,-1.000000,-0.555570,1.0])
p7 = np.array([0.923880,-1.000000,-0.382683,1.0])
p8 = np.array([0.980785,-1.000000,-0.195090,1.0])
p9 = np.array([1.000000,-1.000000,0.000000,1.0])
p10 = np.array([0.980785,-1.000000,0.195090,1.0])
p11 = np.array([0.923880,-1.000000,0.382683,1.0])
p12 = np.array([0.831470,-1.000000,0.555570,1.0])
p13 = np.array([0.707107,-1.000000,0.707107,1.0])
p14 = np.array([0.555570,-1.000000,0.831470,1.0])
p15 = np.array([0.382683,-1.000000,0.923880,1.0])
p16 = np.array([0.195090,-1.000000,0.980785,1.0])
p17 = np.array([-0.000000,-1.000000,1.000000,1.0])
p18 = np.array([-0.195090,-1.000000,0.980785,1.0])
p19 = np.array([-0.382683,-1.000000,0.923880,1.0])
p20 = np.array([-0.555570,-1.000000,0.831470,1.0])
p21 = np.array([-0.707107,-1.000000,0.707107,1.0])
p22 = np.array([-0.831469,-1.000000,0.555570,1.0])
p23 = np.array([-0.923880,-1.000000,0.382684,1.0])
p24 = np.array([-0.980785,-1.000000,0.195090,1.0])
p25 = np.array([-1.000000,-1.000000,-0.000000,1.0])
p26 = np.array([-0.980785,-1.000000,-0.195090,1.0])
p27 = np.array([-0.923879,-1.000000,-0.382684,1.0])
p28 = np.array([-0.831470,-1.000000,-0.555570,1.0])
p29 = np.array([-0.707107,-1.000000,-0.707107,1.0])
p30 = np.array([-0.555570,-1.000000,-0.831470,1.0])
p31 = np.array([-0.382683,-1.000000,-0.923880,1.0])
p32 = np.array([-0.195090,-1.000000,-0.980785,1.0])
p33 = np.array([0.000000,1.000000,0.000000,1.0])

#inicialização das matrizes
translacao = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
rotx = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
roty = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
rotz = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
escala = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


translacaoCam = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -10],
        [0, 0, 0, 1]
    ])


rotxCam = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
rotyCam = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
rotzCam = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

fovy = math.radians(67.0)
aspect = 1.0
zNear = 0.1
zFar = 100

a = 1/(math.tan(fovy/2) * aspect)
b = 1/(math.tan(fovy/2))
c = (zFar+zNear)/(zNear-zFar)
d = (2*(zFar*zNear))/(zNear-zFar)

matrizProjecao = np.array([
    [a, 0, 0, 0],
    [0, b, 0, 0],
    [0, 0, c, d],
    [0, 0, -1, 0]
])

print("\nCoordenadas do modelo")
mostraPontos(p1, p2 ,p3 ,p4 ,p5 ,p6 ,p7 ,p8, p9, p10, p11, p12, p13, p14, p15, 
             p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, 
             p29, p30, p31, p32, p33)

while True:
    print("1. Manipular o objeto")
    print("2. Manipular a Câmera")
    print("3. Modificar projeção")
    print("4. Modificar mapeamento:") 
    print("5. Visualizar objeto:")
    print("6. Calculos:")  
    print("9. Sair:")  

    op = int(input("Digite a opção: "))
    if op == 1:
            print("1. Translação")
            print("2. Escala")
            print("3. Rotação em X")
            print("4. Rotação em Y:") 
            print("5. Rotação em Z:")  

            op = int(input("Digite a opção: "))
          

            if op == 1:

                tx = float(input("digite o valor de tx: "))
                ty = float(input("digite o valor de ty: "))
                tz = float(input("digite o valor de tz: "))
                translacao = np.array([
                    [1, 0, 0, tx],
                    [0, 1, 0, ty],
                    [0, 0, 1, tz],
                    [0, 0, 0, 1]
                ])
            elif op == 2:           

                sx = float(input("digite o valor de tx: "))
                sy = float(input("digite o valor de ty: "))
                sz = float(input("digite o valor de tz: "))
                escala = np.array([
                    [sx, 0, 0, 0],
                    [0, sy, 0, 0],
                    [0, 0, sz, 0],
                    [0, 0, 0, 1]    
                ])

            elif op == 3:      

                angulo = float(input("digite o angulo: "))
                angx = math.radians(angulo)
                rotx = np.array([
                    [1, 0, 0, 0],
                    [0, math.cos(angx), -math.sin(angx), 0],
                    [0, math.sin(angx), math.cos(angx), 0],
                    [0, 0, 0, 1]    
                ])

            elif op == 4:  

                angulo = float(input("digite o angulo: "))
                angy = math.radians(angulo)
                roty = np.array([
                    [math.cos(angy), 0, math.sin(angy), 0],
                    [0, 1, 0, 0],
                    [-math.sin(angy), 0, math.cos(angy), 0],
                    [0, 0, 0, 1]    
                ])

            elif op == 5: 

                angulo = float(input("digite o angulo: "))
                angz = math.radians(angulo)
                rotz = np.array([
                    [math.cos(angz), -math.sin(angz), 0, 0],
                    [math.sin(angz), math.cos(angz), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]    
                ])

            else:
                print("Opção inválida") 

            

    elif op == 2:
        print("1. Translação")
        print("2. Rotação em X")
        print("3. Rotação em Y:") 
        print("4. Rotação em Z:")

        op = int(input("Digite a opção: "))

        if op == 1:
            txCam = float(input("digite o valor de txCam: "))
            tyCam = float(input("digite o valor de tyCam: "))
            tzCam = float(input("digite o valor de tzCam: "))

            #é a cena que se move em torno da câmera
            translacaoCam = np.array([
            [1, 0, 0, -txCam],
            [0, 1, 0, -tyCam],
            [0, 0, 1, -tzCam],
            [0, 0, 0, 1]
            ])

        elif op == 2:
            #rotação da câmera
            #rotacao em x
            angxCam = float(input("digite o valor do ângulo x: "))
            angxCam = math.radians(-angxCam)
            rotxCam = np.array([
            [math.cos(angxCam), 0, math.sin(angxCam), 0],
            [0, 1, 0, 0],
            [-math.sin(angxCam), 0, math.cos(angxCam), 0],
            [0, 0, 0, 1]    
            ])
            
        elif op == 3:
            #rotação da câmera
            #rotacao em y
            angyCam = float(input("digite o valor do ângulo y: "))
            angyCam = math.radians(-angyCam)
            rotyCam = np.array([
            [math.cos(angyCam), 0, math.sin(angyCam), 0],
            [0, 1, 0, 0],
            [-math.sin(angyCam), 0, math.cos(angyCam), 0],
            [0, 0, 0, 1]    
            ])

        elif op == 4:
            #rotação da câmera
            #rotacao em z
            angzCam = float(input("digite o valor do ângulo z: "))
            angzCam = math.radians(-angzCam)
            rotzCam = np.array([
            [math.cos(angzCam), 0, math.sin(angzCam), 0],
            [0, 1, 0, 0],
            [-math.sin(angzCam), 0, math.cos(angzCam), 0],
            [0, 0, 0, 1]    
            ])

        else:
            print("Opção inválida") 
    elif op == 3:

          print("1. Projeção perspectiva")
          print("2.  Projeção paralela")

          op = int(input("Digite a opção: "))

          if op == 1:
              fovy = math.radians(67.0)
              aspect = 1.0
              zNear = 0.1
              zFar = 100

              a = 1/(math.tan(fovy/2) * aspect)
              b = 1/(math.tan(fovy/2))
              c = (zFar+zNear)/(zNear-zFar)
              d = (2*(zFar*zNear))/(zNear-zFar)

              matrizProjecao = np.array([
                  [a, 0, 0, 0],
                  [0, b, 0, 0],
                  [0, 0, c, d],
                  [0, 0, -1, 0]
              ])
              print(matrizProjecao)
          elif op == 2:
              print("bom dia")
          else:
              print("Opção inválida") 
    elif op == 4:
          print("1. Window")
          print("2. Viewport")
          if op == 1:

              xminw = int(input("valor do xminw:"))
              xmaxw = int(input("valor do xmaxw:"))
              yminw = int(input("valor do yminw:"))
              ymaxw = int(input("valor do ymaxw:"))
              
          elif op == 2:

              xminv = int(input("valor do xminv:"))
              xmaxv = int(input("valor do xmaxv:"))
              yminv = int(input("valor do yminv:"))
              ymaxv = int(input("valor do ymaxv:"))
          else:
              print("Opção inválida")
    elif op ==6 :
        #Calculos objeto
        rotacao = rotz.dot(roty.dot(rotx))
        matrizModelo = escala.dot(rotacao.dot(translacao))

        p1u = matrizModelo.dot(p1)
        p2u = matrizModelo.dot(p2)
        p3u = matrizModelo.dot(p3)
        p4u = matrizModelo.dot(p4)
        p5u = matrizModelo.dot(p5)
        p6u = matrizModelo.dot(p6)
        p7u = matrizModelo.dot(p7)
        p8u = matrizModelo.dot(p8)
        p9u = matrizModelo.dot(p9)
        p10u = matrizModelo.dot(p10)
        p11u = matrizModelo.dot(p11)
        p12u = matrizModelo.dot(p12)
        p13u = matrizModelo.dot(p13)
        p14u = matrizModelo.dot(p14)
        p15u = matrizModelo.dot(p15)
        p16u = matrizModelo.dot(p16)
        p17u = matrizModelo.dot(p17)
        p18u = matrizModelo.dot(p18)
        p19u = matrizModelo.dot(p19)
        p20u = matrizModelo.dot(p20)
        p21u = matrizModelo.dot(p21)
        p22u = matrizModelo.dot(p22)
        p23u = matrizModelo.dot(p23)
        p24u = matrizModelo.dot(p24)
        p25u = matrizModelo.dot(p25)
        p26u = matrizModelo.dot(p26)
        p27u = matrizModelo.dot(p27)
        p28u = matrizModelo.dot(p28)
        p29u = matrizModelo.dot(p29)
        p30u = matrizModelo.dot(p30)
        p31u = matrizModelo.dot(p31)
        p32u = matrizModelo.dot(p32)
        p33u = matrizModelo.dot(p33)

        print("\nCoordenadas do mundo")
        mostraPontos(p1u, p2u ,p3u ,p4u ,p5u ,p6u ,p7u ,p8u, p9u, p10u, p11u, p12u, p13u, p14u, p15u, 
                p16u, p17u, p18u, p19u, p20u, p21u, p22u, p23u, p24u, p25u, p26u, p27u, p28u, 
                p29u, p30u, p31u, p32u, p33u)
        #Calculos Camera

        rotacaocam = rotzCam.dot(rotyCam.dot(rotxCam))
        matrizVisualizacaocam = rotacao.dot(translacaoCam)

        p1v = matrizVisualizacaocam.dot(p1u)
        p2v = matrizVisualizacaocam.dot(p2u)
        p3v = matrizVisualizacaocam.dot(p3u)
        p4v = matrizVisualizacaocam.dot(p4u)
        p5v = matrizVisualizacaocam.dot(p5u)
        p6v = matrizVisualizacaocam.dot(p6u)
        p7v = matrizVisualizacaocam.dot(p7u)
        p8v = matrizVisualizacaocam.dot(p8u)
        p9v = matrizVisualizacaocam.dot(p9u)
        p10v = matrizVisualizacaocam.dot(p10u)
        p11v = matrizVisualizacaocam.dot(p11u)
        p12v = matrizVisualizacaocam.dot(p12u)
        p13v = matrizVisualizacaocam.dot(p13u)
        p14v = matrizVisualizacaocam.dot(p14u)
        p15v = matrizVisualizacaocam.dot(p15u)
        p16v = matrizVisualizacaocam.dot(p16u)
        p17v = matrizVisualizacaocam.dot(p17u)
        p18v = matrizVisualizacaocam.dot(p18u)
        p19v = matrizVisualizacaocam.dot(p19u)
        p20v = matrizVisualizacaocam.dot(p20u)
        p21v = matrizVisualizacaocam.dot(p21u)
        p22v = matrizVisualizacaocam.dot(p22u)
        p23v = matrizVisualizacaocam.dot(p23u)
        p24v = matrizVisualizacaocam.dot(p24u)
        p25v = matrizVisualizacaocam.dot(p25u)
        p26v = matrizVisualizacaocam.dot(p26u)
        p27v = matrizVisualizacaocam.dot(p27u)
        p28v = matrizVisualizacaocam.dot(p28u)
        p29v = matrizVisualizacaocam.dot(p29u)
        p30v = matrizVisualizacaocam.dot(p30u)
        p31v = matrizVisualizacaocam.dot(p31u)
        p32v = matrizVisualizacaocam.dot(p32u)
        p33v = matrizVisualizacaocam.dot(p33u)

        print("\nCoordenadas de visualização")
        mostraPontos(p1v, p2v, p3v, p4v, p5v,p6v,p7v,p8v, p9v, p10v, p11v, p12v, p13v, p14v, p15v, 
                p16v, p17v, p18v, p19v, p20v, p21v, p22v, p23v, p24v, p25v, p26v, p27v, p28v, 
                p29v, p30v, p31v, p32v, p33v)

        p1p = matrizProjecao.dot(p1v)
        p2p = matrizProjecao.dot(p2v)
        p3p = matrizProjecao.dot(p3v)
        p4p = matrizProjecao.dot(p4v)
        p5p = matrizProjecao.dot(p5v)
        p6p = matrizProjecao.dot(p6v)
        p7p = matrizProjecao.dot(p7v)
        p8p = matrizProjecao.dot(p8v)
        p9p = matrizProjecao.dot(p9v)
        p10p = matrizProjecao.dot(p10v)
        p11p = matrizProjecao.dot(p11v)
        p12p = matrizProjecao.dot(p12v)
        p13p = matrizProjecao.dot(p13v)
        p14p = matrizProjecao.dot(p14v)
        p15p = matrizProjecao.dot(p15v)
        p16p = matrizProjecao.dot(p16v)
        p17p = matrizProjecao.dot(p17v)
        p18p = matrizProjecao.dot(p18v)
        p19p = matrizProjecao.dot(p19v)
        p20p = matrizProjecao.dot(p20v)
        p21p = matrizProjecao.dot(p21v)
        p22p = matrizProjecao.dot(p22v)
        p23p = matrizProjecao.dot(p23v)
        p24p = matrizProjecao.dot(p24v)
        p25p = matrizProjecao.dot(p25v)
        p26p = matrizProjecao.dot(p26v)
        p27p = matrizProjecao.dot(p27v)
        p28p = matrizProjecao.dot(p28v)
        p29p = matrizProjecao.dot(p29v)
        p30p = matrizProjecao.dot(p30v)
        p31p = matrizProjecao.dot(p31v)
        p32p = matrizProjecao.dot(p32v)
        p33p = matrizProjecao.dot(p33v)

        print("\nCoordenadas de projeção")
        mostraPontos(p1p, p2p ,p3p ,p4p ,p5p ,p6p ,p7p ,p8p, p9p, p10p, p11p, p12p, p13p, p14p, p15p, 
                p16p, p17p, p18p, p19p, p20p, p21p, p22p, p23p, p24p, p25p, p26p, p27p, p28p,
                p29p, p30p, p31p, p32p, p33p)

        p1p = p1p/p1p[3]
        p2p = p2p/p2p[3]
        p3p = p3p/p3p[3]
        p4p = p4p/p4p[3]
        p5p = p5p/p5p[3]
        p6p = p6p/p6p[3]
        p7p = p7p/p7p[3]
        p8p = p8p/p8p[3]
        p9p = p9p/p9p[3]
        p10p = p10p/p10p[3]
        p11p = p11p/p11p[3]
        p12p = p12p/p12p[3]
        p13p = p13p/p13p[3]
        p14p = p14p/p14p[3]
        p15p = p15p/p15p[3]
        p16p = p16p/p16p[3]
        p17p = p17p/p17p[3]
        p18p = p18p/p18p[3]
        p19p = p19p/p19p[3]
        p20p = p20p/p20p[3]
        p21p = p21p/p21p[3]
        p22p = p22p/p22p[3]
        p23p = p23p/p23p[3]
        p24p = p24p/p24p[3]
        p25p = p25p/p25p[3]
        p26p = p26p/p26p[3]
        p27p = p27p/p27p[3]
        p28p = p28p/p28p[3]
        p29p = p29p/p29p[3]
        p30p = p30p/p30p[3]
        p31p = p31p/p31p[3]
        p32p = p32p/p32p[3]
        p33p = p33p/p33p[3]

        mapeamento(p1p)
        mapeamento(p2p)
        mapeamento(p3p)
        mapeamento(p4p)
        mapeamento(p5p)
        mapeamento(p6p)
        mapeamento(p7p)
        mapeamento(p8p)
        mapeamento(p9p)
        mapeamento(p10p)
        mapeamento(p11p)
        mapeamento(p12p)
        mapeamento(p13p)
        mapeamento(p14p)
        mapeamento(p15p)
        mapeamento(p16p)
        mapeamento(p17p)
        mapeamento(p18p)
        mapeamento(p19p)
        mapeamento(p20p)
        mapeamento(p21p)
        mapeamento(p22p)
        mapeamento(p23p)
        mapeamento(p24p)
        mapeamento(p25p)
        mapeamento(p26p)
        mapeamento(p27p)
        mapeamento(p28p)
        mapeamento(p29p)
        mapeamento(p30p)
        mapeamento(p31p)
        mapeamento(p32p)
        mapeamento(p33p)

        plt.show()



    elif op == 9:
        break
    else:
        print("Opção inválida")

