#!/usr/bin/env python3
"""
PyInstaller builder for main.py
Builds a lightweight executable without icon
"""

import PyInstaller.__main__
import sys
import os

def build():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--noupx',
        '--clean',
        '--exclude-module', 'PyQt5',
        '--distpath', './dist',
        '--workpath', './build',
        '--specpath', './build',
    ])

if __name__ == '__main__':
    build()
