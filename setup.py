# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="ggcorrplot", 
    version='0.1.0',
    author="Duvérier DJIFACK ZEBAZE",
    author_email="djifacklab@gmail.com",
    description="Visualization of a Correlation Matrix using plotnine",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/enfantbenidedieu/ggcorrplot",
    packages=find_packages(where="."),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
    install_requires=[
        "numpy>=2.3.4",
        "pandas>=2.3.3",
        "scipy>=1.16.3",
        "plotnine>=0.15.1"
    ],
    keywords="correlation matrix, matrix of correlation p-values, plotnine, ggplot",
    project_urls={
        "Bug Reports": "https://github.com/enfantbenidedieu/ggcorrplot/issues",
        "Source": "https://github.com/enfantbenidedieu/ggcorrplot",
        "Documentation": "https://ggcorrplot.readthedocs.io",
    }
)