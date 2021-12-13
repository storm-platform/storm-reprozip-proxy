#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

FROM golang:1.14.12

#
# Copy files
#
COPY parser/ /usr/src/app/parser

#
# Build the Storm Reprozip parser module
#
WORKDIR /usr/src/app/parser
RUN go mod download \
    && go build -o storm-reprozip-parser
