# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Proxy to handling files into reprounzip-docker executions"""

from .ext import StormReprozipProxy
from .version import __version__

__all__ = ('__version__', 'StormReprozipProxy')
