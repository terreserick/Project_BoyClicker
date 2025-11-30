import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from math import floor
import pygame, project_boyclicker.bk_events_screen, project_boyclicker.bk_visuals, project_boyclicker.bk_gmvars
from project_boyclicker.bk_gmvars import ajust_scale, valores_base
from project_boyclicker.bk_visuals import draw_buttons

#iniciação do pygame
pygame.init()

#variaveis do jogo
pontos, clickes, click_boost,click_mult,auto_value,auto_mult,click_expo,auto_expo, ultimo_intervalo, tempo = project_boyclicker.bk_gmvars.config_sis_vars()

# vars de custo base
up_1, up_2, up_3, up_4, up_5, up_6 = valores_base()

# vars de custo ajustavel
valor_up_1,valor_up_2, valor_up_3,valor_up_4 ,valor_up_5, valor_up_6 = up_1 ,up_2,up_3, up_4, up_5, up_6

# vars de quant de upgrade (Só existem por causa dos mults)
quant_mult_click, quant_expo_click, quant_mult_clicker, quant_expo_clicker = 0, 0, 0 ,0


# Setups
tela = project_boyclicker.bk_events_screen.tela_settings()
timer = pygame.time.Clock()
imagens_visual, imagens_botoes = project_boyclicker.bk_visuals.setup_images()

# configs
botoes = project_boyclicker.bk_visuals.config_buttons(imagens_botoes)
visuais = project_boyclicker.bk_visuals.config_visuals(imagens_visual)
fontes = project_boyclicker.bk_visuals.setup_fonts()

rodando = True
clicked = False

# setup do nome da tela
pygame.display.set_caption('BoyClicker')
pygame.display.set_icon(imagens_botoes[0])

# click Logic

while rodando:
    tempo_atual = pygame.time.get_ticks()

    if tempo_atual - ultimo_intervalo >= tempo:
        if auto_value > 0:
            pontos_auto= floor((auto_value * auto_mult) ** auto_expo)
            pontos += pontos_auto

        ultimo_intervalo = tempo_atual

    valor_click = floor(((1 + click_boost) * click_mult) ** click_expo)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = event.pos

            for i , botao in enumerate(botoes):

                if botao.collidepoint(click_pos):
                    if i == 0:
                        clicked = True
                        pontos += valor_click
                        clickes += 1

                    if i == 1: #upgrade 1
                        if pontos >= valor_up_1:
                            pontos -= valor_up_1
                            click_boost += 1
                            valor_up_1 = ajust_scale(up_1, 1.1, click_boost, 1)

                    if i == 2: #upgrade 2
                        if pontos >= valor_up_2:
                            pontos -= valor_up_2
                            quant_mult_click += 1
                            click_mult += 0.3
                            valor_up_2 = ajust_scale(up_2, 1.2,quant_mult_click , 1.2)

                    if i == 3: #upgrade 3
                        if pontos >= valor_up_3:
                            pontos -= valor_up_3
                            auto_value += 1
                            valor_up_3 = ajust_scale(up_3, 1.3, auto_value, 1.2)

                    if i == 4: #upgrade 4
                        if pontos >= valor_up_4:
                            pontos -= valor_up_4
                            quant_mult_clicker += 1
                            auto_mult += 0.2
                            valor_up_4 = ajust_scale(up_4, 1.4,quant_mult_clicker , 1.4)

                    if i == 5: #upgrade 5
                        if pontos >= valor_up_5:
                            pontos -= valor_up_5
                            quant_expo_click += 1
                            click_expo += 0.01
                            valor_up_5 = ajust_scale(up_5, 1.5, quant_expo_click, 1.8)

                    if i == 6: #upgrade 6
                        if pontos >= valor_up_6:
                            pontos -= valor_up_6
                            quant_expo_clicker += 1
                            auto_expo += 0.01
                            valor_up_6 = ajust_scale(up_6, 1.6,quant_expo_clicker , 1.8)
                    break
        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

    repo_images = imagens_botoes[:]

    if clicked:
        repo_images[0] = imagens_botoes[-1]

    tela.fill((255,255,255))

    draw_buttons(tela, repo_images, botoes)
    project_boyclicker.bk_visuals.draw_visuals(tela,imagens_visual, visuais)
    project_boyclicker.bk_visuals.draw_text(tela, fontes[0], f'Pontos {pontos}', 140, 50, (110, 239, 242))
    # 1
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'Clicker +1' , 1300, 40, (0,0,0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_1}', 1310, 60 , (0,0,0))
    # 2
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'Clicker Mult +0.3', 1250, 185, (0, 0, 0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_2}', 1275, 205, (0, 0, 0))
    # 3
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'AutoClicker +1', 1275, 330, (0, 0, 0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_3}', 1300, 350  , (0, 0, 0))
    # 4
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'AutoClicker Mult +0.2', 1250, 470, (0, 0, 0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_4}', 1275, 490, (0, 0, 0))
    # 5
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'Clicker expo +0.01', 1275, 615, (0, 0, 0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_5}', 1275, 635, (0, 0, 0))
    # 6
    project_boyclicker.bk_visuals.draw_text(tela, fontes[1], 'autoClicker expo +0.01', 1275, 760, (0, 0, 0))
    project_boyclicker.bk_visuals.draw_text(tela, fontes[2], f' Valor {valor_up_6}', 1275, 780, (0, 0, 0))

    print(valor_click, auto_value)

    pygame.display.flip()
    timer.tick(60)
pygame.quit()
