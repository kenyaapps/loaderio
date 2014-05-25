from loaderio.resources.client import Client

class Apps(Client):
	"""

	"""
	def __init__(self, api_key):
		Client.__init__(self, api_key)
		pass

	def list(self):
		return self.request('GET', 'apps')

	def create(self, app):
		payload = { 'app': app }
		return self.request('POST', 'apps', payload)

	def get(self, app_id):
		return self.request('GET', 'apps/'+app_id)

	def verify(self, app_id, method):
		payload = { 'method': method }
		return self.request('POST', 'apps/'+app_id+'/verify', payload)

	def delete(self, app_id):
		return self.request('DELETE', 'apps/'+app_id)