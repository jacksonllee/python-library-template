Foobar library
==============

`foobar` is a Python library for blah blah blah.

Download and Installation
-------------------------

(For non-public repos, omit this section.)

.. code-block:: bash

    pip install <some-library-name>

License
-------

MIT License

Setting Up A Local Development Environment
------------------------------------------

For local development, set up an isolated Python environment,
then download and install from the GitHub source:

.. code-block:: bash

    git clone <some-appropriate-url>
    cd foobar
    pip install -r dev-requirements.txt
    pip install -e .

To run tests and styling checks:

.. code-block:: bash

    flake8 src tests
    pytest
    black --check src tests

## For Maintainers

* [Releasing the package on the Python Package Index (PyPI)](pypi_release.md)
* TODO Compiling the documentation website
