import montando_matriz
import transformacao
import plotando_grafico

def menu():

    Matriz_A = None
    Matriz_B = None

    while True:

        print('\n\t\t-------- Transformações de Matrizes --------')
        print('\t\t1 - Montar Matriz')
        print('\t\t2 - Aplicar Transformação')
        print('\t\t3 - Plotar Gráfico')
        print('\t\t4 - Sair')
        opcao = input('\t\tSelecione uma opção: ')

        if opcao == '1':
            Matriz_A = montando_matriz.criar_matriz()
        elif opcao == '2':
            if Matriz_A is not None:
                Matriz_B = transformacao.menu_transformacao(Matriz_A)
            else:
                print('\n\t\tNenhuma matriz foi adicionada')
        elif opcao == '3':
            if  Matriz_A is not None:
                plotando_grafico.imprimindo_matriz(Matriz_A)
                if Matriz_B is not None:
                    plotando_grafico.imprimindo_matrizes(Matriz_A, Matriz_B)
                else:
                    print('\n\t\tMatriz de Transformação não detectada, tente aplicar uma transformação na Matriz')
            else:
                print('\n\t\tNenhuma matriz foi adicionada')

        elif opcao == '4':
            print('\n\t\tCódigo encerrado')
            break
        else:
            print('\n\t\tOpção Inválida')

if __name__ == '__main__':
    menu()


