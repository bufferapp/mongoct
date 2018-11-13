# !/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mongoct",
    packages=find_packages(),
    version="0.1.2",
    description="MongoDB Change Streams tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="David Gasquez",
    license="MIT",
    author_email="davidgasquez@buffer.com",
    url="https://github.com/bufferapp/mongoct",
    keywords=["mongodb", "change-stream", "crawler"],
    install_requires=["pymongo", "click", "dnspython"],
    entry_points={"console_scripts": ["mongoct=mongoct.cli:run"]},
)
