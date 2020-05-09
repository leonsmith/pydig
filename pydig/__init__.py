__version__ = '0.3.0'

from .query_type import *  # noqa
from .resolver import *  # noqa

_resolver = Resolver()
query = _resolver.query
