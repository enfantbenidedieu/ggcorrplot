.. _getting_started:

===============
Getting started
===============

`ggcorrplot <https://github.com/enfantbenidedieu/ggcorrplot>`_ is an open source python library dedicated to correlation matrix visualization. It is distributed under the MIT Licence.

The purpose of this guide is to illustrate some of the main features of ``ggcorrplot``.

Here is a simple example where we use ggcorrplot to ``mtcars`` data:

    >>> from plotnine.data import mtcars
    >>> from ggcorrplot import ggcorrplot
    >>> mtcars = mtcars.set_index("name") # set name as index
    >>> #with correlation matrix
    >>> p = ggcorrplot(mtcars.corr())
    >>> p
    >>> #with original data
    >>> p = ggcorrplot(mtcars, matrix_type = "completed")
    >>> p