# !/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="mongoct",
    packages=find_packages(),
    version="0.1.0",
    description="MongoDB Change Streams tracker",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@buffer.com",
    url="https://github.com/bufferapp/mongoct",
    keywords=["mongodb", "change-stream", "crawler"],
    install_requires=["pymongo", "click", "dnspython"],
    entry_points={"console_scripts": ["mongoct=mongoct.cli:run"]},
)
