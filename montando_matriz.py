import numpy as np

def criar_matriz():
    
    while True:
        try:
            pontos = int(input("\n\t\tInsira a quantidade de pontos (>=3): "))
            if pontos >= 3:
                break
            print("\n\t\tA matriz precisa ter ao menos 3 pontos")
        except ValueError:
            print("\n\t\tDigite um número válido")
    
    matriz = []
    
    print("\n\t\tDigite as coordenadas dos pontos (x,y):")

    for i in range(pontos):
        while True:
            try:
                x = float(input(f"\n\t\tPonto ({i+1}) | X: "))
                y = float(input(f"\n\t\tPonto ({i+1}) | Y: "))
                matriz.append([x, y])
                break
            except ValueError:
                print("\n\t\tDigite um número válido")

    # p/ ficar no formato [[X1,X2,X3],[Y1,Y2,Y3]]
    return np.array(matriz).T