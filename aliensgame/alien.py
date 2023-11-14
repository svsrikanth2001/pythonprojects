import pygame
from pygame.sprite import  Sprite
class Alien(Sprite):
    def __init__(self,aigame):
        super().__init__()
        self.screen = aigame.screen
        self.image  = pygame.image.load('aliensgame\images\R.bmp')
        self.rect = self.image.get_rect()


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.settings_game = aigame.settings_game

    def update(self):
        self.x  += self.settings_game.alien_speed * self.settings_game.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        self.screen_rect = self.screen.get_rect()
        return (self.rect.right >= self.screen_rect.right) or (self.rect.left <= self.screen_rect.left)






