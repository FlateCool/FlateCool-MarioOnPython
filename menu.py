import pygame
from settings import *


class Button():
    def __init__(self, x, y, w, h, text, screen,
                 padding_x = 0, padding_y = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.screen = screen   
        self.text = text        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
       
        
        
    def draw(self):
        text_surface = self.font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (self.x + self.padding_x, self.y + self.padding_y)
        self.screen.blit(text_surface, text_rect)
        
      

class Menu():
    def __init__(self, screen, game):
        self.legends = {0:"START", 1:"OPTION", 2:"CREDITS", 3:"QUIT" }
        self.npointer = 0
        self.screen = screen
        self.game = game
        self.submenu = False
        
        self.buttons = [
            Button(WIN_WIDTH // 2, 200, 300, 50, self.legends[0], self.screen, 0, 0),
            Button(WIN_WIDTH // 2, 250, 300, 50, self.legends[1], self.screen, 0, 0),
            Button(WIN_WIDTH // 2, 300, 300, 50, self.legends[2], self.screen, 0, 0),
            Button(WIN_WIDTH // 2, 350, 300, 50, self.legends[3], self.screen, 0, 0),
        ]
        
        
    def next(self):
        self.npointer = (self.npointer + 1) % len(self.legends)        
        
    def previous(self):
        if self.npointer == 0:
            self.npointer = len(self.legends) - 1
        else:
            self.npointer -= 1           
        
            
    def enter(self):
        if self.submenu:
            if self.legends[self.npointer] == 'START':
                self.submenu = False
                self.game.toggle()
            elif self.legends[self.npointer] == 'QUIT':
                self.game.GameQuit = True
            else:                
                print(self.legends[self.npointer])
                
    def draw(self):
        for num, button in enumerate(self.buttons):            
            if num == self.npointer:
                button.text = 'x ' + self.legends[num]                
            else:
                button.text = self.legends[num]              
                
            button.draw()
            
    def draw_submenu(self):
        pass
       
            
            