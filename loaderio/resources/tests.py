from loaderio.resources.client import Client

class Tests(Client):
	"""
	Tests resources
	"""	
	def __init__(self, api_key):
		Client.__init__(self, api_key)		
		self.test_type = ''
		self.total = 0
		self.duration = 0
		self.urls = []
		self.name = ''
		self.timeout = 10000
		self.initial = 0
		self.error_threshold = 50
		self.callback = ''
		self.callback_email = ''
		self.scheduled_at = ''
		self.notes = ''

	def list(self):
		return self.request('GET', 'tests')

	def create(self):
		payload = {
			'test_type' : self.test_type,
			'total' : self.total,
			'duration' : self.duration,
			'urls' : self.urls,
			'name' : self.name
		}

		return self.request('POST', 'tests', payload)

	def get(self, test_id):
		return self.request('GET', 'tests/'+test_id)
	
	def run(self, test_id):
		return self.request('PUT', 'tests/'+test_id+'/run')

	def stop(self, test_id):
		return self.request('PUT', 'tests/'+test_id+'/stop')