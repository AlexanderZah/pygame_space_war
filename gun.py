import pygame

class Gun():

    def __init__(self,screen):
        """инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.centerx = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.centery = float(self.rect.centery)
        self.mright = False
        self.mleft = False
        self.mtop = False
        self.mbottom = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.centerx += 7
        elif self.mleft and self.rect.left > self.screen_rect.left:
            self.centerx -= 7
        elif self.mtop and self.rect.top > self.screen_rect.bottom - 100:
            self.centery -= 7
        elif self.mbottom and self.rect.bottom <= self.screen_rect.bottom:
            self.centery += 7

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def create_gun(self):

        self.center = self.screen_rect.centerx
