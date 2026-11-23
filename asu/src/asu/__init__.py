import json
import os
import requests
import typing

from .sources import ALL_SOURCES

# schema: https://faq.altstore.io/developers/make-a-source
def create_source() -> dict[str, typing.Any]:
  return {
    "name": "Frontear's AltStore Repo",
    "subtitle": "Frontear's personal collection",
    "description": "Frontear's personal collection of AltStore apps",
    # from my GitHub avatar
    "iconURL": "https://avatars.githubusercontent.com/u/31909298",
    "website": "https://github.com/Frontear/altstore-sources",

    # LEAVE EMPTY!
    # These are populated by the custom sources
    "apps": [],
  }

def populate_apps(source_obj: dict[str, typing.Any]):
  for source in ALL_SOURCES:
    resp = requests.get(source.url)
    if resp.status_code != 200:
      print(f"Failed to download '{source.name}'")

    data = resp.json()
    app_entry = source.get_app(data)

    source_obj["apps"].append(app_entry)

def main() -> None:
  source_obj = create_source()

  populate_apps(source_obj)

  os.makedirs("assets", exist_ok=True)
  with open("assets/source.json", "w") as f:
    json.dump(source_obj, f, indent=2)