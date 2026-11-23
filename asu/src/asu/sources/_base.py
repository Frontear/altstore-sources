import typing

from abc import ABC, abstractmethod

class Source(ABC):
  def __init__(self, name: str, url: str):
    self.name = name
    self.url = url

  @abstractmethod
  def get_app(self, data: dict[str, typing.Any]):
    pass