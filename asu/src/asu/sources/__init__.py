from .aidoku import AidokuSource
from .open_parsec import OpenParsecSource
from .spotify import SpotifySource

ALL_SOURCES = [
  AidokuSource(),
  OpenParsecSource(),
  SpotifySource(),
]