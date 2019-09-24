import glob
import os

import pygame

from .config import *


class Player(pygame.sprite.Sprite):

    def __init__(self, left, bottom, dir_images):
        pygame.sprite.Sprite.__init__(self)

        self.image1 = pygame.image.load(os.path.join(dir_images, 'Walk (1.1).png'))
        self.image2 = pygame.image.load(os.path.join(dir_images, 'Walk (2.2).png'))

        self.listWalk = [self.image1, self.image2]
        self.posImage = 0

        self.imagesWalk = self.listWalk[self.posImage]

        # self.image = pygame.Surface((40, 40))
        # self.image.fill(BLUE)

        self.rect = self.imagesWalk.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.pos_y = self.rect.bottom
        self.vel_y = 0

        self.can_jump = False

        self.playing = True

    def collide_with(self, sprites):
        objects = pygame.sprite.spritecollide(self, sprites, False)
        if objects:
            return objects[0]

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.rect_top)

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True

    def validate_platform(self, platform):
        result = pygame.sprite.collide_rect(self, platform)
        if result:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

    def jump(self):
        if self.can_jump:
            self.vel_y = -15
            self.can_jump = False

    def update_pos(self):
        self.vel_y += PLAYER_GRAV
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV

    def update(self):
        if self.playing:
            self.update_pos()

            self.rect.bottom = self.pos_y

    def stop(self):
        self.playing = False
