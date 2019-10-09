"""Foobar package"""

import pkg_resources


__version__ = pkg_resources.get_distribution("foobar").version
__all__ = ["__version__"]
