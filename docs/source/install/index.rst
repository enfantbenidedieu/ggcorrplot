.. _install:

=======
Install
=======

.. tip::
    This page assumes you are comfortable using a terminal and are familiar with package managers. The only prerequisite for installing ggcorrplot is Python itself.

Virtual environment
~~~~~~~~~~~~~~~~~~~

Install the 64-bit version of Python 3, for instance from the `official website <https://www.python.org/>`_. Now create a `virtual environment (venv) <https://docs.python.org/3/tutorial/venv.html>`_ and install ggcorrplot.

.. note::
    The virtual environment is optional but strongly recommended, in order to avoid potential conflicts with other packages.

.. code-block:: console

    PS C:\> python -m venv ggcorrplot-env # create virtual env
    PS C:\> ggcorrplot-env\Scripts\activate  # activate
    PS C:\> pip install -U ggcorrplot  # install ggcorrplot

Version
~~~~~~~

In order to check your installation, you can use.

.. code:: python

    import ggcorrplot
    print(ggcorrplot.__version__)

Using an isolated environment such as pip venv or conda makes it possible to install a specific version of ggcorrplot with pip and conda and its dependencies independently of any previously installed Python packages.

.. note::
    You should always remember to activate the environment of your choice prior to running any Python command whenever you start a new terminal session.

Dependencies
~~~~~~~~~~~~

ggcorrplot is compatible with python version which supports both dependencies :

===========  =======
Dependency   Version
===========  =======
numpy        2.3.4
pandas       2.3.3
scipy        1.16.3
plotnine     0.15.1
===========  =======