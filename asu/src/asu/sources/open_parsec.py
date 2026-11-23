from ._base import Source

class OpenParsecSource(Source):
  def __init__(self):
    super().__init__("OpenParsec", "https://raw.githubusercontent.com/NearFrame/OpenParsec/refs/heads/main/altstore.json")

  def get_app(self, data):
    return data["apps"][0]