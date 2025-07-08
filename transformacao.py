import numpy as np
import matplotlib.pyplot as plt

def matriz_translacao(tx,ty):
    return np.array([[1,0,tx], [0,1,ty], [0,0,1]])

def matriz_cisalhamento(wx, wy):
    return np.array([[1,wx,0],[wy,1,0],[0,0,1]])

def matriz_reflexao(escolha):

    if escolha.lower() == 'x':
        return np.array([[1,0,0],[0,-1,0],[0,0,1]])
    elif escolha.lower() =='y':
        return np.array([[-1,0,0], [0,1,0], [0,0,1]])
    elif escolha.lower() == 'origem':
        return np.array([[-1,0,0],[0,-1,0],[0,0,1]])
    else:
        print('\n\t\tOpção Inválida')
        return
    
def aplicar_transformacao(matriz_A, matriz_B):

    x = matriz_A[0]  
    y = matriz_A[1]  
    numero_pontos = len(x)
    
    pontos_homogeneos = [x,y,[1] * numero_pontos]
    
    Nova_Matriz = [[0] * numero_pontos, [0] * numero_pontos,  [0] * numero_pontos]
    
    for i in range(3): 
        for j in range(numero_pontos):  
            soma = 0
            for k in range(3): 
                soma += matriz_B[i][k] * pontos_homogeneos[k][j]
            Nova_Matriz[i][j] = soma
    
    print(Nova_Matriz[0], Nova_Matriz[1])

    #apenas x e y 
    return [Nova_Matriz[0], Nova_Matriz[1]]    
    
def menu_transformacao(Matriz):
    while True:
        print('\n\t\t------ Transformações de Matrizes ------')
        print('\t\t1 - Translacao')
        print('\t\t2 - Cisalhamento')
        print('\t\t3 - Reflexão')
        print('\t\t4 - Voltar ao Menu Principal')
        opcao = input('\t\tEscolha uma opção: ')

        if opcao == '1':
            try:
                x = float(input('\n\t\tInsira o valor de translação em x: '))
                y = float(input('\n\t\tInsira o valor de translação de y: '))

                matriz_transfomacao = matriz_translacao(x,y)
                return aplicar_transformacao(Matriz, matriz_transfomacao)
            except ValueError:
                print('\n\t\tValores x e y inválidos')
        elif opcao == '2':
            try:
                wx = float(input('\n\t\tInsira o p/ cisalhamento em x: '))
                wy = float(input('\n\t\tInsira o p/ de cisalhamento de y: '))

                matriz_transfomacao = matriz_cisalhamento(wx,wy)
                return aplicar_transformacao(Matriz, matriz_transfomacao)     
            except ValueError:
                print('\n\t\tValores de x ou y inválidos')      
        elif opcao == '3':
            eixo = input('\n\t\tInsira o eixo para rotacao (x|y|origem): ')

            if eixo.lower() in ['x', 'y', 'origem']:
                matriz_transfomacao = matriz_reflexao(eixo)
                return aplicar_transformacao(Matriz, matriz_transfomacao)
            else:
                print('\n\t\tValor inválido')
        elif opcao == '4':
            print('\n\t\tRetornando ao menu principal...')
            return     
        else:
            print('\n\t\tOpção Inválida')