#!/usr/bin/env python
# -*- coding: utf-8 -*-

# SetupFixer is a collection of utilities for easy configuration of setuptools
# Copyright (c) 2012 Flight Data Services Ltd
# http://www.flightdatacommunity.com

try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from setupfixer import __version__ as VERSION
from setupfixer.requirements import RequirementsParser
requirements = RequirementsParser()

setup(
    name='SetupFixer',
    version=VERSION,
    author='Flight Data Services Ltd',
    author_email='developers@flightdataservices.com',
    description='Setup Fixer is a collection of utilities for easy configuration of setuptools.',
    long_description=open('README').read()+open('CHANGES').read()+open('TODO').read(),
    license='Open Software License (OSL-3.0)',
    url='http://www.filterpype.org/',
    download_url='http://www.filterpype.org/',    
    packages=find_packages(exclude=['distribute_setup', 'requirements', \
    'tests']),
    # The 'include_package_data' keyword tells setuptools to install any 
    # data files it finds specified in the MANIFEST.in file.    
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements.install_requires,
    setup_requires=requirements.setup_requires,
    tests_require=requirements.tests_require,
    extras_require=requirements.extras_require,
    dependency_links=requirements.dependency_links,
    test_suite='nose.collector',
    platforms=[
        'OS Independent',
    ],        
    keywords=['setuptools', 'pip', 'requirements'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Open Software License (OSL-3.0)",        
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
