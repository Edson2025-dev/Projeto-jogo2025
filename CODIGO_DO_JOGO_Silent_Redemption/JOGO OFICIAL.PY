import pygame
import sys


pygame.init()


largura_tela = 1340
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Silent Redemption")


BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)


velocidade = 5
gravidade = 0.5
velocidade_pulo_inicial = -10






clock = pygame.time.Clock()

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites=[]
        self.sprites.append(pygame.image.load('imagens/Freira1.png'))
        self.sprites.append(pygame.image.load('imagens/Freira2.png'))
        self.sprites.append(pygame.image.load('imagens/Freira3.png'))
        self.sprites.append(pygame.image.load('imagens/Freira4.png'))
        self.sprites.append(pygame.image.load('imagens/Freira5.png'))
        self.sprites.append(pygame.image.load('imagens/Freira6.png'))
        self.sprites.append(pygame.image.load('imagens/Freira7.png'))
        self.sprites.append(pygame.image.load('imagens/Freira8.png'))
        self.sprites.append(pygame.image.load('imagens/Freira9.png'))
        self.sprites.append(pygame.image.load('imagens/Freira10.png'))
        self.sprites.append(pygame.image.load('imagens/Freira11.png'))
        self.sprites.append(pygame.image.load('imagens/Freira12.png'))
        self.sprites.append(pygame.image.load('imagens/Freira13.png'))
        self.atual=0
        self.image=self.sprites[self.atual]
        self.image=pygame.transform.scale(self.image,(24*3,32*3))

        self.rect=self.image.get_rect()
        self.rect.topleft=(x_inicial,y_inicial)

        self.velocidade_x = 0
        self.velocidade_y = 0

        self.animar=False
        self.no_chao = True

    def update(self):
        if self.animar==True:
            self.atual=self.atual + 0.22
            if self.atual>=len(self.sprites):
              self.atual = 0
              self.animar=False
            self.image = self.sprites[int(self.atual)]
            self.image=pygame.transform.scale(self.image,(24*3,32*3))

        
        if not self.no_chao:
            self.velocidade_y += gravidade
        
        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.right > largura_tela:
            self.rect.right = largura_tela

        if self.rect.bottom >= altura_tela:
            self.rect.bottom = altura_tela
            self.velocidade_y = 0
            self.no_chao = True

    def Animar(self):
        self.animar=True
    def mover(self, direcao):
        self.animar = True
        if direcao == "esquerda":
            self.velocidade_x = -velocidade
        elif direcao == "direita":
            self.velocidade_x = velocidade
    
    def parar(self):
        self.velocidade_x = 0
        if self.no_chao:
            self.animar = False
    
    def pular(self):
        if self.no_chao:
            self.velocidade_y = velocidade_pulo_inicial
            self.no_chao = False
            self.animar = True

x_inicial = 230
y_inicial = 530



    

       

todas_as_sprites=pygame.sprite.Group()
personagem=Personagem()
todas_as_sprites.add(personagem)


        

Imagem_de_fundo= pygame.image.load('imagens/floresta_do_jogo.png').convert()
Imagem_de_fundo=pygame.transform.scale(Imagem_de_fundo,(largura_tela,altura_tela))

Relogio=pygame.time.Clock()
while True:
    Relogio.tick(35)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            personagem.Animar()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                personagem.mover("esquerda")
            if event.key == pygame.K_RIGHT:
                personagem.mover("direita")
            if event.key == pygame.K_SPACE:
                personagem.pular()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and personagem.velocidade_x < 0:
                personagem.parar()
            if event.key == pygame.K_RIGHT and personagem.velocidade_x > 0:
                personagem.parar()
            
            
   
    tela.fill(AZUL)
    tela.blit(Imagem_de_fundo,(0,0))
   

    

    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()    
    

    clock.tick(60)


