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

```
	#Get tests list
	print loader.tests.list()

	#Create test
	#Note: You can add more url options as per api docs
	loader.tests.name = 'Gonna crush yah!'
	loader.tests.test_type = 'Non-Cycling'
	loader.tests.total = 400
	loader.tests.duration = 30
	loader.tests.urls = [
			{'url': 'http://gonacrushyaurl.com', 'request_params' : {"name": "Steve"}}]
	loader.tests.create()

	#Others
	loader.tests.get(test_id)
	loader.tests.run(test_id)
	loader.tests.stop(test_id)

```

### Results
```
	loader.results.list(test_id)
	loader.results.get(test_id,results_id)
```

### Servers
```
	loader.servers.list(test_id)
```

##License

The MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

[Loaderio]: http://docs.loader.io/api/intro.html        "Loader.io"