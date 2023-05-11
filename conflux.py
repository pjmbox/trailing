#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :  19:06
# @Author  : jiang.pan
# @Email   : jiang.pan@signify.com
# @File    : conflux.py
# ---------------------
import serial
import struct
import zlib
import binascii
import logging

channel_text = [b'', b'']
last_tx_sn = 0


def _unpack_packet(data):
    data, crc32 = struct.unpack("64s I", data)
    tmp = zlib.crc32(data)
    if crc32 != tmp:
        raise Exception('crc error: old = 0x%08x, new = 0x%08x, data = %s' % (crc32, tmp, binascii.hexlify(data)))
    sync, tmp, data = struct.unpack("H B 61s", data)
    rx_sn = tmp & 0x0f
    tx_sn = (tmp >> 4) & 0x0f
    group = []
    length = 61
    while True:
        tmp, data = struct.unpack("B %ds" % (length - 1), data)
        ch = (tmp >> 6) & 0x03
        cnt = tmp & 0x3f
        if cnt == 0:
            break
        length -= (cnt + 1)
        if length == 0:
            val = data
        else:
            val, data = struct.unpack("%ds %ds" % (cnt, length), data)
        group.append((ch, val))
        if length <= 1:
            break
    global last_tx_sn
    if (last_tx_sn + 1) & 0xf != tx_sn:
        logging.error('missing one packet: last sn = %d, current sn = %d' % (last_tx_sn, tx_sn))
    last_tx_sn = tx_sn
    return tx_sn, rx_sn, crc32, group


def fetch_data(client: serial.Serial):
    tmp = ''
    status = 100
    while True:
        if status == 100:
            tmp = client.read(1)
            if tmp == b'\xaa':
                status = 200
        elif status == 200:
            tmp = client.read(1)
            if tmp == b'\x55':
                tmp = b'\xaa\x55'
                status = 300
            else:
                status = 100
        elif status == 300:
            if len(tmp) < 68:
                tmp += client.read(68 - len(tmp))
                continue
            break
    tx_sn, rx_sn, crc32, group = _unpack_packet(tmp)
    for ch, txt in group:
        if ch < 2:
            channel_text[ch] += txt


def read_cache():
    for i in range(2):
        p = channel_text[i].find(b'\n')
        if p > 0:
            tmp = channel_text[i][:p + 1]
            channel_text[i] = channel_text[i][p + 1:]
            return tmp
    return None


def read_line(client: serial.Serial):
    while True:
        tmp = read_cache()
        if tmp is not None:
            return tmp
        fetch_data(client)
