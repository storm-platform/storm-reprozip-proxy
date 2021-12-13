# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Proxy to handling files into reprounzip-docker executions"""

import os

REPROZIP_PROXY_DOCKER_IMAGE_TAG = "storm/storm-reprozip-proxy:latest"

REPROZIP_INCLUDE_USER_DEFINITION = int(os.getenv("REPROZIP_INCLUDE_USER_DEFINITION", 1))
