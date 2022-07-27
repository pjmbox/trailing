#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/27/2022 2:47 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : highlighter
# ---------------------
import re
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, Qt, QFont


class UartHighLighter(QSyntaxHighlighter):

    def __init__(self, parent=None):
        super(UartHighLighter, self).__init__(parent)
        self._mappings = {}

    def add_mapping(self, pattern, fmt):
        self._mappings[pattern] = fmt

    def highlightBlock(self, text):
        for pattern, fmt in self._mappings.items():
            for match in re.finditer(pattern, text):
                start, end = match.span()
                self.setFormat(start, end - start, fmt)

    def _add_fmt(self, pattern, color):
        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(color)
        self.add_mapping(pattern, fmt)

    def setup_gui(self, doc):
        self._add_fmt('DEBUG', Qt.darkGreen)
        self._add_fmt('INFO', Qt.darkBlue)
        self._add_fmt('WARNING', Qt.darkYellow)
        self._add_fmt('ERROR', Qt.red)
        self.setDocument(doc)
