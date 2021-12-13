# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-reprozip-proxy is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Proxy to handling files into reprounzip-docker executions"""

import os

from setuptools import find_packages, setup

readme = open("README.rst").read()
history = open("CHANGES.rst").read()

tests_require = []

extras_require = {
    "docs": [
        "Sphinx>=3,<4",
    ],
    "tests": tests_require,
    "cli": [
        "click>=7.1.0",
    ],
}

extras_require["all"] = [req for _, reqs in extras_require.items() for req in reqs]

setup_requires = []

install_requires = [
    # Reprozip dependencies
    "rpaths>=1.0.0,<1.1",
    "reprounzip>=1.1,<2.0",
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join("storm_reprozip_proxy", "version.py"), "rt") as fp:
    exec(fp.read(), g)
    version = g["__version__"]

setup(
    name="storm-reprozip-proxy",
    version=version,
    description=__doc__,
    long_description=readme + "\n\n" + history,
    keywords=["Storm Platform", "CLI tool", "Reprozip", "Utility"],
    license="MIT",
    author="Felipe Menino Carlos",
    author_email="felipe.carlos@inpe.br",
    url="https://github.com/storm-platform/storm-reprozip-proxy",
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    entry_points={
        "console_scripts": ["reprozip-proxy = storm_reprozip_proxy.cli:cli"],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 1 - Planning",
    ],
)
