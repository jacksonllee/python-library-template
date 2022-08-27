# Make a release on PyPI

1. Ensure packaging tools are installed and up-to-date.

    ```bash
    $ pip install -U build twine pip setuptools
    ```

2. Generate the source distribution and wheel.

    ```bash
    $ python -m build
    ```

3. After this command finishes, new files are found under `dist/`:

    ```
    dist/
        <package-name>-x.y.z.tar.gz
        <package-name>-x.y.z-py3-none-any.whl
    ```

4. Upload the newly generated distribution files to PyPI.
   (PyPI username and password will be asked for.)

    ```bash
    $ twine upload dist/<package-name>-x.y.z.tar.gz
    $ twine upload dist/<package-name>-x.y.z-py3-none-any.whl
    ```
