# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bluetheme/__init__.py
from bluetheme import __version__ as version

setup(
	name='prussiantheme',
	version=version,
	description='Material UI for ERPNext',
	author='Roy Irwan',
	author_email='roy.irwan@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
