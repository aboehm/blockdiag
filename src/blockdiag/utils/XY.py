#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    from collections import namedtuple
except ImportError:
    from utils.namedtuple import namedtuple


XY = namedtuple('XY', 'x y')
