#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/19/2022 1:18 PM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : common
# ---------------------
import enum


class UartDirection(enum.Enum):
    ToUart = '<<'
    FromUart = '>>'


class LineContext:

    def __init__(self):
        self.line_raw = None
        self.time_raw = None


class TextLineContext(LineContext):

    def __init__(self):
        super(TextLineContext, self).__init__()
        self.is_hex = None
        self.line_text = None


class UpstreamLineContext(TextLineContext):
    dir = UartDirection.ToUart


class DownstreamLineContext(TextLineContext):
    dir = UartDirection.FromUart
