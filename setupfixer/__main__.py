#!/usr/bin/env python
# -*- coding: utf-8 -*-
################################################################################
# Requirements File Parser for Setup Tools
################################################################################

'''
'''

################################################################################
# Imports


import os
import sys
import textwrap

from shutil import copy


################################################################################
# Helpers


def display_help_message():
    '''
    '''
    print >>sys.stderr, textwrap.dedent('''
    Installer for Setup Fixers

    Installer for helpful utilities to make using setuptools easier.

    Options:

        --help, -h          Display this help message.
        --install, -i       Install the requirements parser.
        --upgrade, -u       Upgrade the requirements parser.
    ''')


def install_requirements_parser(src_file, dst_file):
    '''
    '''
    if not os.path.isfile(dst_file):
        copy(src_file, dst_file)
        message = '[+] Installed requirements parser to current directory.'
    else:
        message = '[!] Requirements parser is already installed.'
    print >>sys.stderr, message


def upgrade_requirements_parser(src_file, dst_file):
    '''
    '''
    if os.path.isfile(dst_file):
        copy(src_file, dst_file)
        message = '[>] Upgraded requirements parser in current directory.'
    else:
        message = '[!] Requirements parser is not installed.'
    print >>sys.stderr, message


################################################################################
# Program


if __name__ == '__main__':

    src_path = os.path.realpath(os.path.dirname(__file__))
    src_file = os.path.join(src_path, 'requirements.py')
    dst_path = os.path.realpath('.')
    dst_file = os.path.join(dst_path, 'requirements.py')

    if '--help' in sys.argv[1:] or '-h' in sys.argv[1:]:
        display_help_message()
    elif '--install' in sys.argv[1:] or '-i' in sys.argv[1:]:
        install_requirements_parser(src_file, dst_file)
    elif '--upgrade' in sys.argv[1:] or '-u' in sys.argv[1:]:
        upgrade_requirements_parser(src_file, dst_file)
    else:
        display_help_message()


################################################################################
# vim:et:ft=python:nowrap:sts=4:sw=4:ts=4
