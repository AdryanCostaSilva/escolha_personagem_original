import pygame
import sys

# Iniciando tela
pygame.init()

# Configurando tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("JOGO BÃO")

# Fonte da letra
fonte = pygame.font.Font('ARCADECLASSIC.TTF', 36)
font2 = pygame.font.Font("ARCADECLASSIC.TTF", 90)

# Imagem de fundo da tela
background_imagem = pygame.image.load('puc.jpg')

# Defina as CORES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
VERMELHO = (108, 34, 34)

# Largura e altura dos botões
botao_largura, botao_altura = 120, 120

# Carregando a foto
personagem_adryan = pygame.image.load('adryan.jpg').convert_alpha()
personagem_gustavo = pygame.image.load('gustavo.png').convert_alpha()
personagem_kelvin = pygame.image.load('kelvin.jpg').convert_alpha()
personagem_caio = pygame.image.load('zeca.jpeg').convert_alpha()

# Lista dos personagens
personagens = [personagem_adryan, personagem_gustavo, personagem_kelvin, personagem_caio]

# Classe botão P1 e P2
class Button():
    def __init__(self, x, y, imagem):
        self.imagem = imagem
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x, y)
        self.hovered_p1 = False
        self.hovered_p2 = False

    def draw(self, selected_p1, selected_p2):
        # Desenhando borda azul se estiver selecionado ou hovered (para P1)
        if self.hovered_p1 or selected_p1:
            pygame.draw.rect(tela, (0, 0, 255), self.rect.inflate(8, 8))
            texto_surface = fonte.render("P1", True, (0, 0, 255))
            texto_rect = texto_surface.get_rect(topright=(self.rect.right - 5, self.rect.top + 5))
            tela.blit(texto_surface, texto_rect)
        # Desenhando borda vermelha se estiver selecionado ou hovered (para P2)
        if self.hovered_p2 or selected_p2:
            pygame.draw.rect(tela, (255, 0, 0), self.rect.inflate(8, 8))
            texto_surface = fonte.render("P2", True, (255, 0, 0))
            texto_rect = texto_surface.get_rect(topright=(self.rect.right - 5, self.rect.top + 5))
            tela.blit(texto_surface, texto_rect)

        # Desenhando o botão na tela
        tela.blit(self.imagem, (self.rect.x, self.rect.y))

    def update_hover(self, mouse_pos):
        self.hovered_p1 = self.rect.collidepoint(mouse_pos) # Para P1
        self.hovered_p2 = self.rect.collidepoint(mouse_pos) # Para P2

# Calculando a coordenada x
espacamento_horizontal = 20
total_largura_botoes = botao_largura * len(personagens) + espacamento_horizontal * (len(personagens) - 1)
x_inicial = (largura - total_largura_botoes) // 2

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    tela.blit(text_surface, text_rect)

# Criando botões
botoes = []
x = x_inicial
for i, personagem in enumerate(personagens):
    personagem_redimensionada = pygame.transform.scale(personagem, (botao_largura, botao_altura))
    botao = Button(x, 250, personagem_redimensionada)
    botoes.append(botao)
    x += botao_largura + espacamento_horizontal

selected_index_p1 = 0
selected_index_p2 = 0

# Loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            for botao in botoes:
                botao.update_hover(event.pos)
        elif event.type == pygame.KEYDOWN:
            # Teclas de jogador 1 (P1)
            if event.key == pygame.K_a:
                selected_index_p1 = (selected_index_p1 - 1) % len(botoes)
            elif event.key == pygame.K_d:
                selected_index_p1 = (selected_index_p1 + 1) % len(botoes)
            # Teclas de jogador 2 (P2)
            elif event.key == pygame.K_LEFT:
                selected_index_p2 = (selected_index_p2 - 1) % len(botoes)
            elif event.key == pygame.K_RIGHT:
                selected_index_p2 = (selected_index_p2 + 1) % len(botoes)
            elif event.key == pygame.K_RETURN:
                print("P1 selecionou:", selected_index_p1)
                print("P2 selecionou:", selected_index_p2)

    tela.blit(background_imagem, (0, 0))
    draw_text("SELECIONE", font2, BLACK, largura // 2 + 4, 100)
    draw_text("SELECIONE", font2, VERMELHO, largura // 2, 103)
    for i, botao in enumerate(botoes):
        botao.draw(i == selected_index_p1, i == selected_index_p2)
    pygame.display.update()