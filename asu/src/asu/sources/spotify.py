from ._base import Source

class SpotifySource(Source):
  def __init__(self):
    super().__init__("Spotify", "https://raw.githubusercontent.com/SideloadLabs/SideloasLabs-AltSource/refs/heads/main/apps.json")

  def get_app(self, data):
    # There are two variants, this and "(PATCHED)".
    # The latter can only work on a jailbroken device, which I do not have.
    assert data["apps"][0]["name"] == "EeveeSpotifyReincarnated"

    return data["apps"][0]