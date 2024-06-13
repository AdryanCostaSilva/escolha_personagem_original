import pygame
import sys

#iniciando tela
pygame.init()


#configurando tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")

#Fonte da letra
fonte = pygame.font.Font('ARCADECLASSIC.TTF', 36)
font2 = pygame.font.Font("ARCADECLASSIC.TTF", 90)

#imagem de fundo da tela
background_imagem = pygame.image.load('puc.jpg').convert()
background_imagem = pygame.transform.scale(background_imagem, (largura, altura))

# Defina as CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO = (108, 34, 34)

#Largura e altura dos botões
botao_largura, botao_altura = 120, 120

#Carregando a foto
personagem_adryan = pygame.image.load('adryan.jpg').convert_alpha()
personagem_gustavo = pygame.image.load('gustavo.png').convert_alpha()
personagem_kelvin = pygame.image.load('kelvin.jpg').convert_alpha()
personagem_caio = pygame.image.load('zeca.jpeg').convert_alpha()

#Lista dos personagens
personagens = [personagem_adryan, personagem_gustavo, personagem_kelvin, personagem_caio]

#classe botão P1
class Button():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered = False
    def draw(self, selected):
        # Desenhando borda azul se estiver selecionado ou hovered
        if self.hovered or selected:
            pygame.draw.rect(tela, (0, 0, 255), self.rect.inflate(8, 8))
        else:
            pygame.draw.rect(tela, (0, 0, 0), self.rect.inflate(8, 8))
        # Desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))
        if selected:
            texto_surface = fonte.render("P1", True, (0, 0, 255))
            texto_rect = texto_surface.get_rect(topright=(self.rect.right - 5, self.rect.top + 5))
            tela.blit(texto_surface, texto_rect)
#Calculando a coordenada x
espacamento_horizontal = 20
total_largura_botoes = botao_largura * len(personagens) + espacamento_horizontal * (len(personagens) - 1)
x_inicial = (largura - total_largura_botoes) // 2

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)

#Classe botão  P2
class ButtonPlayer2():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered = False

    def draw(self, selected):
        # Desenhando borda vermelha se estiver selecionado ou hovered
        if self.hovered or selected:
            pygame.draw.rect(tela, (255, 0, 0), self.rect.inflate(8, 8))
        else:
            pygame.draw.rect(tela, (0, 0, 0), self.rect.inflate(8, 8))
        # Desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))

        # Escrevendo "P2" no canto superior direito quando selecionado
        if selected:
            texto_surface = fonte.render("P2", True, (255, 0, 0))
            texto_rect = texto_surface.get_rect(topright=(self.rect.right - 5, self.rect.top + 5))
            tela.blit(texto_surface, texto_rect)

#Criando botões player 1
botoes_player1 = []
x = x_inicial
for i, personagem in enumerate(personagens):
    personagem_redimensionada = pygame.transform.scale(personagem, (botao_largura, botao_altura))
    botao = Button(x, 200, personagem_redimensionada)
    botoes_player1.append(botao)
    x += botao_largura + espacamento_horizontal

#Criando botões player 2
botoes_player2 = []
x = x_inicial
for i, personagem in enumerate(personagens):
    personagem_redimensionada = pygame.transform.scale(personagem, (botao_largura, botao_altura))
    botao = ButtonPlayer2(x, 300, personagem_redimensionada)
    botoes_player2.append(botao)
    x += botao_largura + espacamento_horizontal

selected_index_p1 = 0
selected_index_p2 = 0

#loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Teclas de jogador 1
            if event.key == pygame.K_a:
                selected_index_p1 = (selected_index_p1 - 1) % len(botoes_player1)
            elif event.key == pygame.K_d:
                selected_index_p1 = (selected_index_p1 + 1) % len(botoes_player1)
            #Teclas de jogador 2
            elif event.key == pygame.K_LEFT:
                selected_index_p2 = (selected_index_p2 - 1) % len(botoes_player2)
            elif event.key == pygame.K_RIGHT:
                selected_index_p2 = (selected_index_p2 + 1) % len(botoes_player2)
            elif event.key == pygame.K_RETURN:
                #P1
                if selected_index_p1 == 0:
                    print("Adryan selecionado!")
                elif selected_index_p1 == 1:
                    print("Gustavo selecionado!")
                elif selected_index_p1 == 2:
                    print("Kelvin selecionado!")
                elif selected_index_p1 == 3:
                    print("Caio selecionado!")
                #P2
                if selected_index_p2 == 0:
                    print("Adryan selecionado para o P2!")
                elif selected_index_p2 == 1:
                    print("Gustavo selecionado para o P2!")
                elif selected_index_p2 == 2:
                    print("Kelvin selecionado para o P2!")
                elif selected_index_p2 == 3:
                    print("Caio selecionado para o P2!")
    tela.blit(background_imagem, (0, 0))
    draw_text("SELECIONE", font2, BLACK, largura // 2 + 4, 100)
    draw_text("SELECIONE", font2, VERMELHO, largura // 2, 103)
    for i, botao in enumerate(botoes_player1):
        botao.draw(i == selected_index_p1)
    for i, botao in enumerate(botoes_player2):
        botao.draw(i == selected_index_p2)
    pygame.display.update()
