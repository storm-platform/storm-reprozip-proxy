#!/bin/bash
#
# Copyright (C) 2021 Storm Project.
#
# storm-job-reana is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

#
# Proxing the reprozip experiment bundle
#
storm-reprozip-proxy run --bundle /opt/input/package.rpz --no-include-user-definition

#
# Creating a base user
#
/busybox adduser reprouser -u 1000 --disabled-password --gecos ""
