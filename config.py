#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/28/2022 2:25 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : config
# ---------------------
import yaml
from PySide6.QtCore import QRect


class Config:

    config_filename = 'config.yaml'

    def __init__(self):
        with open(self.config_filename) as f:
            self.config = yaml.safe_load(f)

    def _get_root(self):
        return self.config['config']

    def save(self):
        with open(self.config_filename, 'w') as f:
            yaml.safe_dump(self.config, f)

    def set_auto_scroll(self, v):
        self._get_root()['auto_scroll'] = v

    def set_max_rows(self, v):
        self._get_root()['max_rows'] = v

    def set_uart_settings(self, name, baud, data, parity, stop):
        tmp = self._get_root()['uart']
        tmp['name'] = name
        tmp['baud'] = baud
        tmp['data'] = data
        tmp['parity'] = parity
        tmp['stop'] = stop

    def set_rect(self, rect):
        tmp = self._get_root()['rect']
        tmp['x'] = rect.x()
        tmp['y'] = rect.y()
        tmp['width'] = rect.width()
        tmp['height'] = rect.height()

    def get_auto_scroll(self):
        return self._get_root()['auto_scroll']

    def get_max_rows(self):
        return self._get_root()['max_rows']

    def get_uart_settings(self):
        tmp = self._get_root()['uart']
        return tmp['name'], int(tmp['baud']), int(tmp['data']), tmp['parity'], float(tmp['stop'])

    def get_rect(self):
        tmp = self._get_root()['rect']
        rect = QRect()
        rect.setX(tmp['x'])
        rect.setY(tmp['y'])
        rect.setWidth(tmp['width'])
        rect.setHeight(tmp['height'])
        return rect
