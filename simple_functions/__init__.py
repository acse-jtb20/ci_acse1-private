from .constants import * # noqa
from .functions1 import * # noqa
from .subtract import * #nopq

from pkg_resources import get_distribution, DistributionNotFound
try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
