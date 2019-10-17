from Chamak.Foundation.Router import Router

# Define Your routes here.
Router.get('/', 'HomeController@index')
Router.get('/contact', 'HomeController@contact')
Router.get('/home', 'HomeController@home')
