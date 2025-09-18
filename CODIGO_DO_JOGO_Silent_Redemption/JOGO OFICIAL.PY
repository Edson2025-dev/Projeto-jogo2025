import pygame
import sys
import os


pygame.init()
pygame.mixer.init()


largura_tela = 1340
altura_tela = 650
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Silent Redemption")


BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)


velocidade = 4
gravidade = 0.5
velocidade_pulo_inicial = -10
ataque_personagem_principal=10


START, PLAYING, PAUSE, GAMEOVER = "start", "playing", "pause", "gameover"
estado_jogo = START

fase_atual = 1



musica_de_fundo1=pygame.mixer.music.load("SONS/musica_de_fundo1.mp3")
pygame.mixer.music.play(-1)

barulho_pulo=pygame.mixer.Sound('SONS/som de pulo.wav')





tela_start = pygame.image.load("imagens/TELA DE START.jpg").convert()
tela_start = pygame.transform.scale(tela_start, (largura_tela, altura_tela))



tela_pause =  pygame.image.load("imagens/jogo pausado oficial1.png").convert()
tela_pause = pygame.transform.scale(tela_pause, (largura_tela, altura_tela))



tela_game_over =  pygame.image.load("imagens/tela de pause 2.png").convert()
tela_game_over = pygame.transform.scale(tela_game_over, (largura_tela, altura_tela))


Imagem_de_fundo= pygame.image.load('imagens/floresta_do_jogo.png').convert()
Imagem_de_fundo=pygame.transform.scale(Imagem_de_fundo,(largura_tela,altura_tela))


Imagem_de_fundo2 = pygame.image.load("imagens/sala2.jpeg").convert()  
Imagem_de_fundo2 = pygame.transform.scale(Imagem_de_fundo2, (largura_tela, altura_tela))


Imagem_de_fundo3 = pygame.image.load("imagens/sala3.jpeg").convert()  
Imagem_de_fundo3 = pygame.transform.scale(Imagem_de_fundo3, (largura_tela, altura_tela))

Imagem_de_fundo4 = pygame.image.load("imagens/fase 4.jpg").convert()  
Imagem_de_fundo4 = pygame.transform.scale(Imagem_de_fundo4, (largura_tela, altura_tela))













clock = pygame.time.Clock()






class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        

        self.sprites=[]

        self.sprites.append(pygame.image.load('imagens/Freira1_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira2_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira3_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira4_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira5_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira6_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira7_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira8_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira9_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira10_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira11_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira12_direita.png'))
        self.sprites.append(pygame.image.load('imagens/Freira13_direita.png'))
        self.atual=0

        self.image=self.sprites[self.atual]
        self.image=pygame.transform.scale(self.image,(24*3,32*3))


        
        self.image=self.sprites[self.atual]
        self.image=pygame.transform.scale(self.image,(24*3,32*3))

        self.rect=self.image.get_rect()
        self.rect.topleft=(x_inicial,y_inicial)








 



        self.velocidade_x = 0
        self.velocidade_y = 0

        self.animar=False
        self.no_chao = True
        self.atacando=False
        self.animar_pulo=False


        self.facing_right = True
        

        

  


    def update(self):
        
        if self.animar==True:
            self.atual=self.atual + 0.22
            if self.atual>=len(self.sprites):
              self.atual = 0
              self.animar=True
            self.image = self.sprites[int(self.atual)]
            self.image=pygame.transform.scale(self.image,(24*3,32*3))

            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)

        if  self.atacando==True:
             self.atual_ataque=self.atual_ataque + 0.22
             if self.atual_ataque>=len(self.sprites_ataque):
                 self.atual_ataque = 0
                 self.atacando=True
             self.image_ataque = self.sprites_ataque[int(self.atual_ataque)]
             self.image_ataque=pygame.transform.scale(self.image_ataque,(24*3,32*3))

        

        
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
            self.facing_right = False
            
        elif direcao == "direita":
            self.velocidade_x = velocidade
            self.facing_right = True
    
    def parar(self):
        self.velocidade_x = 0
        if self.no_chao:
            self.animar = False
    
    def pular(self):

        if self.no_chao :
            self.velocidade_y = velocidade_pulo_inicial
            self.no_chao = False
            

    def atacar(self, ):
        self.atacando=True
      



x_inicial = 230
y_inicial = 530



    

       

todas_as_sprites=pygame.sprite.Group()
personagem=Personagem()
todas_as_sprites.add(personagem)



        



Relogio=pygame.time.Clock()
while True:
    Relogio.tick(35)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if estado_jogo == START and event.key == pygame.K_KP_ENTER:  
                estado_jogo = PLAYING
                musica_de_fundo=pygame.mixer.music.load("SONS/musica de fundo.mp3")
                pygame.mixer.music.play(-1)

            elif estado_jogo == PLAYING and event.key == pygame.K_p:
                estado_jogo = PAUSE
                musica_de_fundo2=pygame.mixer.music.load("SONS/musica de fundo2.mp3")
                pygame.mixer.music.play(-1)


            elif estado_jogo == PAUSE and event.key == pygame.K_p:
                estado_jogo = PLAYING
                musica_de_fundo=pygame.mixer.music.load("SONS/musica de fundo.mp3")
                pygame.mixer.music.play(-1)


            elif estado_jogo == GAMEOVER and event.key == pygame.K_RETURN:
                estado_jogo = START

            if estado_jogo == PLAYING:
                if event.key == pygame.K_a: 
                    personagem.Animar()
                if event.key == pygame.K_LEFT:
                    personagem.mover("esquerda")
                if event.key == pygame.K_RIGHT:
                    personagem.mover("direita")
                if event.key == pygame.K_SPACE:
                    personagem.pular()
                    barulho_pulo.play()
                    
                if event.key == pygame.K_z:
                    personagem.atacar()

        if event.type == pygame.KEYUP and estado_jogo == PLAYING:
            if event.key == pygame.K_LEFT and personagem.velocidade_x < 0:
                personagem.parar()
            if event.key == pygame.K_RIGHT and personagem.velocidade_x > 0:
                personagem.parar()

    

    if estado_jogo == PAUSE:
         tela.blit(tela_pause, (0, 0))

    if estado_jogo == START:
        tela.blit(tela_start, (0, 0))
       

    elif estado_jogo == PLAYING:
        if fase_atual == 1:
            tela.blit(Imagem_de_fundo, (0, 0))
        if fase_atual == 2:
            tela.blit(Imagem_de_fundo2, (0, 0))
        if fase_atual == 3:
            tela.blit(Imagem_de_fundo3, (0, 0))
        if fase_atual==4:
            tela.blit(Imagem_de_fundo4, (0, 0))

        todas_as_sprites.update()
        todas_as_sprites.draw(tela)
        

    

    
        if fase_atual == 1 and personagem.rect.right >= largura_tela:
            fase_atual = 2
            personagem.rect.x = 50
            personagem.rect.y = altura_tela - 100
        
        if fase_atual == 2 and personagem.rect.right >= largura_tela:
            fase_atual = 3
            personagem.rect.x = 50
            personagem.rect.y = altura_tela - 100
        

        if fase_atual == 3 and personagem.rect.right >= (largura_tela - 160) :
            fase_atual = 4
            personagem.rect.x = 50
            personagem.rect.y = altura_tela - 100


        if fase_atual == 2 and personagem.rect.right >= largura_tela:
            fase_atual = 1
            personagem.rect.x = 50
            personagem.rect.y = altura_tela - 100


            


    pygame.display.flip()
    clock.tick(60)

