from .builtins import * # noqa

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("envtest")
except PackageNotFoundError:
    __version__ = "unknown"
