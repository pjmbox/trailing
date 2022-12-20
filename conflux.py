#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    :  19:06
# @Author  : jiang.pan
# @Email   : jiang.pan@signify.com
# @File    : conflux.py
# ---------------------
import logging
import serial
import struct
import zlib

channel_text = [b'', b'']


def _unpack_packet(data):
    data = struct.unpack("60s I", data)
    crc32 = data[1]
    tmp = zlib.crc32(data[0])
    if crc32 != tmp:
        raise Exception('crc error: old = %08x, new = %08x, data = %s' % (crc32, tmp, data))
    data = data[0]
    data = struct.unpack("59s b", data)
    tx_sn = (data[1] >> 4) & ((1 << 4) - 1)
    rx_sn = data[1] & ((1 << 4) - 1)
    data = data[0]
    group = []
    x = 59
    while True:
        data = struct.unpack("b %ds" % (x - 1), data)
        ch = (data[0] >> 6) & ((1 << 2) - 1)
        cnt = data[0] & ((1 << 6) - 1)
        if cnt == 0:
            break
        data = data[1]
        x -= cnt + 1
        if x == 0:
            val = data
        else:
            data = struct.unpack("%ds %ds" % (cnt, x), data)
            val = data[0]
            data = data[1]
        group.append((ch, val))
        if x <= 1:
            break
    return tx_sn, rx_sn, crc32, group


def fetch_data(client: serial.Serial):
    tmp = []
    while True:
        try:
            tmp = client.read(64)
            if len(tmp) != 64:
                client.flushInput()
                continue
            tmp = _unpack_packet(tmp)
            break
        except Exception as e:
            logging.error(e)
            client.flushInput()
            continue
    for ch, txt in tmp[3]:
        if ch < 2:
            channel_text[ch] += txt
        else:
            logging.debug('discard pkt, chn: %d, data: %s' % (ch, txt))


def read_cache():
    for i in range(2):
        p = channel_text[i].find(b'\n')
        if p > 0:
            tmp = channel_text[i][:p + 1]
            channel_text[i] = channel_text[i][p + 1:]
            return tmp
    return None


def read_line(client: serial.Serial):
    tmp = read_cache()
    if tmp is not None:
        return tmp
    fetch_data(client)
    return read_cache()
