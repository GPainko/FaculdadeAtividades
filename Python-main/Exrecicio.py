import sys

class Arquivo:
    def __init__(self,nome):
        self.nomearquivo = nome
        try:
            self.lista_glicemia = []
            with open(nome,"r") as self.arquivoglicemia:
                print("Arquivo localizado! ")
                for linha in self.arquivoglicemia:
                    lista_linha = linha.split("@")
                    self.lista_glicemia.append(float(lista_linha[0]))
            self.lista_glicemia_ordenada = self.lista_glicemia[:]
            self.lista_glicemia_ordenada.sort()
            soma = 0
            for i in self.lista_glicemia:
                soma = soma + i

            self.media = soma / len(self.lista_glicemia)        
        
        except:
            print("Alguma exceção foi gerada na execução do programa....")
        

while True:

    print("1. Carregar arquivo")
    print("2. listar dados glicêmicos")
    print("3. Calcular e mostrar medidas centrais")
    print("4. Sair Opção:")  

    op = int(input("Digite a opção: "))
    if op == 1:
        nome = input("nome do arquivo: ")
        carregar  = Arquivo(nome)
        carregar.arquivoglicemia
    elif op == 2:
        for i in carregar.lista_glicemia:
            print(i)   
    elif op == 3:
        print(f"O menor valor da Glicemia {carregar.lista_glicemia_ordenada[0]}")
    
        print(f"O maior valor da glicemia foi {carregar.lista_glicemia_ordenada[-1]}")

        print(f"A média da Glicemia foi {round(carregar.media,2)}")        
    elif op == 4:
        sys.exit() 
    else:
        print("Opção inválida")

    