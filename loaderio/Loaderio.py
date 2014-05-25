from resources.client import Client
from resources.apps import Apps
from resources.results import Results
from resources.servers import Servers
from resources.tests import Tests


class Loaderio():
	"""

	"""
	def __init__(self, api_key):
		self.api_key = api_key
		self.apps = Apps(self.api_key)
		self.results = Results(self.api_key)
		self.servers = Servers(self.api_key)
		self.tests = Tests(self.api_key)