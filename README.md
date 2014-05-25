Pyloader
===========================================
Python wrapper for loader.io api v2

** Installation
    pip install pyloader

** How to use
Go to go loader.io [http://docs.loader.io/api/intro.html] for more details on api resources.

*** Resources

*** Applications

```
	loader = Pyloader('API_KEY')
	print loader.apps.list()
	print loader.apps.create('www.example.com')
	print loader.apps.get('app_id')
	print loader.apps.verify('app_id', method = 'http')
	print loader.apps.delete('app_id')
