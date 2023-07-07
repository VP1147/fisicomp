### UNIVERSIDADE FEDERAL DE MATO GROSSO DO SUL
### INSTITUTO DE FÍSICA
### FÍSICA COMPUTACIONAL E INFORMÁTICA

### PROJETO FINAL DE DISCIPLINA: Simulacao de trajetorias balisticas
### Aluno: Vinicius Arruda Pavao - Engenharia Fisica (INFI)

## Apresentação
# O código simula o lançamento balístico de um projétil em uma superfície
# plana dada uma velocidade inicial (v0), ângulo de lançamento (theta)
# e aceleração gravitacional (g).
# É pedido também o intervalo de integração (dt), tal que o cálculo é mais 
# preciso (e mais demorado) à medida que este se aproxima do 0.
# O código utiliza um método simples de integração (Método de Euler) para
# obter as velocidades e posições instantâneas do projétil.
# O retorno do código são dois gráficos distintos desenhados pela biblioteca 
# MatPlotLib, com o eixo X representando a distância horizontal e o eixo Y 
# representando a altura (azul) e a velocidade vertical (laranja). É também 
# mostrado no terminal a altura máxima atingida, isto é, quando a velocidade
# vertical foi igual a zero. 
# A rotina de testes consistiu em comparar as trajetórias dadas com resultados
# analíticos.

import math
import matplotlib.pyplot as plt

def projectile_motion(v0, theta, g, dt):
    theta = math.radians(theta)

    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)

    X = [0]
    Y = [0]
    Xv = [0]
    Vy = [0]

    x = 0
    y = 0
    t = 0

    # Calcula as velocidades e posições
    # para cada intervalo de coordenadas.
    while y >= 0:
        # Variação do tempo
        t += dt
        # Nova velocidade em y (considerando g)
        vy_n = vy - g * dt
        # Nova posicao em x
        x += vx * dt
        # Nova posicao em y
        y += vy_n * dt

        if -dt < vy_n < dt: print("h = {:.2f} m".format(y))

        X.append(x)
        Y.append(y)
        Vy.append(vy_n)
        vy = vy_n
    return X, Y, Vy

def plot_projectile_motion(X, Y, Vy):
    plt.plot(X, Y)
    plt.plot(X, Vy)
    plt.xlabel("Distancia (m)")
    plt.ylabel("Altura (m)")
    plt.title("Simulador balístico")
    plt.show()

# Exemplo

v0 = 50             # Velocidade inicial            (m/s)
theta = 45          # Ângulo de lançamento          (graus)
g = 9.81            # Aceleração gravitacional      (m/s^2)
dt = 0.001

X, Y, Vy = projectile_motion(v0, theta, g, dt)
plot_projectile_motion(X, Y, Vy)