import pygame
from pygame.sprite import AbstractGroup
import settings
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,group):
            super().__init__(group)


            self.import_assets()
            self.status = 'down'
            self.frame_index = 0

            self.image = self.animations[self.status][self.frame_index]
            self.rect = self.image.get_rect(center = pos)
            
            # player movement
            self.direction = pygame.math.Vector2()
            self.pos = pygame.math.Vector2(self.rect.center)
            self.speed = 300
    
    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
             self.direction.y = -1
             self.status = 'up'

        elif keys[pygame.K_s]:
             self.direction.y = 1
             self.status = 'down'

        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
             self.direction.x = -1
             self.status = 'left'

        elif keys[pygame.K_d]:
             self.direction.x = 1
             self.status = 'right'

        else:
            self.direction.x = 0

        print(self.direction)

    def move(self,dt):
        if (self.direction.magnitude() > 0):
            self.direction = self.direction.normalize()

        #horizontal movement
        self.pos.y+= self.direction.y * self.speed * dt
        self.pos.x+= self.direction.x * self.speed * dt
        self.rect = self.pos
        
        #vertical movement
    

    def import_assets(self):
         #all states that the player can be 
         self.animations = {'up':[],'down':[],'left':[],'right':[],
                            'right_idle':[], 'left_idle':[],'up_idle':[],
                            'down_idle':[]
                            }
        
         for animation in self.animations.keys():
            full_path = './assets/character/' + animation
            self.animations[animation] = import_folder(full_path)
         print(self.animations)

    def animate(self,dt):
         self.frame_index += 4 * dt
         if(self.frame_index >= len(self.animations[self.status])):
              self.frame_index = 0

         self.image = self.animations[self.status][int(self.frame_index)]

    def get_status(self):
         if(self.direction.magnitude() == 0):
              self.status = self.status.split('_')[0] + '_idle'
        
    def update(self,dt):
        self.controls()
        self.get_status()
        self.move(dt)
        self.animate(dt)
        



#                            'right_hoe':[],'left_hoe':[],
#                            'up_hoe':[],'down_hoe':[], 'right_axe':[],
#                            'left_axe':[],'up_axe':[], 'down_axe':[],
#                            'up_water':[],'down_water':[],'left_water':[],
#                            'right_water':[]