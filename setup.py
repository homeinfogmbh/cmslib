#! /usr/bin/env python3

from distutils.core import setup


setup(
    name='cmslib',
    version='latest',
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info at homeinfo dot de>',
    maintainer='Richard Neumann',
    maintainer_email='<r dot neumann at homeinfo period de>',
    requires=[
        'configlib', 'flask', 'functoolsplus', 'his', 'hisfs', 'mdb',
        'peewee', 'peeweeplus', 'pyxb', 'terminallib'],
    packages=[
        'cmslib',
        'cmslib.functions',
        'cmslib.messages',
        'cmslib.orm',
        'cmslib.orm.charts',
        'cmslib.orm.content',
        'cmslib.presentation'],
    description='Conent Management Systemd library.')
