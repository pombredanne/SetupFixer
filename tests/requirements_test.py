# -*- coding: utf-8 -*-
################################################################################
# Requirements File Parser Tests
################################################################################

'''
Test suite for the requirements file parser.
'''

################################################################################
# Imports


import os
import platform

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from setupfixer.requirements import RequirementsParser


################################################################################
# Test Cases


class TestRequirementsParser(unittest.TestCase):
    '''
    '''

    def setUp(self):
        '''
        '''
        self.base_path = os.path.realpath(os.path.dirname(__file__))

    def test_dependency_links(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/001')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [
            'http://www.example.net/package/package-0.0.1.zip',
            'http://www.example.net/simple',
        ])

    def test_requirements(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/002')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'h5py==2.0.0', 'numpy', 'scipy',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__architecture_specific(self):
        '''
        '''
        system = platform.system().lower()
        if system == 'linux':
            expected = ['dbus-python>=0.84.0']
        elif system == 'windows':
            expected = ['wmi>=1.4.9']
        else:
            self.skipTest('Test not available for this platform.')
        path = os.path.join(self.base_path, 'data/003')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, expected)
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__setup(self):
        '''
        '''
        expected = ['nose>=1.0.0']
        path = os.path.join(self.base_path, 'data/004')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [])
        self.assertEquals(requirements.setup_requires, expected)
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {
            'setup': expected,
        })
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__tests(self):
        '''
        '''
        expected = ['mock', 'nose>=1.0.0']
        path = os.path.join(self.base_path, 'data/005')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, expected)
        self.assertEquals(requirements.extras_require, {
            'tests': expected,
        })
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__extras(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/006')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {
            'cython': ['lxml [cython]'],
            'pdf': ['PIL', 'reportlab==2.5']
        })
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__extras__architecture_specific(self):
        '''
        '''
        system = platform.system().lower()
        if system == 'linux':
            expected = ['easygconf']
        elif system == 'windows':
            expected = ['regobj']
        else:
            self.skipTest('Test not available for this platform.')
        path = os.path.join(self.base_path, 'data/007')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {
            'registry': expected,
        })
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__group_extras(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/008')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'random [abc, xyz]',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__group_extras_with_matching_versions(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/009')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'random==0.0.1 [abc, xyz]',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__remove_duplicates(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/010')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'double', 'triple==0.0.1',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])

    def test_requirements__package_with_dependency_link(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/011')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'package==0.0.1',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [
            'http://www.example.net/package/package-0.0.1.zip',
        ])

    def test_requirements__editable_package(self):
        '''
        '''
        path = os.path.join(self.base_path, 'data/012')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'package',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [
            'http://git.example.net/package/package.git#egg=package',
        ])

    def test_requirements__path_with_extra_hyphens(self):
        '''
        Check extraction of extras name and operating system name.
        '''
        path = os.path.join(self.base_path, 'data/013/a-b-c')
        requirements = RequirementsParser(path=path)
        self.assertEquals(requirements.install_requires, [
            'h5py==2.0.0', 'numpy', 'scipy',
        ])
        self.assertEquals(requirements.setup_requires, [])
        self.assertEquals(requirements.tests_require, [])
        self.assertEquals(requirements.extras_require, {})
        self.assertEquals(requirements.dependency_links, [])


################################################################################
# vim:et:ft=python:nowrap:sts=4:sw=4:ts=4
