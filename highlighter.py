#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/27/2022 2:47 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : highlighter
# ---------------------
import re
import yaml
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, Qt, QFont


class UartHighLighter(QSyntaxHighlighter):

    config_filename = 'highlight.yaml'

    def __init__(self, parent=None):
        super(UartHighLighter, self).__init__(parent)
        self._mappings = {}
        with open(self.config_filename) as f:
            self.config = yaml.safe_load(f)

    def highlightBlock(self, text):
        for pattern, fmt in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)

    def setup_gui(self, doc):
        for item in self.config['highlight']:
            fmt = QTextCharFormat()
            fmt.setFontWeight(QFont.Weight.__dict__[item['weight']])
            fmt.setForeground(Qt.GlobalColor.__dict__[item['color']])
            self._mappings[item['pattern']] = fmt
        self.setDocument(doc)
