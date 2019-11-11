#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyscribble',
    version='0.0.4',
    packages=find_packages(include=["pyscribble*"]),
    author='Thomas Schmelzer',
    author_email='thomas.schmelzer@gmail.com',
    description='', install_requires=['numpy', 'numexpr']
)
