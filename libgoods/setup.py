#!/usr/bin/env python

"""
setup.py for the libgoods package
"""

# This setup is suitable for "python setup.py develop".
from setuptools import setup

from libgoods import __version__

setup(
    name="libgoods",
    version=__version__,
    description="utilities for pre-processing input data for GNOME",
    long_description=open("README.md").read(),
    packages=["libgoods"],
    # note: this is only a few of the scripts -- the ones that may be useful
    scripts=["scripts/hycom2bna.py",
             "scripts/nc_time_shift.py",
             "scripts/shape2bna",
             "scripts/make_map.py"
             ],
    author="Amy MacFadyen, Christopher Barker",
    author_email="amy.macfadyen@noaa.gov, chris.barker@noaa.gov",
    url="http://www.gnome.orr.noaa.gov",
    license="LICENSE.txt",
    keywords="GNOME GOODS ORR",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Meteorology/Oceanography",
        "License :: Public Domain",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
    ],

    )


