#Guilherme e Pedro Cassenote

# Luzes

# Neste exemplo, especificamos uma uma iluminação ambiente, difusa e especular básicas.
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import pyrr
from TextureLoader import load_texture
from ObjLoader import ObjLoader

Window = None
Shader_programm = None
Vao_cubo = None
Vao_piramide = None
tam_piramide = 0
WIDTH = 800
HEIGHT = 600

Vao_Objetogato = None
obj_indicesgato = None
obj_buffergato = None
obj_texturagato = None

Vao_Objetosofa = None
obj_indicessofa = None
obj_buffersofa = None
obj_texturasofa = None

Tempo_entre_frames = 0 #variavel utilizada para movimentar a camera

#Variáveis referentes a câmera virtual e sua projeção
Cam_speed = 10.0 #velocidade da camera, 1 unidade por segundo
Cam_yaw_speed = 80.0 #velocidade de rotação da câmera em y, 10 graus por segundo
Cam_pos = np.array([0.0, 0.0, 15.0]) #posicao inicial da câmera
Cam_yaw = 0.0 #ângulo de rotação da câmera em y

#Variáveis referentes a luz 1
luz_posicao = np.array([0.0, 0.0, 0.0])
La = np.array([0.2, 0.2, 0.2]) #Luz ambiente
Ld = np.array([0.7, 0.7, 0.7]) #cinza bem claro
Ls = np.array([1.0, 1.0, 1.0]) #luz branca

luz_speed = 10.0

luz_posicao1 = np.array([0.0, 0.0, 0.0])
La1 = np.array([0.2, 0.2, 0.2]) #Luz ambiente
Ld1 = np.array([0.3, 0.3, 0.7]) #cinza bem claro
Ls1 = np.array([1.0, 1.0, 1.0]) #luz branca

 #velocidade da luz qdo movimentada pelo teclado, 1 unidade por segundo

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Projeto Final", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de video: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versao do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))
    print("MENU DE COMANDOS: ")
    print("wsda anda")
    print("<- vira camera para esquerda")
    print("-> vira camera para direita")
    print("ctrl abaixa camera ")
    print("espaço cima camera ")
    print("e abrir porta ")
    print("r reseta camera ")
    print("num 4568 movimenta luz ")
    print("num 79 aproxima e afasta luz ")

def inicializaCubo():

    global Vao_cubo
    # Vao do cubo
    Vao_cubo = glGenVertexArrays(1)
    glBindVertexArray(Vao_cubo)

    # VBO dos vértices do cubo
    points = [
		#face frontal
		0.5, 0.5, 0.5,#0
		0.5, -0.5, 0.5,#1
		-0.5, -0.5, 0.5,#2
		-0.5, 0.5, 0.5,#3
		0.5, 0.5, 0.5,
		-0.5, -0.5, 0.5,
		#face trazeira
		0.5, 0.5, -0.5,#4
		0.5, -0.5, -0.5,#5
		-0.5, -0.5, -0.5,#6
		-0.5, 0.5, -0.5,#7
		0.5, 0.5, -0.5,
		-0.5, -0.5, -0.5,
		#face esquerda
		-0.5, -0.5, 0.5,
		-0.5, 0.5, 0.5,
		-0.5, -0.5, -0.5,
		-0.5, -0.5, -0.5,
		-0.5, 0.5, -0.5,
		-0.5, 0.5, 0.5,
		#face direita
		0.5, -0.5, 0.5,
		0.5, 0.5, 0.5,
		0.5, -0.5, -0.5,
		0.5, -0.5, -0.5,
		0.5, 0.5, -0.5,
		0.5, 0.5, 0.5,
		#face baixo
		-0.5, -0.5, 0.5,
		0.5, -0.5, 0.5,
		0.5, -0.5, -0.5,
		0.5, -0.5, -0.5,
		-0.5, -0.5, -0.5,
		-0.5, -0.5, 0.5,
		#face cima
		-0.5, 0.5, 0.5,
		0.5, 0.5, 0.5,
		0.5, 0.5, -0.5,
		0.5, 0.5, -0.5,
		-0.5, 0.5, -0.5,
		-0.5, 0.5, 0.5,
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    # VBO das normais
    normais = [
		#face frontal
		0.0, 0.0, 1.0,#apontado para frente
		0.0, 0.0, 1.0,#apontado para frente
		0.0, 0.0, 1.0,#apontado para frente
		0.0, 0.0, 1.0,#apontado para frente
		0.0, 0.0, 1.0,#apontado para frente
		0.0, 0.0, 1.0,#apontado para frente
		#face trazeira
		0.0, 0.0, -1.0,#apontado para trás
		0.0, 0.0, -1.0,#apontado para trás
		0.0, 0.0, -1.0,#apontado para trás
		0.0, 0.0, -1.0,#apontado para trás
		0.0, 0.0, -1.0,#apontado para trás
		0.0, 0.0, -1.0,#apontado para trás
		#face esquerda
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente
		-1.0, 0.0, 0.0,#apontado para esquerda e para frente          
		#face direita
		1.0, 0.0, 0.0,#apontado para direita e para frente
		1.0, 0.0, 0.0,#apontado para direita e para frente
		1.0, 0.0, 0.0,#apontado para direita e para frente
		1.0, 0.0, 0.0,#apontado para direita e para frente
		1.0, 0.0, 0.0,#apontado para direita e para frente
		1.0, 0.0, 0.0,#apontado para direita e para frente
		#face inferior
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		0.0, -1.0, 0.0,#apontado para baixo e para frente
		#face superior
		0.0, 1.0, 0.0,#apontado para cima e para frente
		0.0, 1.0, 0.0,#apontado para cima e para frente
		0.0, 1.0, 0.0,#apontado para cima e para frente
		0.0, 1.0, 0.0,#apontado para cima e para frente
		0.0, 1.0, 0.0,#apontado para cima e para frente
		0.0, 1.0, 0.0,#apontado para cima e para frente
	]
    normais = np.array(normais, dtype=np.float32)
    nvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, nvbo)
    glBufferData(GL_ARRAY_BUFFER, normais, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaObjetogato():
    global Vao_Objetogato, obj_buffergato, obj_indicesgato, obj_texturagato
    obj_indicesgato, obj_buffergato = ObjLoader.load_model("modelagem/gato.obj")

    #Vao do objeto
    Vao_Objetogato = glGenVertexArrays(1)
    glBindVertexArray(Vao_Objetogato)

    #VBO do objeto. Ao invés de termos 1 VBO para cada informação (vértices, texturas, normais, etc.), este exemplo utiliza
    #1 único VBO com todas as informações dentro
    bvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, bvbo)
    glBufferData(GL_ARRAY_BUFFER, obj_buffergato.nbytes, obj_buffergato, GL_STATIC_DRAW)
    # vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj_buffergato.itemsize * 8, ctypes.c_void_p(0))
    # texturas
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj_buffergato.itemsize * 8, ctypes.c_void_p(12))
    # normais
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj_buffergato.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    #carrega os arquivos de textura
    obj_texturagato = glGenTextures(1)
    load_texture("gato.jpg", obj_texturagato)

def inicializaObjetosofa():
    global Vao_Objetosofa, obj_buffersofa, obj_indicessofa, obj_texturasofa
    obj_indicessofa, obj_buffersofa = ObjLoader.load_model("modelagem/mesa.obj")

    #Vao do objeto
    Vao_Objetosofa = glGenVertexArrays(1)
    glBindVertexArray(Vao_Objetosofa)

    #VBO do objeto. Ao invés de termos 1 VBO para cada informação (vértices, texturas, normais, etc.), este exemplo utiliza
    #1 único VBO com todas as informações dentro
    bvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, bvbo)
    glBufferData(GL_ARRAY_BUFFER, obj_buffersofa.nbytes, obj_buffersofa, GL_STATIC_DRAW)
    # vertices
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, obj_buffersofa.itemsize * 8, ctypes.c_void_p(0))
    # texturas
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, obj_buffersofa.itemsize * 8, ctypes.c_void_p(12))
    # normais
    glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, obj_buffersofa.itemsize * 8, ctypes.c_void_p(20))
    glEnableVertexAttribArray(2)

    obj_texturasofa = glGenTextures(1)
    load_texture("gato.jpg", obj_texturasofa)

def inicializaShaders():
    global Shader_programm
    # Especificação do Vertex Shader:
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao; //vértices do objeto vindas do modelo do objeto (PYTHON)
        layout(location = 1) in vec3 vertex_normal; //normais do objeto vindas do modelo do objeto (PYTHON)
        out vec3 vertex_posicao_cam, vertex_normal_cam;
        out vec2 v_texture; //saida da textura para o fragment shader
        uniform mat4 transform, view, proj;
        void main () {
           vertex_posicao_cam = vec3 (view * transform * vec4 (vertex_posicao, 1.0)); //posição do objeto em relação a CÂMERA
            vertex_normal_cam = vec3 (view *  transform * vec4 (vertex_normal, 0.0)); //normais do objeto em relação a CÂMERA
       
            gl_Position = proj * view * transform * vec4 (vertex_posicao, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

    # Especificação do Fragment Shader:
    fragment_shader = """
        #version 400
		in vec3 vertex_posicao_cam, vertex_normal_cam; //variáveis vindas do VERTEX SHADER
        in vec2 v_texture; //variável de textura vinda do VERTEX SHADER
        uniform sampler2D s_texture;
        
        //propriedades de uma luz pontual vindas do PYTHON
        uniform vec3 luz_posicao;
        uniform vec3 Ls;// luz especular
		uniform vec3 Ld;// luz difusa
		uniform vec3 La;// luz ambiente

        uniform vec3 luz_posicao1;
        uniform vec3 Ls1;// luz especular
		uniform vec3 Ld1;// luz difusa
		uniform vec3 La1;// luz ambiente

        //propriedades de reflexão da superficie do objeto vindas do PYTHON
		uniform vec3 Ks;//reflexão especular
		uniform vec3 Kd;//reflexão difusa
		uniform vec3 Ka;//reflexão ambiente
        uniform float especular_exp;//expoente especular
        
        uniform mat4 view; //matriz da câmera vinda do PYTHON
		out vec4 frag_colour;

        //variáveis globais que são utilizadas tanto na intensidade difusa quanto especular, para não precisar recalcular duas vezes
        vec3 luz_posicao_cam, luz_vetor_cam, luz_vetor_cam_normalizada, vertex_normal_cam_normalizada;
        vec3 luz_posicao_cam1, luz_vetor_cam1, luz_vetor_cam_normalizada1;

        vec3 intensidadeAmbiente(){
            /*
            Cálculo de Intensidade de Luz Ambiente (Ia)
            O cálculo da intensidade de luz ambiente é o mais simples:
            basta multiplicar a cor da luz ambiente pela refletância de luz ambiente da superfície
            */
            vec3 Ia = La * Ka;
            return Ia;
        }

        vec3 intensidadeAmbiente1(){
            vec3 Ia = La1 * Ka;
            return Ia;
        }

        vec3 intensidadeDifusa(){
            /*
            Cálculo de Intensidade de Luz Difusa (Id)
            Para calcularmos a intensidade de luz difusa, precisamos, primeiramente, 
            calcular a posição da luz em relação a câmera (luz_posicao_cam)
            */
            luz_posicao_cam = vec3 (view * vec4 (luz_posicao, 1.0));//posicao da luz em relação a câmera

            /*A posição da luz (luz_posicao_cam) calculada acima representa um vetor que sai da origem (0,0,0) e
		aponta para a luz. Para a luz difusa, precisamos calcular um vetor que saia de cada vértice do objeto
		(vertex_posicao_cam) e aponte para essa luz. Para isso, basta calcularmos a diferença entre luz_posicao_cam
		e vertex_posicao_cam.*/
            luz_vetor_cam = luz_posicao_cam - vertex_posicao_cam;//vetor apontando para a luz em relação a posicao do vértice 

            /*Por fim, normalizamos o vetor da luz em relação ao vértice do objeto e calculamos o cosseno do angulo
		entre o mesmo e a normal da superficie utilizando o produto escalar*/
            luz_vetor_cam_normalizada = normalize(luz_vetor_cam);//vetor da luz normalizada
            vertex_normal_cam_normalizada = normalize(vertex_normal_cam);
            float cosseno_difusa = dot(vertex_normal_cam_normalizada,luz_vetor_cam_normalizada);//cosseno do angulo entre o vetor da luz e a normal da superficie
            
            vec3 Id = Ld * Kd * cosseno_difusa;

            return Id;

        }

        vec3 intensidadeDifusa1(){
            luz_posicao_cam1 = vec3 (view * vec4 (luz_posicao1, 1.0));//posicao da luz em relação a câmera
            luz_vetor_cam1 = luz_posicao_cam1 - vertex_posicao_cam;//vetor apontando para a luz em relação a posicao do vértice 
            luz_vetor_cam_normalizada1 = normalize(luz_vetor_cam1);//vetor da luz normalizada
            vertex_normal_cam_normalizada = normalize(vertex_normal_cam);
            float cosseno_difusa = dot(vertex_normal_cam_normalizada,luz_vetor_cam_normalizada1);//cosseno do angulo entre o vetor da luz e a normal da superficie
            
            vec3 Id = Ld1 * Kd * cosseno_difusa;
            return Id;

        }

        vec3 intensidadeEspecular(){
            /*
            Cálculo de Intensidade de Luz Especular (Is)
            Para o cálculo da intensidade de luz especular, precisamos primeiramente calcular o vetor que representa 
            a luz refletida em relação a normal da superfície */
            vec3 luz_reflexao_vetor_cam = reflect(-luz_vetor_cam_normalizada, vertex_normal_cam_normalizada);
            /*Como a intensidade de luz especular depende da posição da câmera, definimos um vetor que sai da superficie
		    do objeto e aponta para a camera, e então normalizamos, pois utilizaremos ele no cálculo do produto escalar*/
            vec3 superficie_camera_vetor = normalize(-vertex_posicao_cam);
            /*E então calculamos o ângulo entre o vetor de reflexão da luz e o vetor em relação a posicao do observador*/
            float cosseno_especular = dot(luz_reflexao_vetor_cam, superficie_camera_vetor);
            cosseno_especular = max(cosseno_especular, 0.0);//se o cosseno der negativo, atribui 0 para ele
            /*Na intensidade especular, precisamos elevar o cosseno calculado acima ao expoente especular*/
            float fator_especular = pow (cosseno_especular, especular_exp);
            /*E, por fim, calculamos a intensidade de luz especular refletida (Is) */

            vec3 Is = Ls * Ks * fator_especular;

            return Is;
        }

        vec3 intensidadeEspecular1(){
            vec3 luz_reflexao_vetor_cam = reflect(-luz_vetor_cam_normalizada1, vertex_normal_cam_normalizada);
            vec3 superficie_camera_vetor = normalize(-vertex_posicao_cam);
            float cosseno_especular = dot(luz_reflexao_vetor_cam, superficie_camera_vetor);
            cosseno_especular = max(cosseno_especular, 0.0);//se o cosseno der negativo, atribui 0 para ele
            float fator_especular = pow (cosseno_especular, especular_exp);

            vec3 Is = Ls1 * Ks * fator_especular;

            return Is;
        }
		void main () {

            vec3 Ia = intensidadeAmbiente();
            vec3 Ia1 = intensidadeAmbiente();

            vec3 Id = intensidadeDifusa();
            vec3 Id1 = intensidadeAmbiente();

            vec3 Is = intensidadeEspecular();
            vec3 Is1 = intensidadeAmbiente();

            /*A cor final do fragmento é a soma das 3 componentes de iluminação*/
		    vec4 corReflexao = vec4(Ia1+Ia+Id1+Id+Is1+Is, 1.0);
            vec4 corTextura = texture(s_texture, v_texture);

            /*A cor final do fragmento é a soma das 3 componentes de iluminação + cor da textura*/
            frag_colour = corReflexao + corTextura;
		}
    """
    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def transformacaoGenerica(Tx, Ty, Tz, Sx, Sy, Sz, Rx, Ry, Rz):
    #matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, Tx], 
        [0.0, 1.0, 0.0, Ty], 
        [0.0, 0.0, 1.0, Tz], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de rotação em torno do eixo X
    angulo = np.radians(Rx)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoX = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos, -sen, 0.0],
        [0.0, sen, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Y
    angulo = np.radians(Ry)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoY = np.array([
        [cos, 0.0, sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Z
    angulo = np.radians(Rz)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoZ = np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #combinação das 3 rotação
    rotacao = rotacaoZ.dot(rotacaoY.dot(rotacaoX))

    #matriz de escala
    escala = np.array([
        [Sx, 0.0, 0.0, 0.0], 
        [0.0, Sy, 0.0, 0.0], 
        [0.0, 0.0, Sz, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    transformacaoFinal = translacao.dot(rotacao.dot(escala))
    
    #E passamos a matriz para o Vertex Shader.
    transformLoc = glGetUniformLocation(Shader_programm, "transform")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacaoFinal)

def especificaMatrizVisualizacao():

    # Especificação da matriz de visualização, que é definida com valores de translação e
	# rotação inversos da "posição" da câmera, pois é o mundo que se movimenta ao redor da
	# câmera, e não a câmera que se movimenta ao redor do mundo.
    visualizacao = np.identity(4)

    #posicao da camera
    translacaoCamera = np.array([
        [1.0, 0.0, 0.0, -Cam_pos[0]], 
        [0.0, 1.0, 0.0, -Cam_pos[1]], 
        [0.0, 0.0, 1.0, -Cam_pos[2]], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)
    
    #orientacao da camera (rotação em y)
    angulo = np.radians(-Cam_yaw)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoCamera = np.array([
        [cos, 0.0, sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    visualizacao = rotacaoCamera.dot(translacaoCamera)

    transformLoc = glGetUniformLocation(Shader_programm, "view")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, visualizacao)

def especificaMatrizProjecao():
    #Especificação da matriz de projeção perspectiva.
    znear = 0.1 #recorte z-near
    zfar = 100.0 #recorte z-far
    fov = np.radians(67.0) #campo de visão
    aspecto = WIDTH/HEIGHT #aspecto

    a = 1/(np.tan(fov/2)*aspecto)
    b = 1/(np.tan(fov/2))
    c = (zfar + znear) / (znear - zfar)
    d = (2*znear*zfar) / (znear - zfar)
    projecao = np.array([
        [a,   0.0, 0.0,  0.0],
        [0.0, b,   0.0,  0.0],
        [0.0, 0.0, c,    d],
        [0.0, 0.0, -1.0, 1.0]
    ])

    transformLoc = glGetUniformLocation(Shader_programm, "proj")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, projecao)

def inicializaCamera():
    especificaMatrizVisualizacao()
    especificaMatrizProjecao()

def trataTeclado():
    global Cam_pos, Cam_yaw, Cam_yaw_speed, Tempo_entre_frames, luz_posicao
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)): #fecha a aplicação
            glfw.set_window_should_close(Window, True)

    #o botão R reseta a cena (posição e ângulo da câmera; e a luz)
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_R)):
        luz_posicao = np.array([0.0, 0.0, 0.0])
        Cam_pos = np.array([0.0, 0.0, 15.0])
        Cam_yaw = 0.0 #ângulo de rotação da câmera em y

    #movimentos da câmera
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_A)):
        Cam_pos[0] -= Cam_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_D)):
        Cam_pos[0] += Cam_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_W)):
        Cam_pos[2] -= Cam_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_S)):
        Cam_pos[2] += Cam_speed * Tempo_entre_frames

    #muda a altura da câmera
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_SPACE)):
        Cam_pos[1] += Cam_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_LEFT_CONTROL)):
        Cam_pos[1] -= Cam_speed * Tempo_entre_frames

    #gira a câmera na horizontal
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_LEFT)):
        Cam_yaw += Cam_yaw_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_RIGHT)):
        Cam_yaw -= Cam_yaw_speed * Tempo_entre_frames
    
    #parâmetros da posição da luz
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_4)):
        luz_posicao[0] -= luz_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_6)):
        luz_posicao[0] += luz_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_5)):
        luz_posicao[1] -= luz_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_8)):
        luz_posicao[1] += luz_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_7)):
        luz_posicao[2] -= luz_speed * Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_KP_9)):
        luz_posicao[2] += luz_speed * Tempo_entre_frames

def especificaMaterial(KaR, KaG, KaB, KdR, KdG, KdB, KsR, KsG, KsB, n):
    global Shader_programm
    #Coeficiente de reflexão ambiente
    Ka = np.array([KaR, KaG, KaB])#reflete luz ambiente
    Ka_loc = glGetUniformLocation(Shader_programm, "Ka")
    glUniform3fv(Ka_loc, 1, Ka)

    #Coeficiente de reflexão difusa
    Kd = np.array([KdR, KdG, KdB])#reflete luz difusa
    Kd_loc = glGetUniformLocation(Shader_programm, "Kd")
    glUniform3fv(Kd_loc, 1, Kd)

    #Coeficiente de reflexão especular
    Ks = np.array([KsR, KsG, KsB])#reflete luz especular
    Ks_loc = glGetUniformLocation(Shader_programm, "Ks")
    glUniform3fv(Ks_loc, 1, Ks)

    #expoente expecular
    especular_exp = n
    especular_exp_loc = glGetUniformLocation(Shader_programm, "especular_exp")
    glUniform1f(especular_exp_loc, especular_exp)



def especificaMaterialCubo(KaR, KaG, KaB, KdR, KdG, KdB, KsR, KsG, KsB, n):
    global Shader_programm
    #Coeficiente de reflexão ambiente
    Ka = np.array([KaR, KaG, KaB])#reflete luz ambiente
    Ka_loc = glGetUniformLocation(Shader_programm, "Ka")
    glUniform3fv(Ka_loc, 1, Ka)

    #Coeficiente de reflexão difusa
    Kd = np.array([KdR, KdG, KdB])#reflete luz difusa
    Kd_loc = glGetUniformLocation(Shader_programm, "Kd")
    glUniform3fv(Kd_loc, 1, Kd)

    #Coeficiente de reflexão especular
    Ks = np.array([KsR, KsG, KsB])#reflete luz especular
    Ks_loc = glGetUniformLocation(Shader_programm, "Ks")
    glUniform3fv(Ks_loc, 1, Ks)

    #expoente expecular
    especular_exp = n
    especular_exp_loc = glGetUniformLocation(Shader_programm, "especular_exp")
    glUniform1f(especular_exp_loc, especular_exp)

def especificaLuz():
    global Shader_programm, luz_posicao, La, Ld, Ls
    #posição da luz
    luz_posicaoloc = glGetUniformLocation(Shader_programm, "luz_posicao")#envia o array da posição da luz para o shader
    glUniform3fv(luz_posicaoloc, 1, luz_posicao)

    #Fonte de luz ambiente
    La_loc = glGetUniformLocation(Shader_programm, "La")#envia o array da Luz Ambiente para o shader
    glUniform3fv(La_loc, 1, La)

    #Fonte de luz difusa
    Ld_loc = glGetUniformLocation(Shader_programm, "Ld")#envia o array da Luz Difusa para o shader
    glUniform3fv(Ld_loc, 1, Ld)
    
    #Fonte de luz especular
    Ls_loc = glGetUniformLocation(Shader_programm, "Ls")#envia o array da Luz Especular para o shader
    glUniform3fv(Ls_loc, 1, Ls)

def especificaLuz1():
    global Shader_programm, luz_posicao1, La1, Ld1, Ls1
    #posição da luz
    luz_posicaoloc = glGetUniformLocation(Shader_programm, "luz_posicao1")#envia o array da posição da luz para o shader
    glUniform3fv(luz_posicaoloc, 1, luz_posicao1)

    #Fonte de luz ambiente
    La_loc = glGetUniformLocation(Shader_programm, "La1")#envia o array da Luz Ambiente para o shader
    glUniform3fv(La_loc, 1, La1)

    #Fonte de luz difusa
    Ld_loc = glGetUniformLocation(Shader_programm, "Ld1")#envia o array da Luz Difusa para o shader
    glUniform3fv(Ld_loc, 1, Ld1)
    
    #Fonte de luz especular
    Ls_loc = glGetUniformLocation(Shader_programm, "Ls1")#envia o array da Luz Especular para o shader
    glUniform3fv(Ls_loc, 1, Ls1)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao, WIDTH, HEIGHT, Tempo_entre_frames

    tempo_anterior = glfw.get_time()

    #Ativação do teste de profundidade. Sem ele, o OpenGL não sabe que faces devem ficar na frente e que faces devem ficar atrás.
    glEnable(GL_DEPTH_TEST)
    while not glfw.window_should_close(Window):
        #calcula quantos segundos se passaram entre um frame e outro
        tempo_frame_atual = glfw.get_time()
        Tempo_entre_frames = tempo_frame_atual - tempo_anterior
        tempo_anterior = tempo_frame_atual

        #limpa a tela e os buffers
        glClearColor(0.2, 0.3, 0.3, 1.0)        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #configura a viewport para pegar toda a janela
        glViewport(0, 0, WIDTH, HEIGHT)

        #ativa o shader
        glUseProgram(Shader_programm)

        especificaLuz() #parâmetros da fonte de luz
        especificaLuz1()

        inicializaCamera()#configuramos a câmera
        glBindVertexArray(Vao_cubo) #ativamos o objeto (cubo) que queremos renderizar

        #chão marrom
        especificaMaterialCubo(0.2, 0.2, 0.2, 135/255, 84/255, 56/255, 0.1, 0.1, 0.1, 32)
        transformacaoGenerica(0,-5,0,20,0.5,20,0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36) #renderiza o cubo

        #paredes de uma casa verde escura
        especificaMaterialCubo(0.2, 0.2, 0.2, 7/255, 112/255, 70/255, 0.3, 0.3, 0.3, 32)
        #parede esquerda da casa
        transformacaoGenerica(-5,-1.25,0,  0.5,7.5,10,  0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        #parede direita da casa
        transformacaoGenerica(5,-1.25,0,  0.5,7.5,10,  0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        #parede de trás da casa
        transformacaoGenerica(0,-1.25,-5,  10,7.5,0.5,  0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        #parede de cima da casa - teto
        transformacaoGenerica(0,2.25,0,  10,10,0.5,  90,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        #parede da frente esquerda da casa
        transformacaoGenerica(-3.75,-1.25,5,  3,7,0.5,  0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)
        #parede da frente direita da casa
        transformacaoGenerica(3.75,-1.25,5,  3,7,0.5,  0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)

        #porta da casa - marrom
        trans_x = 0 # base
        trans_z = 5 # base
        porta_rotacao = 0 # base

        #enquanto o botão E estiver apertado, a porta fica aberta
        if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_E)):
            trans_x = -1.625
            trans_z = 3.25
            porta_rotacao = 80

        especificaMaterialCubo(0.2, 0.2, 0.2, 135/255, 84/255, 56/255, 0.1, 0.1, 0.1, 32)
        transformacaoGenerica(trans_x,-1.25,trans_z,  4.5,7,0.5,  0,porta_rotacao,0)
        glDrawArrays(GL_TRIANGLES, 0, 36)

        glBindVertexArray(Vao_Objetogato) #ativamos o objeto que queremos renderizar
        glBindTexture(GL_TEXTURE_2D,obj_texturagato)
        especificaMaterial(0.2, 0.2, 0.2, 0.8, 0.8, 0.8, 0.1, 0.1, 0.1, 32)
        transformacaoGenerica(0,-4,0,0.2,0.2,0.2,0,0,0)
        glDrawArrays(GL_TRIANGLES, 0, len(obj_indicesgato))

        glBindVertexArray(Vao_Objetosofa) #ativamos o objeto que queremos renderizar
        glBindTexture(GL_TEXTURE_2D,obj_texturasofa)
        transformacaoGenerica(2,-4.8,1,1,1,1,0,90,0)
        glDrawArrays(GL_TRIANGLES, 0, len(obj_indicessofa))


        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        trataTeclado()
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaCubo()
    inicializaObjetogato()
    inicializaObjetosofa()
    inicializaShaders()
    inicializaRenderizacao()
    

if __name__ == "__main__":
    main()