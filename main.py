#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 7/21/2022 11:09 AM
# @Author  : jonas pan
# @Email   : jonas.pan@signify.com
# @File    : main
# ---------------------
import logging
import coloredlogs
import os
import sys
import py_mainwindow
from PySide6.QtWidgets import QApplication


class Main:

    @staticmethod
    def setup_logging(level=logging.DEBUG, log_folder='log', filename='mainwindow.log'):
        log_filename = None
        if filename is not None and log_folder is not None:
            log_filename = log_folder + os.sep + filename
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        log_format = '%(asctime)s - %(levelname)5s - %(lineno)4s - %(filename)18s - %(message)s'
        logging.basicConfig(filename=log_filename, level=level, format=log_format)
        if log_filename is not None:
            console = logging.StreamHandler(stream=sys.stdout)
            console.setLevel(logging.getLogger().level)
            console.setFormatter(logging.Formatter(log_format))
            logging.getLogger().addHandler(console)
        coloredlogs.install(level=level, fmt=log_format, milliseconds=True)

    @classmethod
    def run(cls):
        cls.setup_logging()
        app = QApplication(sys.argv)
        tmp = py_mainwindow.MainWindow()
        tmp.show()
        try:
            sys.exit(app.exec())
        except Exception as e:
            logging.error(e)


if __name__ == '__main__':
    Main.run()

