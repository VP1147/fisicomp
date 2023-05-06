## -- Orbiter Simulation --
## Simula um satelite em orbita circular em torno
## de um planeta.
## Aluno: Vinicius Pavao - INFI/UFMS
## Maio de 2023

import graphics as gfx
from getch import getch
import math as m
import time
import platform

def init(size, speed, sf):
	print("Iniciando ...")
	uname = platform.uname()
	print(f"Sistema: {uname.system} {uname.node} {uname.release} {uname.version}\n")

	global Win; global x; global y;					# Variaveis graficas
	global G 										# Constantes fisicas
	G = 6.67*10**-11								# N.m²/Kg²
	global motion; global size_factor				# Variaveis de escala

	x, y = size, int(size*(3/4))					# Define o aspecto 3:4 da janela
	Win = gfx.GraphWin("Orbiter Simulation", x, y) 	# Inicia janela grafica
	motion = speed
	size_factor = sf
	Win.setBackground(gfx.color_rgb(0,10,20))		# Cor de fundo

	text = 		"Vel.: "+str(motion)+"x\n"				# Velocidade da animacao
	text += 	"Esc.: "+str(size_factor)+" Km/px"		# Escala | Km/pixel
	label = gfx.Text(gfx.Point(x/2, 20), text)
	label.setFill(gfx.color_rgb(255,255,255))
	label.draw(Win)

def planet(name, center, radius, mass):		# Nome | Raio (km) | massa (kg)
	p = gfx.Circle(gfx.Point(center[0], center[1]), radius / size_factor)
	p.setFill(gfx.color_rgb(200,200,200))
	p.draw(Win)
	label = gfx.Text(gfx.Point(center[0], center[1]), name)
	label.setFill(gfx.color_rgb(0,0,0))
	label.draw(Win)

def satellite(center, h, period, M):			# centro (x,y) | Altura em relacao 
												# ao CM (Km) | Periodo (s) | Massa (Kg)
	X = 0
	Y = 0
	height = h / size_factor					# Converte para a escala

	desloc = 2*m.pi*h							# Deslocamento (circunferencia) - Km

	R = 0
	V = (desloc / period)						# Vel - km/s
	Vh = (desloc / (period/3600))
	ag = (G*M)/((h*1000)**2)
	#V = m.sqrt((G*M)/h)

	dt = 1/60 								# Variacoes de tempo (dt) e posicao (dx, dy)
											# para cada frame (60 fps)
	dx = ( dt / period ) 
	dy = ( dt / period ) 
	#print(dx)
	if period/60 < 200: per = str(round(period/60, 2))+" min"		# Legenda
	elif period/60 >= 200: per = str(round(period/3600,2))+" h"

	info = 		"V = "+str(round(Vh, 2))+" km/h\n"
	info +=		"T = "
	info +=		per
	info +=		"\ng = "+str(round(ag, 2))+" m/s²"
	satinfo = gfx.Text(gfx.Point(x/2, y-30), info)
	satinfo.setFill(gfx.color_rgb(255,255,255))
	satinfo.draw(Win)
																# loop da orbita - segue 
																# durante o resto da
																# execucao
	while R <= desloc:
		sat = gfx.Circle(gfx.Point(m.cos(X)*height + center[0], m.sin(Y)*height + center[1]), 3)
		sat.setFill(gfx.color_rgb(255,255,255))
		sat.draw(Win)

		vt = gfx.Line(gfx.Point(m.cos(X)*height + center[0], m.sin(Y)*height + center[1]), gfx.Point(m.cos(X + 30*dx*motion)*height + center[0], m.sin(Y + 30*dy*motion)*height + center[1]))
		vt.setArrow("last") 
		vt.setFill(gfx.color_rgb(0,150,0))
		vt.draw(Win)

		fg = gfx.Line(gfx.Point(m.cos(X)*height + center[0], m.sin(Y)*height + center[1]), gfx.Point(m.cos(X + dx*motion)*height/(3/2) + center[0], m.sin(Y + dy*motion)*height/(3/2) + center[1]))
		fg.setArrow("last") 
		fg.setFill(gfx.color_rgb(0,0,150))
		fg.draw(Win)

		Win.update()											# Desenha frame
		X += (dx) * motion
		Y += (dy) * motion
		#print(X)
		#R += dx*h
		time.sleep(dt)											# Variacao do tempo
		sat.undraw()											# Apaga para o 
																# prox. frame
		vt.undraw()
		fg.undraw()

mv = 3600			# Fator de velocidade - Maior = mais rapido 
					# (1 = tempo real)
sf = 50				# Fator de tamanho - Maior = maior `zoom`

init(800, mv, sf)

# Dados do Planeta (Terra)
rt = 6378 				# km
Mt = 5.97*(10**24)  		# kg

c = [ x/2, y/2 ]		# Centro da janela: [ x/2, y/2 ]

# Cria o planeta (Terra) com as dimensoes acima
#planet("Terra", c, r, M)
planet("Marte", c, rt, Mt)

# Dados do satelite
#h = 35786					# Km - geostacionario
h = 408					# Km - ISS
#h = 384000                 # Km - Lua

a = (rt + h)*1000 		# m
T = 2*m.pi*m.sqrt( a**3 / (G*Mt))
print("T = {:d} seg".format(int(T)))
print(" = {:.2f} h".format(T/3600))
#T = 5

# Cria um satelite com as caracteristicas acima
# Note que r e M referem-se ao planeta orbitado
satellite(c, rt + h, T, Mt)

# Espera por uma entrada no console
win.promptClose(win.getWidth()/2, 30) # specify x, y coordinates of prompt