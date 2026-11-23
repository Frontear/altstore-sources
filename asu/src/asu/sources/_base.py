from abc import ABC, abstractmethod

class Source(ABC):
  def __init__(self, name, url):
    self.name = name
    self.url = url

  @abstractmethod
  def get_app(self, data):
    pass