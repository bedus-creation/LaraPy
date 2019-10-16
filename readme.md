# LaraPy
A python implementation of laravel framework for machine learning, AI, datascience and data intensive work.

### Features
* **MVC** Framework
* **Routing**
* **jinja 2** templating engine.

### Serve app
```
gunicorn server:app -b :8080 
```
### Testing
```
python -m pytest

# With out Network 
python -m pytest -m "not network" 
```
