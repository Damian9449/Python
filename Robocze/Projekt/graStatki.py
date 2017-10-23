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
	
	def manual_fill_map(self):
		
		# rozmieszczenie jedynek
		tmp = 1
		while tmp != 5:
			os.system("clear")
			print self.myMap
			print "Rozmieszczamy 'jedynke' "
			wsp_x = raw_input("Podaj wsp x: ")
			wsp_y = raw_input("Podaj wsp y: ")
			
			# konwersja wsp_x na int
			try:
				i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
			except ValueError:                  # kod obslugujacy bledy
				print "Blad przy konwersji wsp x"
			
			# konwersja wsp_y na int
			try:
				i_wsp_y = int(wsp_y)
			except ValueError:                  # kod obslugujacy bledy
				print "Blad pry konwersji wsp y"
			
			self.update_map(i_wsp_x, i_wsp_y, 'X')
			tmp += 1
		
		
		#rozmieszczenie dwojek
		tmp = 1
		while tmp != 4:
			os.system("clear")
			print self.myMap
			print "Rozmieszczamy 'dwojke' "
			
			for i in range(2):
				wsp_x = raw_input("Podaj wsp x: ")
				wsp_y = raw_input("Podaj wsp y: ")
				
				# konwersja wsp_x na int
				try:
					i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad przy konwersji wsp x"
				
				# konwersja wsp_y na int
				try:
					i_wsp_y = int(wsp_y)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad pry konwersji wsp y"
				
				self.update_map(i_wsp_x, i_wsp_y, 'X')
				
			tmp += 1
		
		#rozmieszczenie trojek		
		tmp = 1
		while tmp != 3:
			os.system("clear")
			print self.myMap
			print "Rozmieszczamy 'trojke' "
			
			for i in range(3):
				wsp_x = raw_input("Podaj wsp x: ")
				wsp_y = raw_input("Podaj wsp y: ")
				
				# konwersja wsp_x na int
				try:
					i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad przy konwersji wsp x"
				
				# konwersja wsp_y na int
				try:
					i_wsp_y = int(wsp_y)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad pry konwersji wsp y"
				
				self.update_map(i_wsp_x, i_wsp_y, 'X')
			
			tmp += 1
				
			
		os.system("clear")
		print self.myMap
		# rozmieszczenie czworki
		print "Rozmieszczamy 'czworke' "
		for i in range(4):
			wsp_x = raw_input("Podaj wsp x: ")
			wsp_y = raw_input("Podaj wsp y: ")
			
			# konwersja wsp_x na int
			try:
				i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
			except ValueError:                  # kod obslugujacy bledy
				print "Blad przy konwersji wsp x"
			
			# konwersja wsp_y na int
			try:
				i_wsp_y = int(wsp_y)
			except ValueError:                  # kod obslugujacy bledy
				print "Blad pry konwersji wsp y"
			
			self.update_map(i_wsp_x, i_wsp_y, 'X')
	
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
	
	autoFillMap = False
	
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
				elif key == 'a':
					os.system("clear")
					pixel = 70
					print self.GREEN+"=== WYBIERZ SPOSOB GENEROWANIA MAPY ==="
					print self.BLUE+" a - sposob automatyczny"
					print self.BLUE+" b - sposob reczny"+self.NORMAL
					
					key = raw_input()
					
					if key == 'a':
						self.autoFillMap = True
					elif key == 'b':
						self.autoFillMap = False
					else:
						print " WPROWADZILES ZLA LITERE !!!"
						print " PATRZ MENU WYZEJ !!!"
					
					if key == 'a' or key == 'b':
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
		
		# zmienna przechwujaca informacje kogo jest kolejny ruchu
		# 1 - gracz
		# 2 - komputer
		nextShoot = 1
		
		self.my_map = Map()
		self.computer_map = Map()
		self.tmp = Map()
			
		def check_win(): #ok
			if mySunkenShips != 20 and computerSunkenShips != 20:
				return True
			else:
				return False
		
		# uzupelnianie map
		if self.autoFillMap:
			self.my_map.fill_map()
		else:
			self.my_map.manual_fill_map()
		
		self.computer_map.fill_map()
		
		while check_win():
			os.system("clear")
			self.print_all_map()
			
			if nextShoot == 1:
			
				wsp_x = raw_input("Podaj wsp x: ")
				wsp_y = raw_input("Podaj wsp y: ")
				
				# konwersja wsp_x na int
				try:
					i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad przy konwersji wsp x"
				
				# konwersja wsp_y na int
				try:
					i_wsp_y = int(wsp_y)
				except ValueError:                  # kod obslugujacy bledy
					print "Blad pry konwersji wsp y"
				
				# ustalenie kto wykonuje kolejny ruchu
				position = 13 * i_wsp_y + i_wsp_x + 1
				if self.computer_map[position] == 'X':
					computerSunkenShips += 1
					nextShoot = 1
				else:
					nextShoot = 2
				
				# wykonanie mojego ruchu
				self.computer_map.update_map(i_wsp_x, i_wsp_y, '*')
				
			
			if nextShoot == 2:
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
				
				#kolejka gracza
				nextShoot = 1
			
			time.sleep(0.05)
		
		# sprawdzenie kto wygral
		if mySunkenShips >= 20:
			os.system("clear")
			pixel = 70
			print self.GREEN+"Przegrales :( " + self.NORMAL
			print "\n\n\n\n"
			print self.RED+"=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			print self.NORMAL
			
			
		if computerSunkenShips >= 20:
			os.system("clear")
			pixel = 70
			print self.GREEN+"WYGRALES !!!!!!!!!"+self.NORMAL
			print "\n\n\n\n"
			print self.RED+"=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			print self.NORMAL
				
	# funkcja rysujaca interfejs menu
	def draw(self, screen):
		os.system("clear")
		pixel = 70
		if screen == 1:
			print self.YELLOW+"========================".center(pixel)
			print self.RED + "Witam w grze Statki !!!".center(pixel) + self.NORMAL	
			print self.YELLOW+"========================".center(pixel)
			print self.GREEN+"MENU: ".center(pixel), self.NORMAL
			print self.YELLOW+"========================".center(pixel)
			print self.NORMAL+" a - START".center(pixel)
			print " b - AUTOR".center(pixel)
			print " c - USTAWIENIA".center(pixel)
			print " d - WYJSCIE".center(pixel)
			print self.YELLOW+"========================".center(pixel), self.NORMAL
		elif screen == 2:
			# start gry
			self.run_game()
			
		elif screen == 3:
			# Autor
			print self.GREEN+"==== AUTOR GRY: ==== ".center(pixel)
			print self.BLUE+"1. Damian Polchlopek  ".center(pixel)
			print self.GREEN+"=====================".center(pixel)
			print "\n\n\n\n"
			print self.RED+"=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			print self.NORMAL
		
		elif screen == 4:
			# ustawienia gry
			print self.GREEN+"==== AKTUALNE USTAWIENIA GRY: ===="+self.NORMAL
			print self.BLUE+"-----------------------------------------"+self.NORMAL
			print self.BLUE+" Automatyczne generowanie mapy -"+self.NORMAL, self.autoFillMap
			print self.BLUE+"-----------------------------------------"+self.NORMAL
			print "\n\n\n\n"
			print self.GREEN+"==== ABY ZMIENIC USTAWIENIA WCISNIJ: ===="+self.NORMAL
			print self.BLUE+" * a - sposob generowania mapy"
			print "\n\n\n\n"
			print self.RED+"=====================".center(pixel)
			print "q - menu glowne  ".center(pixel)
			print "=====================".center(pixel)
			print self.NORMAL
		
		
game = Game()
game.start_game()
