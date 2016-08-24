#! /usr/bin/env python
"""InstaCLI project install script."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="instacli",
    version="0.1",
    description="Instagram command line application",
    long_description=open("README.md").read(),
    author="Teona Rusu, Matei Micu, Alexandru Coman",
    url="https://github.com/micumatei/InstaCLI",
    packages=["instacli"],
    scripts=["scripts/instacli"],
    requires=[]
)
