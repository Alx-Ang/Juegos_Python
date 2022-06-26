#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.mixer.init()


class Personaje(Sprite):
	def __init__(self):
		self.image = personaje = pygame.image.load("Imagenes/naruto.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(50, 300)
		self.muerto = 0
		pygame.mixer.music.play(loops=-1)
	def update(self):
		teclas = pygame.key.get_pressed()
		if teclas[K_SPACE]:
			self.image = personaje = pygame.image.load("Imagenes/naruto_ataque.png").convert_alpha()
			disparo1.play()
		elif kamehameha.rect.x > 860:
			self.image = personaje = pygame.image.load("Imagenes/naruto.png").convert_alpha()
		if teclas[K_LEFT]:
			self.image = personaje = pygame.image.load("Imagenes/naruto_izquierda.png").convert_alpha()
			if self.rect.x > 0:
				self.rect.x -= 10
		elif teclas[K_RIGHT]:
			self.image = personaje = pygame.image.load("Imagenes/naruto_derecha.png").convert_alpha()
			if self.rect.x < 740:
				self.rect.x += 10

		if teclas[K_UP]:
			self.image = personaje = pygame.image.load("Imagenes/naruto_arriba.png").convert_alpha()
			if self.rect.y > 32:
				self.rect.y -= 10
		elif teclas[K_DOWN]:
			if self.rect.y < 410:
				self.image = personaje = pygame.image.load("Imagenes/naruto_abajo.png").convert_alpha()
				self.rect.y += 10

class Kamehameha(Sprite):
	def __init__(self):
		self.image = kamehameha = pygame.image.load("Imagenes/ataque_n.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(900, 700)
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.rect.x > 840:
			if teclas[K_SPACE]:
				self.rect.x = (personaje.rect.x + 60)
				self.rect.y = (personaje.rect.y + 14)
		if self.rect.x < 870:
			self.rect.x += 20

class Barravidagoku(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/barravida_naruto.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(18, 4)
	def update(self):
		if barravidagoku.rect.x <= -152:
			personaje.muerto = 1
			ese_compa.play()
		if disparo.rect.y >= (personaje.rect.y - 56):
			if disparo.rect.y <= (personaje.rect.y + 62):
				if disparo.rect.x >= personaje.rect.x:
					if disparo.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400
						hay.play()
		if minicell.rect.y >= (personaje.rect.y - 56):
			if minicell.rect.y <= (personaje.rect.y + 62):
				if minicell.rect.x >= personaje.rect.x:
					if minicell.rect.x <= (personaje.rect.x + 43):
						barravidagoku.rect.x -= 26
						disparo.rect.x = -400

class Minicell(Sprite):
	def __init__(self):
		self.image = minicell = pygame.image.load("Imagenes/sasuke.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(750, 300)
		self.bandera = 0
		self.muerto = 0
	def update(self):
		if self.rect.y == 40:
			self.bandera = 0
		elif self.rect.y == 410:
			self.bandera = 1

		if self.bandera == 0:
			self.rect.y += 10
		elif self.bandera == 1:
			self.rect.y -= 10
	def dificil(self):
		if self.rect.x < 0:
			self.rect.x = 800
		if self.rect.y > 600:
			self.rect.y = 0
		self.rect.x -= 10
		self.rect.y += 10

class Disparo(Sprite):
	def __init__(self):
		self.image = barravidagoku = pygame.image.load("Imagenes/ataque_s.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(-400, -400)
		
	def update(self):
		if self.rect.x == -400:
			if minicell.rect.y == personaje.rect.y:
				self.rect.x = (minicell.rect.x - 60)
				self.rect.y = (minicell.rect.y - 14)
				disparo2.play()
		if self.rect.x > -400:
			self.rect.x -= 5

class Barravidaminicell(Sprite):
	def __init__(self):
		self.image = barravidaminicell = pygame.image.load("Imagenes/barravida_sasuke.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(612, 4)
	def update(self):
		if self.rect.x >= 782:
			minicell.muerto = 1
			siu.play()
		if kamehameha.rect.y >= minicell.rect.y:
			if kamehameha.rect.y <= (minicell.rect.y + 62):
				if kamehameha.rect.x >= minicell.rect.x:
					if kamehameha.rect.x <= (minicell.rect.x + 43):
						self.rect.x += 6
						kamehameha.rect.x = 900
						ayuda.play()

if __name__ == '__main__':
	# Variables.
	salir = False

	# Variables Sonidos.
	pygame.mixer.music.load("Sonidos/naruto.ogg")
	pygame.mixer.music.set_volume(0.4)
	
	disparo1 = pygame.mixer.Sound("Sonidos/disparo_n.ogg")
	disparo2 = pygame.mixer.Sound("Sonidos/disparo_s.ogg")

	hay = pygame.mixer.Sound("Sonidos/hay.ogg")
	ayuda = pygame.mixer.Sound("Sonidos/ayuda.ogg")

	ese_compa = pygame.mixer.Sound("Sonidos/ese_compa.ogg")
	siu = pygame.mixer.Sound("Sonidos/siu.ogg")

	# Establezco la pantalla.
	screen = pygame.display.set_mode((800,485))
	

	# Establezco el título.
	pygame.display.set_caption("Naruto vs Sasuke")

	# Creo dos objetos surface.
	fondo = pygame.image.load("Imagenes/paisaje.jpg").convert()
	cuadrovidagoku = pygame.image.load("Imagenes/cuadrovida_naruto.png").convert_alpha()
	cuadrovidaminicell = pygame.image.load("Imagenes/cuadrovida_sasuke.png").convert_alpha()
	hasperdido = pygame.image.load("Imagenes/Hasperdido.png").convert()
	hasperdido.set_colorkey([0,0,0])
	hasganado = pygame.image.load("Imagenes/Hasganado.png").convert()
	hasganado.set_colorkey([0,0,0])
	# .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

	# Objetos
	temporizador = pygame.time.Clock()
	personaje = Personaje()
	kamehameha = Kamehameha()
	minicell = Minicell()
	disparo = Disparo()
	barravidagoku = Barravidagoku()
	barravidaminicell = Barravidaminicell()

	# Movimiento del personaje.
	while not salir:
		personaje.update()
		kamehameha.update()
		if barravidaminicell.rect.x < 697:
			minicell.update()
		else:
			minicell.dificil()
		disparo.update()
		barravidagoku.update()
		barravidaminicell.update()

		# actualizacion grafica
		screen.blit(fondo, (0, 0))
		screen.blit(personaje.image, personaje.rect)
		screen.blit(kamehameha.image, kamehameha.rect)
		screen.blit(minicell.image, minicell.rect)
		screen.blit(disparo.image, disparo.rect)
		screen.blit(barravidagoku.image, barravidagoku.rect)
		screen.blit(barravidaminicell.image, barravidaminicell.rect)
		screen.blit(cuadrovidagoku, (0,0))
		screen.blit(cuadrovidaminicell, (608,0))
		if personaje.muerto == 1:
			screen.blit(hasperdido, (350,195))
		if minicell.muerto == 1:
			screen.blit(hasganado, (350,195))
		pygame.display.flip()

		if personaje.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		elif minicell.muerto == 1:
			pygame.time.delay(3000)
			salir = True
		temporizador.tick(60)

		# gestion de eventos
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				salir = True
