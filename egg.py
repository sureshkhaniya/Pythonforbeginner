
import pygame

class Egg:
    
    def __int_(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        
    def draw(self, surface):
        """ draw the egg on surface"""
        pygame.Rect(self._x, self._y, self._size, self._size)
        pygame.draw.ellipse(surface, (255, 235, 10))
        
    
        
    
        
    