#!/usr/bin/env python

from distutils.core import setup, Extension

MOD = 'ext'

setup(name=MOD, ext_modules=[Extension(MOD, sources=['ext.c'])])
