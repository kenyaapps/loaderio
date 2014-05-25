from loaderio.resources.client import Client
from loaderio.resources.apps import Apps
from loaderio.resources.results import Results
from loaderio.resources.servers import Servers
from loaderio.resources.tests import Tests


class Loaderio():
	"""

	"""
	def __init__(self, api_key):
		self.api_key = api_key
		self.apps = Apps(self.api_key)
		self.results = Results(self.api_key)
		self.servers = Servers(self.api_key)
		self.tests = Tests(self.api_key)
