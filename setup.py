#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import v2rayU

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setup(
    name='v2rayU',
    version=v2rayU.__version__,
    description="a tool to manage v2ray config json",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='python v2ray v2rayU vmess socks5',
    author='DockerCS',
    author_email='dockercs@163.com',
    url='https://github.com/DockerCS/v2rayU',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'v2rayU = v2rayU.main:menu'
        ]
    },
    classifiers=[
        'Topic :: Utilities',
        'Development Status :: 5 - Production/Stable',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)