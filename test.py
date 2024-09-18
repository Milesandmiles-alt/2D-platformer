import pygame

class CameraWrapper:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rect = pygame.Rect(0, 0, 1, 1)
        
    def update(self):
        self.rect = self.a.union(self.b)

    def get_rect(self):
        return self.rect
    
a = pygame.Rect(32, 32, 32, 32)
b = pygame.Rect(64, 32, 32, 32)

wrap = CameraWrapper(a, b)

wrap.update()
new = wrap.get_rect()

print(new)