#!/usr/bin/python

import os
from random import randrange
import time

# czyszczenie ekranu
os.system("clear")


class Map:
	# zmienne do interfejsu
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	NORMAL = '\033[0m'
	
	#zmienne potrzebne do wyrysowania map gry
	myMap = ""

	def __getitem__(self, key):
		return self.myMap[key]

	def __init__(self): # ok
		self.myMap += "  ABCDEFGHIJ\n"
		for tmp_y in range(10):
			self.myMap += str(tmp_y+1).zfill(2)
			for tmp_x in range(10):
				self.myMap += "."
			self.myMap += "\n"
	
	def __str__(self): # ok
		return self.myMap
	
	def fill_map(self): # ok
	
		#zdefiniowac funkcje sprawdzajaca sasiadow
		def chceck_neighbors(wsp_x, wsp_y):
			position = 13*wsp_y + wsp_x + 1
			
			# sprawdzanie podstawowych kierunkow
			up = position - 13
			down = position + 13
			left = position - 1
			right = position + 1
			
			# sprawdzanie skosnych kierunkow
			up_left = position - 14
			up_right = position - 12
			down_left = position + 14
			down_right = position + 12
			
			# ochrona przed wyjsciem z zakresu stringa
			if down > 141:
				down = 1
			if down_left > 141:
				down_left = 1
			if down_right > 141:
				down_right = 1
			
			if self.myMap[up] != 'X' and self.myMap[down] != 'X' and \
			   self.myMap[left] != 'X' and self.myMap[right] != 'X' and \
			   self.myMap[up_left] != 'X' and self.myMap[up_right] != 'X' and \
			   self.myMap[down_left] != 'X' and self.myMap[down_right] != 'X' and \
			   self.myMap[position] != 'X':
			   return True
			else:
				return False
		
		# umieszczanie na mapie 'jedynek'
		tmp = 4
		while tmp > 0:
			wsp_x = randrange(1,11)
			wsp_y = randrange(1,11)
			if chceck_neighbors(wsp_x,wsp_y):
				self.update_map(wsp_x,wsp_y,'X')
				tmp -= 1
				
		# umieszczanie na mapie 'dwojek'
		tmp = 3
		while tmp > 0:
			direction = randrange(1,3)
			if direction == 1:
				wsp_x = randrange(1,11)
				wsp_y = randrange(2,11)
				if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x,wsp_y-1):
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x,wsp_y-1,'X')
					tmp -= 1
			else:
				wsp_x = randrange(2,11)
				wsp_y = randrange(1,11)
				if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x-1,wsp_y):
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x-1,wsp_y,'X')
					tmp -= 1
		
		# umieszczanie na mapie 'trojek'
		tmp = 2
		while tmp > 0:
			direction = randrange(1,3)
			if direction == 1:
				wsp_x = randrange(1,11)
				wsp_y = randrange(2,10)
				if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x,wsp_y-1) and \
				   chceck_neighbors(wsp_x, wsp_y+1):
				   
					self.update_map(wsp_x,wsp_y+1,'X')
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x,wsp_y-1,'X')
					tmp -= 1
			else:
				wsp_x = randrange(2,10)
				wsp_y = randrange(1,11)
				if chceck_neighbors(wsp_x, wsp_y) and chceck_neighbors(wsp_x-1, wsp_y)and \
				   chceck_neighbors(wsp_x+1, wsp_y):
				   
					self.update_map(wsp_x+1,wsp_y,'X')
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x-1,wsp_y,'X')
					tmp -= 1
					
		# umieszczanie na mapie 'czworek'
		tmp = 1
		while tmp > 0:
			direction = randrange(1,3)
			if direction == 1:
				wsp_x = randrange(1,11)
				wsp_y = randrange(2,9)
				if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x,wsp_y-1) and \
				   chceck_neighbors(wsp_x, wsp_y+1) and chceck_neighbors(wsp_x, wsp_y+2):
					
					self.update_map(wsp_x,wsp_y+2,'X')
					self.update_map(wsp_x,wsp_y+1,'X')
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x,wsp_y-1,'X')
					tmp -= 1
			else:
				wsp_x = randrange(2,9)
				wsp_y = randrange(1,11)
				if chceck_neighbors(wsp_x, wsp_y) and chceck_neighbors(wsp_x-1, wsp_y)and \
				   chceck_neighbors(wsp_x+1, wsp_y) and chceck_neighbors(wsp_x+2, wsp_y):
					
					self.update_map(wsp_x+2,wsp_y,'X')
					self.update_map(wsp_x+1,wsp_y,'X')
					self.update_map(wsp_x,wsp_y,'X')
					self.update_map(wsp_x-1,wsp_y,'X')
					tmp -= 1
		
	# funkcja zamieniajaca znak na mapie
	def update_map(self, wsp_x, wsp_y, character): #ok
		position = 13*wsp_y + wsp_x + 1
		tmp_map = self.myMap
		self.myMap = tmp_map[:position]
		self.myMap += character
		self.myMap += tmp_map[position+1:]

		
class Game:
	# zmienne do interfejsu
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	NORMAL = '\033[0m'
	
	
	def start_game(self):
		menu = 1
		key = 'f'
		redraw = True
		
		self.draw(menu)
		
		while True:
			
			key = raw_input()
			
			if menu == 1:
				# mechanika menu
				if key == 'a':
					menu = 2
					redraw = True
				elif key == 'b':
					menu = 3
					redraw = True
				elif key == 'c':
					menu = 4
					redraw = True
				elif key == 'd':
					break
				else:
					print "Nieznany klawisz !!!"
				
			# gra
			elif menu == 2:
				if key == 'q':
					menu = 1
					redraw = True
			# autor	
			elif menu == 3:
				if key == 'q':
					menu = 1
					redraw = True
			# ustawienia
			elif menu == 4:
				if key == 'q':
					menu = 1
					redraw = True
			
			if redraw:
				self.draw(menu)
				redraw = False	
		
	def print_all_map(self):
		os.system("clear")
		pixel = 70
		print "========================".center(pixel)
		print self.YELLOW + "Mapa przeciwnika".center(pixel) + self.NORMAL	
		print "========================".center(pixel)
		print self.computer_map
		print "\n"
		print "========================".center(pixel)
		print self.YELLOW + "Twoja mapa".center(pixel) + self.NORMAL	
		print "========================".center(pixel)
		print self.my_map
		
	def run_game(self):
		wsp_x = 0
		wsp_y = 0
		i_wsp_y = 0
		i_wsp_x = 0
		
		mySunkenShips = 0
		computerSunkenShips = 0
		
		self.my_map = Map()
		self.computer_map = Map()
		self.tmp = Map()
			
		def check_win(): #ok
			if mySunkenShips != 20 and computerSunkenShips != 20:
				return True
			else:
				return False
		
		# uzupelnianie map
		self.my_map.fill_map()
		self.computer_map.fill_map()
		
		while check_win():
			os.system("clear")
			self.print_all_map()
			
			# wsp_x = raw_input("Podaj wsp x: ")
			# wsp_y = raw_input("Podaj wsp y: ")
			
			wsp_x = 'A'
			wsp_y = 1
			
			# konwersja wsp_x na int
			try:
				i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
			except ValueError:                  # kod obslugujacy bledy
				print "blad x"
			
			# konwersja wsp_y na int
			try:
				i_wsp_y = int(wsp_y)
			except ValueError:                  # kod obslugujacy bledy
				print "blad y"
			
			# wykonanie mojego ruchu
			self.computer_map.update_map(i_wsp_x, i_wsp_y, '*')
			
			#wykonanie ruchu komputera
			while True:
				i_wsp_x = randrange(1,11)
				i_wsp_y = randrange(1,11)
				position = 13 * i_wsp_y + i_wsp_x + 1
				if self.my_map[position] != '*':
					#sprawdzenie czy nastapilo trafienie w statek
					if self.my_map[position] == 'X':
						mySunkenShips += 1
					self.my_map.update_map(i_wsp_x, i_wsp_y, '*')
					break
			
			time.sleep(0.05)
		
		# sprawdzenie kto wygral
		if mySunkenShips >= 20:
			os.system("clear")
			print "Komputer wygral !!!!!!!!"
			pixel = 70
			print "\n\n\n\n"
			print "=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			
		if computerSunkenShips >= 20:
			os.system("clear")
			print "Wygrales !!!!!!!!!"
			pixel = 70
			print "\n\n\n\n"
			print "=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			
	
	# funkcja rysujaca interfejs menu
	def draw(self, screen):
		os.system("clear")
		pixel = 70
		if screen == 1:
			print "========================".center(pixel)
			print self.RED + "Witam w grze Statki !!!".center(pixel) + self.NORMAL	
			print "========================".center(pixel)
			print "MENU: ".center(pixel)
			print "========================".center(pixel)
			print " a - START".center(pixel)
			print " b - AUTOR".center(pixel)
			print " c - USTAWIENIA".center(pixel)
			print " d - WYJSCIE".center(pixel)
		elif screen == 2:
			# start gry
			self.run_game()
			
		elif screen == 3:
			# Autor
			print "==== AUTOR GRY: ==== ".center(pixel)
			print "1. Damian Polchlopek  ".center(pixel)
			print "=====================".center(pixel)
			print "\n\n\n\n"
			print "=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
		
		elif screen == 4:
			# ustawienia gry
			print "Ustawienia gry"
			print "\n\n\n\n"
			print "=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
		
		
		
game = Game()
game.start_game()
