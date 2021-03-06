# -*- encoding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4 textwidth=79
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import bugspots

setup(
    name="bugspots",
    version=bugspots.__version__,
    description="Identify hot spots in a codebase with the bug prediction "
    "algorithm used at Google.",
    long_description=bugspots.__doc__,
    author=bugspots.__author__,
    author_email="pickusr@gmail.com",
    url="https://github.com/d0vs/bugspots",
    py_modules=["bugspots"],
    scripts=["bugspots.py"],
    license=bugspots.__license__,
    platforms="Unix",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"])
