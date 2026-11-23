from .aidoku import AidokuSource
from .open_parsec import OpenParsecSource
from .spotify import SpotifySource
from .youtube import YouTubeSource

ALL_SOURCES = [
  AidokuSource(),
  OpenParsecSource(),
  SpotifySource(),
  YouTubeSource(),
]