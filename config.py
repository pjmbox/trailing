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

    config_filename = 'cf_config.yaml'

    def __init__(self):
        with open(self.config_filename) as f:
            self.config = yaml.safe_load(f)

    def _get_root(self):
        return self.config['config']

    def save(self):
        with open(self.config_filename, 'w') as f:
            yaml.safe_dump(self.config, f)

    def is_conflux_enabled(self):
        tmp = self._get_root()['conflux']
        return tmp['enabled']

    def get_highlight_config_filename(self):
        tmp = self._get_root()['cfg_files']
        return tmp['highlight']

    def get_aliases_config_filename(self):
        tmp = self._get_root()['cfg_files']
        return tmp['aliases']

    def get_history_config_filename(self):
        tmp = self._get_root()['cfg_files']
        return tmp['history']

    def get_actions_config_filename(self):
        tmp = self._get_root()['cfg_files']
        return tmp['actions']

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

    def set_rcv_text(self, hexify, auto_scroll, max_rows):
        tmp = self._get_root()['rcv_text']
        tmp['hex'] = hexify
        tmp['auto_scroll'] = auto_scroll
        tmp['max_rows'] = max_rows

    def set_snd_text(self, hexify, cr, lf):
        tmp = self._get_root()['snd_text']
        tmp['hex'] = hexify
        tmp['carrier_return'] = cr
        tmp['line_feed'] =lf

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

    def get_rcv_text(self):
        tmp = self._get_root()['rcv_text']
        return tmp['hex'], tmp['auto_scroll'], tmp['max_rows']

    def get_snd_text(self):
        tmp = self._get_root()['snd_text']
        return tmp['hex'], tmp['carrier_return'], tmp['line_feed']
