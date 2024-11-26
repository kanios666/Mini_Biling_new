"""
PySide6-Frameless-Window
========================
A cross-platform frameless window based on pyside6, support Win32, Linux and macOS.

Documentation is available in the docstrings and
online at https://pyqt-frameless-window.readthedocs.io.

Examples are available at https://github.com/zhiyiYo/PyQt-Frameless-Window/tree/PySide6/examples.

:copyright: (c) 2021 by zhiyiYo.
:license: LGPLv3, see LICENSE for more details.
"""

__version__ = "0.4.3"
__author__ = "zhiyiYo"

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QMainWindow

from .titlebar import TitleBar, TitleBarButton, SvgTitleBarButton, StandardTitleBar, TitleBarBase

from .windows import WindowsFramelessWindow as FramelessWindow
from .windows import WindowsFramelessMainWindow as FramelessMainWindow
from .windows import WindowsFramelessDialog as FramelessDialog
from .windows import CustomFramelessWindow as EfektyOknaBezramkowego
