#! /usr/bin/env python3
"""Install script."""

from setuptools import setup


setup(
    name='cmslib',
    use_scm_version={
        "local_scheme": "node-and-timestamp"
    },
    setup_requires=['setuptools_scm'],
    author='HOMEINFO - Digitale Informationssysteme GmbH',
    author_email='<info at homeinfo dot de>',
    maintainer='Richard Neumann',
    maintainer_email='<r dot neumann at homeinfo period de>',
    install_requires=[
        'bookings',
        'configlib',
        'ferengi',
        'filedb',
        'flask',
        'functoolsplus',
        'his',
        'hisfs',
        'hwdb',
        'mdb',
        'newslib',
        'openimmodb',
        'peewee',
        'peeweeplus',
        'pyxb',
        'werkzeug',
        'wsgilib'
    ],
    packages=[
        'cmslib',
        'cmslib.functions',
        'cmslib.functions.charts',
        'cmslib.orm',
        'cmslib.orm.charts',
        'cmslib.orm.charts.api',
        'cmslib.orm.content',
        'cmslib.presentation'
    ],
    description='Conent Management Systemd library.'
)
