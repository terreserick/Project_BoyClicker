import math

def config_sis_vars():
    score = 0
    clicks = 0
    click_boost = 0
    click_mult = 1
    auto_value = 0
    auto_mult = 1
    click_expo = 1
    auto_expo = 1
    last_auto = 0
    timer = 1000

    return score,clicks,click_boost,click_mult, auto_value, auto_mult, click_expo ,auto_expo, last_auto, timer

def valores_base():
    valor_up_1 = 50
    valor_up_2 = 150
    valor_up_3 = 500
    valor_up_4 = 1500
    valor_up_5 = 10000
    valor_up_6 = 100000

    return valor_up_1, valor_up_2, valor_up_3, valor_up_4, valor_up_5, valor_up_6

def ajust_scale(base,r,n,i):
    price = math.floor(base * r ** (n * i))
    return price


