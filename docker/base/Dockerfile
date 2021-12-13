#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

#
# Compiled tool layers
#
FROM amd64/busybox:1.30.0-glibc as busybox
FROM stormproject/storm-reprozip-parser:latest as storm-reprozip-parser

FROM ubuntu:20.04

#
# Install base dependencies
#
RUN apt update -y \
    && apt install \
        git \
        curl \
        python3 \
        python3-pip \
        python3-dev -y \
    && pip3 install poetry

#
# Install storm-reprozip
#
COPY . /usr/src/app/storm_reprozip_proxy
RUN cd /usr/src/app/storm_reprozip_proxy \
    # Configuring the poetry to install the dependencies
    # in the system site package
    && poetry config virtualenvs.create false \
    && poetry install

#
# Install busybox (1.30 glibc - used to fix the bug 11651[https://bugs.busybox.net/show_bug.cgi?id=11651])
# The issue was solved based on solutions presented in the distroless issue #225
# (https://github.com/GoogleContainerTools/distroless/issues/225).
#
COPY --from=busybox /bin/busybox /busybox
RUN ["/busybox", "--install", "/bin"]

#
# Install storm-reprozip-parser
#
COPY --from=storm-reprozip-parser /usr/src/app/parser/storm-reprozip-parser /storm-reprozip-parser

#
# Environment files
#
COPY docker/base/third-party/ /opt/third-party
RUN cd /opt/third-party \
    && chmod +x install.sh \
    && ./install.sh

RUN chmod +x /rpzsudo /rpztar /storm-reprozip-parser
