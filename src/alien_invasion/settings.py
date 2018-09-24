#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Settings:
    """存储游戏相关的所有设置"""

    def __init__(self):
        """初始化游戏的设置"""

        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #飞船速度设置
        self.ship_speed_factor = 1.5

