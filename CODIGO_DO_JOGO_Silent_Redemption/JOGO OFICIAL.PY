import pygame



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
velocidade_pulo_inicial = -11

TEMPO_SPAWN_INIMIGO = 3000  # isso é 3 segundossssssssssssss
ultimo_spawn = 0




VELOCIDADE_PROJETIL = 12        
TEMPO_COOLDOWN_MS = 500        
ultimo_tiro_tempo = 0  















START, PLAYING, PAUSE, GAMEOVER, VITORIA = "start", "playing", "pause", "gameover", "vitoria"
estado_jogo = START

fase_atual = 1



musica_de_fundo1=pygame.mixer.music.load("Projeto-jogo2025-main/SONS/musica_de_fundo1.mp3")
pygame.mixer.music.play(-1)

barulho_pulo=pygame.mixer.Sound('Projeto-jogo2025-main/SONS/som de pulo.wav')
bossAtacando = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/boss atacando.wav')
feitico_som = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/fogo.wav')
gameuver = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/gameuver.wav')
inimigoDano = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/inimigoDano.wav')
caminhando = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/caminhando.wav')
suspense = pygame.mixer.Sound('Projeto-jogo2025-main/SONS/suspense(chefao).wav')

tela_start = pygame.image.load("Projeto-jogo2025-main/imagens/TELA DE START.jpg").convert()
tela_start = pygame.transform.scale(tela_start, (largura_tela, altura_tela))


tela_vitoria = pygame.image.load("Projeto-jogo2025-main/imagens/telaDeViquitorii.jpg").convert()
tela_vitoria = pygame.transform.scale(tela_vitoria, (largura_tela, altura_tela))


tela_pause =  pygame.image.load("Projeto-jogo2025-main/imagens/jogo pausado oficial1.png").convert()
tela_pause = pygame.transform.scale(tela_pause, (largura_tela, altura_tela))



tela_game_over =  pygame.image.load("Projeto-jogo2025-main/imagens/game_over.jpg").convert()
tela_game_over = pygame.transform.scale(tela_game_over, (largura_tela, altura_tela))


telaDeViqutorii =  pygame.image.load("Projeto-jogo2025-main/imagens/telaDeViquitorii.jpg").convert()
telaDeViqutorii = pygame.transform.scale(telaDeViqutorii, (largura_tela, altura_tela))


Imagem_de_fundo= pygame.image.load('Projeto-jogo2025-main/imagens/floresta_do_jogo.png').convert()
Imagem_de_fundo=pygame.transform.scale(Imagem_de_fundo,(largura_tela,altura_tela))


Imagem_de_fundo2 = pygame.image.load("Projeto-jogo2025-main/imagens/sala2.jpeg").convert()  
Imagem_de_fundo2 = pygame.transform.scale(Imagem_de_fundo2, (largura_tela, altura_tela))


Imagem_de_fundo3 = pygame.image.load("Projeto-jogo2025-main/imagens/sala3.jpeg").convert()  
Imagem_de_fundo3 = pygame.transform.scale(Imagem_de_fundo3, (largura_tela, altura_tela))

Imagem_de_fundo4 = pygame.image.load("Projeto-jogo2025-main/imagens/fase 4.jpg").convert()  
Imagem_de_fundo4 = pygame.transform.scale(Imagem_de_fundo4, (largura_tela, altura_tela))




coracao_cheio = pygame.image.load("Projeto-jogo2025-main/imagens/coração cheio.png").convert_alpha()
coracao_vazio = pygame.image.load("Projeto-jogo2025-main/imagens/coração vazio.png").convert_alpha()

coracao_cheio = pygame.transform.scale(coracao_cheio, (32, 32))
coracao_vazio = pygame.transform.scale(coracao_vazio, (32, 32))














clock = pygame.time.Clock()




class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.tempo_ultimo_dano = 0
        self.cooldown_dano = 1000 #SÓ PREDE(agr q eu percebi que escrevi errado, vou deixar assim msm ദ്ദി◝ ⩊ ◜.ᐟ) LEVAR DANO A CADA 1 SEGUNDO.... que vergonhoso véi

        self.sprites=[]

        self.sprit_pulo=[]

        self.sprit_pulo.append(pygame.image.load('Projeto-jogo2025-main/imagens/pulando.png'))
        self.sprit_pulo.append(pygame.image.load('Projeto-jogo2025-main/imagens/pulando.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira1_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira2_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira3_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira4_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira5_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira6_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira7_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira8_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira9_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira10_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira11_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira12_direita.png'))
        self.sprites.append(pygame.image.load('Projeto-jogo2025-main/imagens/Freira13_direita.png'))
        
        
        
        self.atual=0

        self.Atual=0

        self.image=self.sprit_pulo[self.Atual]
        self.image=pygame.transform.scale(self.image,(24*3,32*3))


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
        self.pulo=False

        self.facing_right = True

        self.vida_maxima = 5
        self.vida_atual = 5













        

        

  


    def update(self):
        
        if self.animar==True:
            self.atual=self.atual + 0.09
            if self.atual>=len(self.sprites):
              self.atual = 0
              self.animar=True
            self.image = self.sprites[int(self.atual)]
            self.image=pygame.transform.scale(self.image,(24*3,32*3))
            
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)

        
        
        
        
        
        if  self.atacando==True :
             self.atual_ataque+=self.atual_ataque + 0.02
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

        if self.rect.bottom >= 626:
            self.rect.bottom = 626
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
            self.animar = True
            self.pulo=False
    
    def pular(self):
        self.pulo=True
        if self.no_chao :
            self.velocidade_y = velocidade_pulo_inicial
            self.no_chao = False


     
            

    def atacar(self):
        self.atacando=True



class Projetil(pygame.sprite.Sprite):
    def __init__(self, x, y, direcao_direita=True):
        super().__init__()


        self.image = pygame.image.load('Projeto-jogo2025-main/imagens/ATQ.png').convert_alpha()
        

        self.image = pygame.transform.scale(self.image, (60, 34))
        if direcao_direita:
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        if direcao_direita:
         self.vel_x = VELOCIDADE_PROJETIL
        else:
         self.vel_x = -VELOCIDADE_PROJETIL
         

    
    def update(self):
        self.rect.x += self.vel_x
        if self.rect.right < 0 or self.rect.left > largura_tela:
            self.kill()

def atirar(personagem):
    global ultimo_tiro_tempo
    agora = pygame.time.get_ticks()

    if agora - ultimo_tiro_tempo < TEMPO_COOLDOWN_MS:
        return

    ultimo_tiro_tempo = agora

    offset_x = 20 if personagem.facing_right else -20
    x_spawn = personagem.rect.centerx + offset_x
    y_spawn = personagem.rect.centery - 10

    p = Projetil(x_spawn, y_spawn, direcao_direita=personagem.facing_right)
    projeteis.add(p)

    feitico_som.play()


def desenhar_vida(tela, vida_atual, vida_maxima):
    x_inicial = 20
    y_inicial = 20

    for i in range(vida_maxima):
        if i < vida_atual:
            tela.blit(coracao_cheio, (x_inicial + i * 36, y_inicial))
        else:
            tela.blit(coracao_vazio, (x_inicial + i * 36, y_inicial))





class Inimigo(pygame.sprite.Sprite):
    def __init__(self, imagem, velocidade):
        super().__init__()
        self.image = pygame.image.load(imagem).convert_alpha()
        self.image = pygame.transform.scale(self.image, (60, 80))
        self.rect = self.image.get_rect()
        self.rect.x = largura_tela
        self.rect.y = altura_tela - 145
        self.velocidade = velocidade


        

    

    def update(self):
        self.rect.x -= self.velocidade
        if self.rect.right < 0:
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.spriteDaMao = []
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada1.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada2.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada3.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada4.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada5.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada6.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada7.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada8.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada9.png"))
        self.spriteDaMao.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada10.png"))
        
        self.spritesDoBoss = []
        self.spritesDoBoss.append(pygame.image.load("Projeto-jogo2025-main/imagens/Pecado_da_Ira1.png"))
        self.spritesDoBoss.append(pygame.image.load("Projeto-jogo2025-main/imagens/Pecado_da_Ira2.png"))
        self.spritesDoBoss.append(pygame.image.load("Projeto-jogo2025-main/imagens/Pecado_da_Ira3.png"))
        self.spritesDoBoss.append(pygame.image.load("Projeto-jogo2025-main/imagens/Pecado_da_Ira4.png"))

        
        self.sprite_ataque = []
        self.sprite_ataque.append(pygame.image.load("Projeto-jogo2025-main/imagens/boss_atacando1.png"))
        self.sprite_ataque.append(pygame.image.load("Projeto-jogo2025-main/imagens/boss_atacando2.png"))
        self.sprite_ataque.append(pygame.image.load("Projeto-jogo2025-main/imagens/boss_atacando3.png"))
        self.sprite_ataque.append(pygame.image.load("Projeto-jogo2025-main/imagens/boss_atacando4.png"))

        self.atualDaMao = 0
        self.image = self.spriteDaMao[self.atualDaMao]
        self.image = pygame.transform.scale(self.image, (150, 200))

        self.atual = 0
        self.image = self.spritesDoBoss[self.atual]
        self.image = pygame.transform.scale(self.image, (150, 200))

        self.ataque = 0
        self.image = self.sprite_ataque[self.ataque]
        self.image = pygame.transform.scale(self.image, (150, 200))

        self.rect = self.image.get_rect()
        self.rect.topleft = (xDoBoss_inicial, yDoBoss_inicial)

        self.velocidade_x = -2
        self.velocidade_y = 0

        self.animar = True
        self.atacando = False
        self.facing_right = True
        self.tempo_ultimo_ataque = 0
        self.cooldown_ataque = 4500
        self.atual_ataque = 0
        self.mao_chamada = False
        self.vida = 18

    def update(self):

        if self.atacando:
            self.atual_ataque += 0.08
            if self.atual_ataque >= len(self.sprite_ataque):
                self.atual_ataque = 0
                self.atacando = False
                self.mao_chamada = False
                self.maozada() 

            self.image = self.sprite_ataque[int(self.atual_ataque)]
        else:
            self.atual += 0.08
            if self.atual >= len(self.spritesDoBoss):
                self.atual = 0

            self.image = self.spritesDoBoss[int(self.atual)]

        self.image = pygame.transform.scale(self.image, (150, 200))

        if self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect.x += self.velocidade_x

        if self.rect.left <= 0 or self.rect.right >= largura_tela:
            self.velocidade_x *= -1
            self.facing_right = not self.facing_right

        x = self.rect.centerx

        if x < largura_tela * 0.66:
            self.atacar()

        elif x > largura_tela * 0.66:
            self.atacar()

    def atacar(self):
        agora = pygame.time.get_ticks()

        if agora - self.tempo_ultimo_ataque >= self.cooldown_ataque:
            self.atacando = True
            self.atual_ataque = 0
            self.tempo_ultimo_ataque = agora


    def maozada(self):
        x_alvo = personagem.rect.centerx
        mao = MaoDoCeu(x_alvo)
        mao_do_ceu.add(mao)

class MaoDoCeu(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()

        self.sprites = []
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada1.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada2.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada3.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada4.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada5.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada6.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada7.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada8.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada9.png"))
        self.sprites.append(pygame.image.load("Projeto-jogo2025-main/imagens/maozada10.png"))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.rect = self.image.get_rect()
    
        self.rect.midtop = (x, -200)

        self.velocidade_y = 8
        self.no_chao = False
        self.facing_right = True

    def update(self):
        if not self.no_chao:
            self.rect.y += self.velocidade_y

            self.atual += 0.1
            if self.atual >= len(self.sprites):
                self.atual = len(self.sprites) - 1

            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (330, 300))
            self.rect = self.image.get_rect(midtop=self.rect.midtop)

            if self.rect.bottom >= altura_tela:
                self.rect.bottom = altura_tela
                self.no_chao = True
                self.kill()
            if self.rect.centerx >= largura_tela / 2:
                self.image = pygame.transform.flip(self.image, True, False)
            
        




x_inicial = 230
y_inicial = 530
xDoBoss_inicial = 450
yDoBoss_inicial = 426


    

       
mao_do_ceu = pygame.sprite.Group()
todas_as_sprites = pygame.sprite.Group()
projeteis = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
boss = pygame.sprite.Group()
personagem = Personagem()
todasAsSpritesDoBoss = pygame.sprite.Group()
todas_as_sprites.add(personagem)
boss_criado = False
boss_derrotado = False
suspense_tocada = False






        



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
                musica_de_fundo=pygame.mixer.music.load("Projeto-jogo2025-main/SONS/musica de fundo.mp3")
                pygame.mixer.music.play(-1)

            elif estado_jogo == PLAYING and event.key == pygame.K_p:
                estado_jogo = PAUSE
                musica_de_fundo2=pygame.mixer.music.load("Projeto-jogo2025-main/SONS/musica de fundo2.mp3")
                pygame.mixer.music.play(-1)
            

            elif estado_jogo == PAUSE and event.key == pygame.K_p:
                estado_jogo = START
                musica_de_fundo=pygame.mixer.music.load("Projeto-jogo2025-main/SONS/musica de fundo.mp3")
                pygame.mixer.music.play(-1)


            elif estado_jogo == GAMEOVER and event.key == pygame.K_RETURN:
                boss_criado = False
                boss_derrotado = False
                suspense_tocada = False
                todasAsSpritesDoBoss.empty()
                estado_jogo = START
                fase_atual = 1

                personagem.rect.topleft = (x_inicial, y_inicial)
                personagem.vida_atual = personagem.vida_maxima
                personagem.velocidade_x = 0
                personagem.velocidade_y = 0

                inimigos.empty()
                projeteis.empty()
                todas_as_sprites.empty()
                todas_as_sprites.add(personagem)

                pygame.mixer.music.load("Projeto-jogo2025-main/SONS/musica_de_fundo1.mp3")
                pygame.mixer.music.play(-1)
            
            
            if estado_jogo == PLAYING:
                if event.key == pygame.K_a: 
                    personagem.Animar()
                if event.key == pygame.K_LEFT:
                    personagem.mover("esquerda")
                    caminhando.play(-1)
                if event.key == pygame.K_RIGHT:
                    personagem.mover("direita")
                    caminhando.play(-1)
                if event.key == pygame.K_SPACE:
                    if personagem.no_chao == True:
                        personagem.pular()
                        barulho_pulo.play()
                
                if event.key == pygame.K_x:
                    atirar(personagem)
                    
                

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
        if fase_atual == 4:
            tela.blit(Imagem_de_fundo4, (0, 0))
            velocidade=5

            if not boss_criado and not boss_derrotado:
                boss = Boss()
                todasAsSpritesDoBoss.add(boss)
                boss_criado = True

                
        todasAsSpritesDoBoss.update()
        todasAsSpritesDoBoss.draw(tela)
        mao_do_ceu.update()
        mao_do_ceu.draw(tela)
            
        

        tempo_atual = pygame.time.get_ticks()
        desenhar_vida(tela, personagem.vida_atual, personagem.vida_maxima)



        if fase_atual == 2:
            if tempo_atual - ultimo_spawn > TEMPO_SPAWN_INIMIGO:
               inimigo = Inimigo("Projeto-jogo2025-main/imagens/VILÃO1.png", velocidade=5)
               inimigos.add(inimigo)
               todas_as_sprites.add(inimigo)
               ultimo_spawn = tempo_atual
            


        if fase_atual == 3:
            
            if tempo_atual - ultimo_spawn > TEMPO_SPAWN_INIMIGO:
               inimigo = Inimigo("Projeto-jogo2025-main/imagens/VILÃO1.png", velocidade=5)
               inimigos.add(inimigo)
               todas_as_sprites.add(inimigo)
               ultimo_spawn = tempo_atual
        


        todas_as_sprites.update()
        projeteis.update()

        pygame.sprite.groupcollide(projeteis, inimigos, True, True)
        pygame.sprite.groupcollide(projeteis, mao_do_ceu, True, False)
        
        todas_as_sprites.draw(tela)
        projeteis.draw(tela)
        #inimigos.update()
        inimigos.draw(tela)

    

        colisoes = pygame.sprite.spritecollide(personagem, inimigos, True)
        colisoes += pygame.sprite.spritecollide(personagem, mao_do_ceu, False)
        colisoes_boss = pygame.sprite.groupcollide(todasAsSpritesDoBoss, projeteis, False, True)
        
        agora = pygame.time.get_ticks()
        
        for boss_sprite in colisoes_boss:
            boss_sprite.vida -= 1
            inimigoDano.play()
            if boss_sprite.vida <= 0:
                boss_sprite.kill()
                boss_derrotado = True
                todasAsSpritesDoBoss.empty()
                estado_jogo = VITORIA
                gameuver.play()
                caminhando.stop()
                
                

        if colisoes and agora - personagem.tempo_ultimo_dano >= personagem.cooldown_dano:
            personagem.vida_atual -= 1
            personagem.tempo_ultimo_dano = agora
        if personagem.vida_atual <= 0:
            estado_jogo = GAMEOVER
            pygame.mixer.music.stop()
            caminhando.stop()
            gameuver.play()

    
        
    
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

        if fase_atual == 2 and personagem.rect.left <=0 :
            fase_atual = 1
            personagem.rect.x = 1150
            personagem.rect.y = altura_tela - 100

        if fase_atual == 3 and personagem.rect.left <=0 :
            fase_atual = 2
            personagem.rect.x = 1150
            personagem.rect.y = altura_tela - 100
        if fase_atual == 4 and not suspense_tocada:
            pygame.mixer.music.load("Projeto-jogo2025-main/SONS/suspense(chefao).wav")
            pygame.mixer.music.play(-1)
            suspense_tocada = True



    elif estado_jogo == VITORIA:
        if boss_sprite.vida <= 0:
            boss_sprite.kill()
            boss_derrotado = True
            todasAsSpritesDoBoss.empty()

            estado_jogo = VITORIA

            pygame.mixer.music.stop()
        tela.blit(telaDeViqutorii, (0, 0))









    elif estado_jogo == GAMEOVER:
         tela.blit(tela_game_over, (0, 0))
         

       

        


        


            

    pygame.display.flip()
    clock.tick(60)
 

 







