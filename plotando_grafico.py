import numpy as np
import matplotlib.pyplot as plt

def criacao_plano_cartesiano():
    #criacao do  plano cartesiano no matplotlib
    ax = plt.axes()

    plt.grid(True, linestyle='--', alpha=0.7)
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.set_aspect('equal')

    plt.xlim([-25,25]) #limites do plano cartesiano em x
    plt.ylim([-25,25]) #limites do plano cartesiano em y

def plotando_matriz(matriz, ls='--', lw=1.2, color='blue'):
  #colocando a matriz no gráfico
  pontos_x, pontos_y = matriz
  size = len(pontos_x)

  for i in range(size): #definindo os pontos da matriz no mat
    plt.plot(pontos_x[i], pontos_y[i], marker='o')
    plt.plot([pontos_x[i], pontos_x[(i+1) % size]], [pontos_y[i], pontos_y[(i+1) % size]], linestyle=ls, linewidth=lw, color=color)

def imprimindo_matriz(matriz_A):
   
   criacao_plano_cartesiano()
   plotando_matriz(matriz_A, color='red')
   plt.show()

def imprimindo_matrizes(matriz_A, matriz_B):
   
   criacao_plano_cartesiano()
   plotando_matriz(matriz_A, color='red')
   plotando_matriz(matriz_B, color='blue')
   plt.show()
