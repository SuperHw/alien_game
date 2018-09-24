#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pygame
from src.alien_invasion.settings import Settings
from src.alien_invasion.ship import Ship
import src.alien_invasion.game_functions as gf


def run_game():
    """
    初始化游戏，并创建一个屏幕对象
    :return:
    """
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings, screen)

    #开始游戏主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


run_game()
