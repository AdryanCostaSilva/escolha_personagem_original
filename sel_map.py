import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definição das cores
WHITE = (255, 255, 255)

# Configurações da janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Seleção de Mapa no Pygame")

# Classe para representar botões com imagens
class ImageButton:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Função principal de seleção de mapa
def select_map():
    map_selected = None
    while not map_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in map_buttons:
                    if button.rect.collidepoint(mouse_pos):
                        map_selected = button.text
                        break

        screen.fill(WHITE)
        for button in map_buttons:
            button.draw(screen)

        pygame.display.flip()

    return map_selected

# Criando botões (imagens) para seleção de mapa
map_buttons = [
    ImageButton(WIDTH // 2, HEIGHT // 2 - 100, "adryan.jpg"),  # Substitua "map1.png" pelo caminho da sua imagem
    ImageButton(WIDTH // 2, HEIGHT // 2, "gustavo.png"),        # Substitua "map2.png" pelo caminho da sua imagem
    ImageButton(WIDTH // 2, HEIGHT // 2 + 100, "kelvin.jpg")   # Substitua "map3.png" pelo caminho da sua imagem
]

# Selecionando o mapa
selected_map = select_map()
print("Mapa selecionado:", selected_map)

# Aqui você pode carregar e renderizar o mapa selecionado
# Exemplo:
# if selected_map == "Mapa 1":
#     load_and_render_map("mapa1.png")
# elif selected_map == "Mapa 2":
#     load_and_render_map("mapa2.png")
# elif selected_map == "Mapa 3":
#     load_and_render_map("mapa3.png")

pygame.quit()
sys.exit()
