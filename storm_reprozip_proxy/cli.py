# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

import click

from storm_reprozip_proxy.proxy import reprozip_proxy_run


@click.group(name="reprozip-proxy")
@click.version_option()
def reprozip_proxy():
    """Reprozip Proxy base CLI."""


@click.command(name="run")
@click.option("--bundle", required=True)
@click.option("--input-file", multiple=True)
@click.option("--input-name", multiple=True)
def reprozip_run(bundle, input_file, input_name):
    reprozip_proxy_run(bundle, input_file, input_name)
