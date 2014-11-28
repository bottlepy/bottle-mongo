#!/usr/bin/env python
from setuptools import setup


REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setup(
    name = 'bottle-mongo',
    version = '0.2.4',
    url = 'https://github.com/bottlepy/bottle-mongo',
    description = 'MongoDB integration for Bottle',
    author = 'Thiago Avelino',
    author_email = 'thiago@avelino.xxx',
    license = 'MIT',
    platforms = 'any',
    py_modules = [
        'bottle_mongo'
    ],
    install_requires = REQUIREMENTS,
    classifiers = [
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Bottle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
