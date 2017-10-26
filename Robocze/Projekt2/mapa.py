#!/usr/bin/python

import os
from random import randrange
import time
import sys

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
	myMap = list()

	def __init__(self): # ok
		myMapColumn = ['.' for i in range(10)] + [' ']
		self.myMap = [myMapColumn for i in range(10)]
		self.myMap.insert(0, [ chr(x) for x in range(65, 75)])
		self.myMap[0].insert(11, ' ')
		self.myMap[0].insert(0, '  ')
		self.myMap.append([' ' for i in range(12)])
		
		for i in range(10):
			self.myMap[i+1] = [str(i+1).zfill(2)] + self.myMap[i+1]
      
	def __str__(self): # ok
		return "Wskazane jest wypisanie mapy za pomoca specjalnej funkcji"
	
	def print_map(self):
		for row in self.myMap:
			for node in row:
				sys.stdout.write(node)
			print ""
	
	# funkcja zamieniajaca znak na mapie
	def update_map(self, wsp_x, wsp_y, character): #ok
		self.myMap[wsp_y][wsp_x] = character
	
	def manual_fill_map(self):
		# rozmieszczenie jedynek
		tmp = 1
		while tmp != 5:
			os.system("clear")
			self.print_map()
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
			self.print_map()
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
			self.print_map()
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
		self.print_map()
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
		
		self.print_map()
	
	def fill_map(self): # ok
	
		# funkcja sprawdzajaca sasiadow
		def chceck_neighbors(wsp_x, wsp_y):
			# sprawdzanie podstawowych kierunkow
			x_up = wsp_x
			y_up = wsp_y - 1
			x_down = wsp_x
			y_down = wsp_y + 1
			x_left = wsp_x - 1
			y_left = wsp_y
			x_right = wsp_x + 1
			y_right = wsp_y
			
			# sprawdzanie skosnych kierunkow
			x_up_left = wsp_x - 1
			y_up_left = wsp_y - 1
			x_up_right = wsp_x + 1
			y_up_right = wsp_y - 1
			x_down_left = wsp_x - 1
			y_down_left = wsp_y + 1
			x_down_right = wsp_x + 1
			y_down_right = wsp_y + 1
			
			# ochrona przed wyjsciem z zakresu stringa
			# if down > 141:
				# down = 1
			# if down_left > 141:
				# down_left = 1
			# if down_right > 141:
				# down_right = 1
				
			# if self.myMap[up] != 'X' and self.myMap[down] != 'X' and \
			   # self.myMap[left] != 'X' and self.myMap[right] != 'X' and \
			   # self.myMap[up_left] != 'X' and self.myMap[up_right] != 'X' and \
			   # self.myMap[down_left] != 'X' and self.myMap[down_right] != 'X' and \
			   # self.myMap[position] != 'X':
			   # return True
			# else:
				# return False
				
			
			if self.myMap[y_up][x_up] != 'X' and self.myMap[y_down][x_down] != 'X' and \
			   self.myMap[y_left][x_left] != 'X' and self.myMap[y_right][x_right] != 'X' and \
			   self.myMap[y_up_left][x_up_left] != 'X' and self.myMap[y_up_right][x_up_right] != 'X' and \
			   self.myMap[y_down_left][x_down_left] != 'X' and self.myMap[y_down_right][x_down_right] != 'X' and \
			   self.myMap[wsp_y][wsp_x] != 'X':
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
	
	
	
		
map = Map()
print map
map.print_map()
#map.update_map(1,1,'X')
map.print_map()
#map.manual_fill_map()
map.fill_map()
map.print_map()
