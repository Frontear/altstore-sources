import typing

from ._base import Source

class YouTubeSource(Source):
  def __init__(self):
    super().__init__("YouTube", "https://raw.githubusercontent.com/mrdrvt99/Altstore-Repository/main/ytlite.json")

  def get_app(self, data: dict[str, typing.Any]):
    return data["apps"][0]