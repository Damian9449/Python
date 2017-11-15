#!/usr/bin/python

import os
from random import randrange
import sys

# clear console
os.system("clear")

class Map:
    """Class representing the game map"""
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    UNDERLINE = '\033[4m'
    NORMAL = '\033[0m' 

    myMap = list()


    # list, which storing areas of all ships
    allShips = []

    def __getitem__(self, key):
        """Operator []"""
        return self.myMap[key]

    def __init__(self):
        """Constructor of map"""
        myMapColumn = [self.BLUE+'.'+self.NORMAL for i in range(10)] + [' ']
        self.myMap = [myMapColumn for i in range(10)]
        self.myMap.insert(0, [ self.GREEN+chr(x)+self.NORMAL for x in range(65, 75)])
        self.myMap[0].insert(11, ' ')
        self.myMap[0].insert(0, '  ')
        self.myMap.append([' ' for i in range(12)])
        
        for i in range(10):
            self.myMap[i+1] = [self.GREEN+str(i+1).zfill(2)+self.NORMAL] + self.myMap[i+1]
        
        self.allShips = [list() for i in range(10)]		
        
    def __str__(self):
        """Return a warning about bad map output"""
        return "Wskazane jest wypisanie mapy za pomoca specjalnej funkcji"

    def print_map(self):
        """Write a map to standard output"""
        for row in self.myMap:
            for node in row:
                sys.stdout.write(node)
            print ""


    def update_map(self, wsp_x, wsp_y, character):
        """Change character on map"""
        self.myMap[wsp_y][wsp_x] = character

    def manual_fill_map(self):
        """Arrange the ships on the map manually"""
        # place 4 ships with one field
        tmp = 1
        while tmp != 5:
            os.system("clear")
            self.print_map()
            print "Rozmieszczamy 'jedynke' "
            wsp_x = raw_input("Podaj wsp x: ")
            wsp_y = raw_input("Podaj wsp y: ")
            
            try:
                i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
            except ValueError:                 
                print "Blad przy konwersji wsp x"
            
            try:
                i_wsp_y = int(wsp_y)
            except ValueError:                 
                print "Blad pry konwersji wsp y"
            
            self.update_map(i_wsp_x, i_wsp_y, 'X')
            self.allShips[tmp-1].append([wsp_x, wsp_y])
            tmp += 1
        
        
        # place 3 ships with two field
        tmp = 1
        while tmp != 4:
            os.system("clear")
            self.print_map()
            print "Rozmieszczamy 'dwojke' "
            
            for i in range(2):
                wsp_x = raw_input("Podaj wsp x: ")
                wsp_y = raw_input("Podaj wsp y: ")
                
                try:
                    i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
                except ValueError:                 
                    print "Blad przy konwersji wsp x"
                
                try:
                    i_wsp_y = int(wsp_y)
                except ValueError:            
                    print "Blad pry konwersji wsp y"
                
                self.update_map(i_wsp_x, i_wsp_y, 'X')
                self.allShips[tmp+3].append([wsp_x, wsp_y])
                
            tmp += 1
        
        # place 2 ships with three field
        tmp = 1
        while tmp != 3:
            os.system("clear")
            self.print_map()
            print "Rozmieszczamy 'trojke' "
            
            for i in range(3):
                wsp_x = raw_input("Podaj wsp x: ")
                wsp_y = raw_input("Podaj wsp y: ")
                
                try:
                    i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
                except ValueError:           
                    print "Blad przy konwersji wsp x"
                
                try:
                    i_wsp_y = int(wsp_y)
                except ValueError:      
                    print "Blad pry konwersji wsp y"
                
                self.update_map(i_wsp_x, i_wsp_y, 'X')
                self.allShips[tmp+6].append([wsp_x, wsp_y])
            
            tmp += 1
            
            
        os.system("clear")
        self.print_map()
        # place 1 ship with four field
        print "Rozmieszczamy 'czworke' "
        for i in range(4):
            wsp_x = raw_input("Podaj wsp x: ")
            wsp_y = raw_input("Podaj wsp y: ")
            
            try:
                i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
            except ValueError:              
                print "Blad przy konwersji wsp x"
            
            try:
                i_wsp_y = int(wsp_y)
            except ValueError:             
                print "Blad pry konwersji wsp y"
            
            self.update_map(i_wsp_x, i_wsp_y, 'X')
            self.allShips[9].append([wsp_x, wsp_y])
        
        self.print_map()

    def fill_map(self):
        """Arrange the ships on the map radomly"""

        def chceck_neighbors(wsp_x, wsp_y):
            """Chceck the neighboring area"""
            
            # determination of basic directions
            x_up = wsp_x
            y_up = wsp_y - 1
            x_down = wsp_x
            y_down = wsp_y + 1
            x_left = wsp_x - 1
            y_left = wsp_y
            x_right = wsp_x + 1
            y_right = wsp_y
            
            # determination of oblique directions
            x_up_left = wsp_x - 1
            y_up_left = wsp_y - 1
            x_up_right = wsp_x + 1
            y_up_right = wsp_y - 1
            x_down_left = wsp_x - 1
            y_down_left = wsp_y + 1
            x_down_right = wsp_x + 1
            y_down_right = wsp_y + 1
            
            if self.myMap[y_up][x_up] != 'X' and self.myMap[y_down][x_down] != 'X' and \
               self.myMap[y_left][x_left] != 'X' and self.myMap[y_right][x_right] != 'X' and \
               self.myMap[y_up_left][x_up_left] != 'X' and self.myMap[y_up_right][x_up_right] != 'X' and \
               self.myMap[y_down_left][x_down_left] != 'X' and self.myMap[y_down_right][x_down_right] != 'X' and \
               self.myMap[wsp_y][wsp_x] != 'X':
                return True
            else:
                return False
        
        # place 4 ships with one field
        tmp = 4
        while tmp > 0:
            wsp_x = randrange(1,11)
            wsp_y = randrange(1,11)
            if chceck_neighbors(wsp_x,wsp_y):
                self.update_map(wsp_x,wsp_y,'X')
                self.allShips[tmp-1].append([wsp_x, wsp_y])
                tmp -= 1
                
        # place 3 ships with two field
        tmp = 3
        while tmp > 0:
            direction = randrange(1,3)
            if direction == 1:
                wsp_x = randrange(1,11)
                wsp_y = randrange(2,11)
                if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x,wsp_y-1):
                    self.update_map(wsp_x,wsp_y,'X')
                    self.update_map(wsp_x,wsp_y-1,'X')
                    self.allShips[tmp+3].append([wsp_x, wsp_y])
                    self.allShips[tmp+3].append([wsp_x, wsp_y-1])
                    tmp -= 1
            else:
                wsp_x = randrange(2,11)
                wsp_y = randrange(1,11)
                if chceck_neighbors(wsp_x,wsp_y) and chceck_neighbors(wsp_x-1,wsp_y):
                    self.update_map(wsp_x,wsp_y,'X')
                    self.update_map(wsp_x-1,wsp_y,'X')
                    self.allShips[tmp+3].append([wsp_x, wsp_y])
                    self.allShips[tmp+3].append([wsp_x, wsp_y-1])
                    tmp -= 1
        
        # place 2 ships with three field
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
                    
                    self.allShips[tmp+6].append([wsp_x, wsp_y+1])
                    self.allShips[tmp+6].append([wsp_x, wsp_y])
                    self.allShips[tmp+6].append([wsp_x, wsp_y-1])
                    tmp -= 1
            else:
                wsp_x = randrange(2,10)
                wsp_y = randrange(1,11)
                if chceck_neighbors(wsp_x, wsp_y) and chceck_neighbors(wsp_x-1, wsp_y)and \
                   chceck_neighbors(wsp_x+1, wsp_y):
                   
                    self.update_map(wsp_x+1,wsp_y,'X')
                    self.update_map(wsp_x,wsp_y,'X')
                    self.update_map(wsp_x-1,wsp_y,'X')
                    
                    self.allShips[tmp+6].append([wsp_x+1, wsp_y])
                    self.allShips[tmp+6].append([wsp_x, wsp_y])
                    self.allShips[tmp+6].append([wsp_x-1, wsp_y])
                    tmp -= 1
                    
        # place 1 ship with four field
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
                    
                    self.allShips[9].append([wsp_x, wsp_y+2])
                    self.allShips[9].append([wsp_x, wsp_y+1])
                    self.allShips[9].append([wsp_x, wsp_y])
                    self.allShips[9].append([wsp_x, wsp_y-1])
                    
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
                    
                    self.allShips[9].append([wsp_x+2, wsp_y])
                    self.allShips[9].append([wsp_x+1, wsp_y])
                    self.allShips[9].append([wsp_x, wsp_y])
                    self.allShips[9].append([wsp_x-1, wsp_y])
                    
                    tmp -= 1
	
class Game:
    """Class representing the game"""
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    NORMAL = '\033[0m'

    autoFillMap = True

    my_map = Map()
    computer_map = Map()
    tmp_map = Map()

    def color_ships(self, tmp_map, computer_map):
        """Change character sunken ships"""
        for ship in self.computer_map.allShips:
            triger = True;
            for area in range(len(ship)):
                x_tmp = ship[area][0]
                y_tmp = ship[area][1]
                
                if self.tmp_map[y_tmp][x_tmp] == 'X' and self.computer_map[y_tmp][x_tmp] == 'X':
                    print "True"
                else:
                    triger = False
                    break
                
            if triger:
                for area in range(len(ship)):
                    x_tmp = ship[area][0]
                    y_tmp = ship[area][1]
                    self.tmp_map[y_tmp][x_tmp] = '@'
                
    def start_game(self):
        """Game menu logic"""
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
        """Print all maps to standard output """

        os.system("clear")
        pixel = 70
        # print self.RED+"========================".center(pixel),self. NORMAL
        # print self.YELLOW + "Computer".center(pixel) + self.NORMAL	
        # print self.RED+"========================".center(pixel), self.NORMAL
        # self.computer_map.print_map()
        print self.RED+"========================".center(pixel),self. NORMAL
        print self.YELLOW + "Twoje strzaly".center(pixel) + self.NORMAL	
        print self.RED+"========================".center(pixel), self.NORMAL
        self.tmp_map.print_map()
        print "\n"
        print self.RED+"========================".center(pixel), self.NORMAL
        print self.YELLOW + "Twoja mapa".center(pixel) + self.NORMAL	
        print self.RED+"========================".center(pixel), self.NORMAL
        self.my_map.print_map()
        
    def run_game(self):
        """Logic of the whole game"""
        wsp_x = 0
        wsp_y = 0
        i_wsp_y = 0
        i_wsp_x = 0
        
        mySunkenShips = 0
        computerSunkenShips = 0
        
        # A variable that holds information about next move
        # 1 - player
        # 2 - computer
        nextShoot = 1
        
        self.my_map = Map()
        self.computer_map = Map()
        self.tmp_map = Map()
            
        def check_win():
            if mySunkenShips != 20 and computerSunkenShips != 20:
                return True
            else:
                return False
        
        # fill map
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
                
                # conversion wsp_x to int
                try:
                    i_wsp_x = int(ord(wsp_x) - ord('A') + 1)
                except ValueError:                  
                    print "Blad przy konwersji wsp x"
                
                # conversion wsp_y to int
                try:
                    i_wsp_y = int(wsp_y)
                except ValueError:                  
                    print "Blad pry konwersji wsp y"
                
                
                # Check who doing next move
                # Verify that the ship has hit
                if self.computer_map[i_wsp_y][i_wsp_x] == 'X':
                    self.tmp_map.update_map(i_wsp_x, i_wsp_y, 'X')
                    computerSunkenShips += 1
                    nextShoot = 1
                else:
                    nextShoot = 2
                    self.tmp_map.update_map(i_wsp_x, i_wsp_y, '*')
                    
            if nextShoot == 2:
                
                while True:
                    i_wsp_x = randrange(1,11)
                    i_wsp_y = randrange(1,11)
                    if self.my_map[i_wsp_y][i_wsp_x] != '*':
                        # Verify that the ship has hit
                        if self.my_map[i_wsp_y][i_wsp_x] == 'X':
                            mySunkenShips += 1
                        self.my_map.update_map(i_wsp_x, i_wsp_y, '*')
                        break
                
                # player's turn
                nextShoot = 1
                
            self.color_ships(self.tmp_map, self.computer_map)
            
        
        # check who win
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
                
    def draw(self, screen):
        """Draws the menu interface"""
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
            self.run_game()
            
        elif screen == 3:
            print self.GREEN+"==== AUTOR GRY: ==== ".center(pixel)
            print self.BLUE+"1. Damian Polchlopek  ".center(pixel)
            print self.GREEN+"=====================".center(pixel)
            print "\n\n\n\n"
            print self.RED+"=====================".center(pixel)
            print "q - menu glowne  ".center(pixel)
            print "=====================".center(pixel)
            print self.NORMAL
        
        elif screen == 4:
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
