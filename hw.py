import pygame
import random

pygame.init()
surf_color="yellow"
color="green"

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,width,height))
        self.rect=self.image.get_rect()
    def moveRight(self,pix):
        self.rect.x += pix
    def moveLeft(self,pix):
        self.rect.x -= pix
    def moveForward(self,speed):
        self.rect.y += speed * speed/10
    def moveBack(self,speed):
        self.rect.y -= speed * speed/10

pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("SPRITE EXAMPLE-2")
all_sprites_list=pygame.sprite.Group()

sp1=Sprite(color, 50,30)
sp1.rect.x=random.randint(10,580)
sp1.rect.y=random.randint(10,580)
all_sprites_list.add(sp1)

sp2=Sprite("red", 50,30)
sp2.rect.x=random.randint(10,580)
sp2.rect.y=random.randint(10,580)
all_sprites_list.add(sp2)
rad=20
exit=True
clock=pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_DOWN]:
        sp1.moveForward(5)
    if keys[pygame.K_UP]:
        sp1.moveBack(5)
    
    all_sprites_list.update()
    screen.fill(surf_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    
    if sp1.rect.colliderect(sp2.rect):
        all_sprites_list.remove(sp2)

    

    pygame.display.update() 
    clock.tick(60)

pygame.quit()
