#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 8/24/2022 10:05 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : action_agent
# ---------------------
import re
import threading
import logging
import datetime


class ActionBean:

    def __init__(self, idx, flag, timeout, delay, cmd):
        self.idx = idx
        self.flag = flag
        self.timeout = timeout
        self.delay = delay
        self.cmd = cmd
        self.flag_is_found = False


class ActionAgent:

    def __init__(self, uart, signal):
        self.uart = uart
        self.signal = signal
        self._thread = None
        self._terminated = None
        self.action_beans = None
        self.loop_count = None
        self.bean = None
        self.pattern = None

    def init(self, cfg, count):
        if self._thread is not None:
            raise Exception('action task is under going')
        self.action_beans = []
        self.loop_count = count
        for a in cfg:
            idx = a['id']
            flag = a['flag']
            timeout = a['timeout']
            delay = a['delay']
            cmd = a['cmd']
            b = ActionBean(idx, flag, timeout, delay, cmd)
            self.action_beans.append(b)

    def parse(self, ctx):
        if self.pattern is not None and self.pattern.match(ctx.line_text):
            self.bean.flag_is_found = True

    def loop(self):
        self.uart.parser_register(self.parse)
        try:
            self.bean = None
            tp = None
            cnt = self.loop_count
            cur = 0
            status = 100
            while not self._terminated:
                if status == 100:  # start a new action
                    self.bean = self.action_beans[cur]
                    if self.bean.flag is None:
                        status = 400
                    else:
                        tp = datetime.datetime.now() + datetime.timedelta(seconds=self.bean.timeout)
                        self.bean.flag_is_found = False
                        self.pattern = re.compile(self.bean.flag)
                        status = 200
                elif status == 200:  # check flag
                    if datetime.datetime.now() >= tp or self.bean.flag_is_found:
                        self.pattern = None
                        status = 400
                    else:
                        self._thread.sleep(0.1)
                elif status == 400:  # delay to send
                    self._thread.sleep(self.bean.delay)
                    status = 500
                elif status == 500:  # send cmd
                    self.signal.send(self.bean.cmd)
                    self.bean = None
                    status = 100
                    cur += 1
                    if cur >= len(self.action_beans):
                        cur = 0
                        cnt -= 1
                        if cnt <= 0:
                            self._terminated = True
        except Exception as e:
            logging.error('uncaught exception in action loop, %s' % e)
            self.signal.show_alert('Error', 'unexpected error in action loop, %s' % e)
        finally:
            self.uart.parser_unregister(self.parse)
            self._terminated = True
            self._thread = None

    def start(self):
        if self._thread is None:
            self._terminated = False
            self._thread = threading.Thread(target=self.loop)
            self._thread.daemon = True
            self._thread.start()
        else:
            # shouldn't come here
            logging.error('start action while action is under going')

    def stop(self):
        if self._thread is not None:
            self._terminated = True
            self._thread = None
        else:
            # shouldn't come here
            logging.error('stop action while action is stopped')
