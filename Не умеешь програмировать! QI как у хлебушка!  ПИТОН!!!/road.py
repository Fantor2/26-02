import pygame as pg

class Road(pg.sprite.Sprite):
    def __init__(self,filename,screen, x, y):
        self.screen = screen
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
    def update(self):
        pass
    def draw(self):
        self.screen_blit(self.image,self.rect)
