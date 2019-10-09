import os
import setuptools


_VERSION = "0.0.0"

if getattr(setuptools, "__version__", "0") < "39":
    # v36.4.0+ needed to automatically include README.md in packaging
    # v38.6.0+ needed for long_description_content_type in setup()
    raise EnvironmentError(
        "Your setuptools is too old. "
        "Please run 'pip install --upgrade pip setuptools'."
    )

_THIS_DIR = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(_THIS_DIR, "README.md")) as f:
    _LONG_DESCRIPTION = f.read().strip()


def main():
    setuptools.setup(
        name="foobar",
        version=_VERSION,
        author="Jackson L. Lee",
        author_email="(email)",
        description="(short description)",
        long_description=_LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        # py_modules=["file1.py"] instead for a single file package
        packages=setuptools.find_packages(),
        url="(URL)",
        keywords=["keyword1", "keyword2"],
        license="Apache 2.0",
        python_requires=">=3.6",
        zip_safe=False,
        # Minimal requirements (vs. exact version pins in requirements.txt)
        install_requires=["setuptools"],
        # PyPI trove classifiers, see https://pypi.org/classifiers/
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Development Status :: 3 - Alpha",
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
        ],
        data_files=[
            (".", ["LICENSE.txt", "CHANGELOG.md", "requirements.txt"]),
        ],
    )


if __name__ == "__main__":
    main()
