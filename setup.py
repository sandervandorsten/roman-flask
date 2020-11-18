"""A setuptools based setup module.

See:
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="romanflask",
    version="0.0.1",
    description="But that is how one learns, is it not? By trying and failing?",
    
    # The project's main homepage.
    url="https://github.com/sandervandorsten/roman-flask",
    
    # Author details
    author="Sander van Dorsten",
    author_email="sandervandorsten@gmail.com",
    
    # Choose your license
    license="MIT",

    # What does your project relate to?
    keywords="flask roman numeral",
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
   
    # List run-time dependencies here. These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["flask"],
    
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": [
            "roman_api=romanflask.interface.api:main",
            "roman_cli=romanflask.interface.cli:main",
        ]
    },
)
