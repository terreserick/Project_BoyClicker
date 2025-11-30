import pygame

def tela_settings():
    """
    Faz a configuração da tela quando o jogo abre

    :return: função que define o tamnaho da tela
    """
    info_tela = pygame.display.Info()
    largura = info_tela.current_w
    altura = info_tela.current_h
    return pygame.display.set_mode((largura,altura))



 # def activate_auto(pontos, interval):
