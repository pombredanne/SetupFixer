.. _Principles:

Principles
==========

`pip`_ is a tool for installing and managing Python packages, such as those 
found in the Python Package Index. It's a replacement for ``easy_install``.

`Distribute`_ is a fork of the *Setuptools* project. *Distribute* is intended to 
replace *Setuptools* as the standard method for working with Python module 
distributions.

``pip`` has a feature where package dependencies can be described in a simple 
text file called ``requirements.txt``. The packages dependencies described in a 
*requirements* file can be installed from just about anywhere, including a 
Python Package Index (PyPI) compliant server, arbitrary download sites and 
version control systems such as Bazaar, Git, Subversion, etc.

Complementary to that, ``setup.py`` which is used by *distutils* and *setuptools* 
to package Python modules has several keywords to define different types of
dependencies that a package may have. From the *setuptools* documentation:

* ``install_requires``
 * A string or list of strings specifying what other distributions need to be installed when this one is. 
    
* ``extras_require``
 * A dictionary mapping names of *extras* (optional features of your project) to strings or lists of strings specifying what other distributions must be installed to support those features. 
    
* ``setup_requires``
 * A string or list of strings specifying what other distributions need to be present in order for the setup script to run.

* ``dependency_links``
 * A list of strings naming URLs to be searched when satisfying dependencies. 
    
* ``tests_require``
 * If your project's tests need one or more additional packages besides those needed to install it, you can use this option to specify them. 

`Flight Data Services`_ wanted the best of both worlds:

* Use pip *requirements* files to easily deploy servers and CI test environments 
* Still have packages that can be installed in the usual way via ``pip`` or 
  ``easy_install`` for users of our Open Source software.

However, we didn't want to maintain package requirements in multiple places so 
we created SetupFixer. SetupFixer parses one, or more, pip *requirements* files 
and automatically populates the *setuptools* keywords listed above based on what
it finds. All package dependency management is now maintained in a few easy to 
read text files that act as the single source for package dependency tracking.

.. _pip: http://pypi.python.org/pypi/pip
.. _Distribute: http://pypi.python.org/pypi/distribute
.. _Flight Data Services: http://www.flightdataservices.com/
