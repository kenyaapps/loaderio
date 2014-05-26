import requests
import json
class Client():
	"""
	Client endpoint to handle the api requests
	"""
	def __init__(self, api_key):
		self.api_key = api_key
		self.url = 'https://api.loader.io/v2/'
		pass

	def request(self, type, resource, payload=None):
		try:
			headers = {'loaderio-auth': self.api_key, 'Content-Type' : 'application/json'}
			if type is 'GET':			
				response = requests.get(self.url+resource, headers = headers)
			elif type is 'POST':
				response = requests.post(self.url+resource, data=json.dumps(payload), headers = headers)
			elif type is 'PUT':
				response = requests.put(self.url+resource, data=json.dumps(payload), headers = headers)
			else:
				response = requests.delete(self.url+resource, headers = headers)
			
			if response is not None:
				return response.json()
					
		except Exception, e:
			print e;
			pass
		finally:
			pass