from ._base import Source

class AidokuSource(Source):
  def __init__(self):
    super().__init__("Aidoku", "https://raw.githubusercontent.com/Aidoku/Aidoku/altstore/apps.json")

  def get_app(self, data):
    return data["apps"][0]