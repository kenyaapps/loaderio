Loaderio
===========================================
Python wrapper for loader.io api v2

## Installation
```pip install loaderio```

## How to use
Go to go [Loaderio][] for more details on api resources.

## Resources

### Applications

```
	from loaderio.Loaderio import Loaderio	
	loader = Loaderio('API_KEY')
	
	print loader.apps.list()
	print loader.apps.create('www.example.com')
	print loader.apps.get('app_id')
	print loader.apps.verify('app_id', method = 'http')
	print loader.apps.delete('app_id')
```

### Tests



[Loaderio]: http://docs.loader.io/api/intro.html        "Loader.io"