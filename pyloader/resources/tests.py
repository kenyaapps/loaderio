from resources.client import Client

class Tests(Client):
	"""
	Tests resources
	"""

	def __init__(self, api_key):
		Client.__init__(self, api_key)		
		pass

	def list_tests(self):
		pass

	def create_test(self):
		pass
	
	def run_test(self, test_id):
		pass

	def stop_test(self, test_id):
		pass