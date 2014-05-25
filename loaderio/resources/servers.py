from loaderio.resources.client import Client

class Servers(Client):
	"""

	"""
	def __init__(self, api_key):
		Client.__init__(self, api_key)
		pass

	def list(self):
		pass