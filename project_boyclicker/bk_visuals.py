import pygame
# imagem de Setup
def setup_images():
    images_buttons = []
    images_visuals = []
    clicker_image = pygame.image.load('bk_image_df.png').convert_alpha()
    clicked_image = pygame.image.load('bk_image_clicked.png')
    scoreboard = pygame.image.load('scoreboard_01.PNG').convert_alpha()
    up_1 = pygame.image.load('Up_1.PNG').convert_alpha()
    up_2 = pygame.image.load('Up_2.png').convert_alpha()
    up_3 = pygame.image.load('Up_3.png').convert_alpha()
    up_4 = pygame.image.load('Up_4.png').convert_alpha()
    up_5 = pygame.image.load('Up_5.png').convert_alpha()
    up_6 = pygame.image.load('Up_6.png').convert_alpha()

    images_buttons.append(clicker_image)

    images_buttons.append(up_1)
    images_buttons.append(up_2)
    images_buttons.append(up_3)
    images_buttons.append(up_4)
    images_buttons.append(up_5)
    images_buttons.append(up_6)

    images_buttons.append(clicked_image)

    images_visuals.append(scoreboard)
    return images_visuals, images_buttons

def setup_fonts():
    fonte = []
    font_points = pygame.font.Font('Cookiemonster-gv11.ttf', 40)
    fonte.append(font_points)

    font_up = pygame.font.Font('Cookiemonster-gv11.ttf', 23)
    fonte.append(font_up)

    font_up_price = pygame.font.Font('Cookiemonster-gv11.ttf', 20)
    fonte.append(font_up_price)

    return fonte

def config_visuals(images):
    visuals = []
    scoreboard = images[0].get_rect()
    scoreboard.left = 30
    visuals.append(scoreboard)

    return visuals

#configurações
def config_buttons(images):
    botoes = []
    clicker = images[0].get_rect()
    clicker.top = 200
    clicker.left = 30
    botoes.append(clicker)

    up_1 = images[1].get_rect()
    up_1.top = 0
    up_1.left = 1140

    up_2 = images[2].get_rect()
    up_2.top = 145
    up_2.left = 1140

    up_3 = images[3].get_rect()
    up_3.left = 1140
    up_3.top = 290

    up_4 = images[4].get_rect()
    up_4.left = 1140
    up_4.top = 430

    up_5 = images[5].get_rect()
    up_5.left = 1140
    up_5.top = 575

    up_6 = images[6].get_rect()
    up_6.left = 1140
    up_6.top = 720

    botoes.append(up_1)
    botoes.append(up_2)
    botoes.append(up_3)
    botoes.append(up_4)
    botoes.append(up_5)
    botoes.append(up_6)

    return botoes

#Criação de objetos na tela

def draw_buttons(tela ,images, botoes):
    for image, botao in zip(images , botoes):
        tela.blit(image ,botao)

def draw_visuals(tela ,images, visuals):
    for image, visual in zip(images ,visuals ):
        tela.blit(image ,visual)

def draw_text(tela, fonte, mensagem, x, y, cor=(255, 255, 255)):

    texto_surface = fonte.render(mensagem, True, cor)
    text_rect = texto_surface.get_rect()
    text_rect.left = x
    text_rect.top = y
    tela.blit(texto_surface, text_rect)