from loaderio.resources.client import Client

class Results(Client):
	"""

	"""
	def __init__(self, api_key):
		Client.__init__(self, api_key)
		pass

	def list(self, test_id):
		return self.request('GET', 'tests/'+test_id+'/results')

	def get(self, test_id, results_id):
		return self.request('GET', 'tests/'+test_id+'/results/'+results_id)