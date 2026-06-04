1. the app route decorator tells the application which code to run when that specific route is used in the url
2. flask knows which code to use by using the endpoints of the routes
3. route parameters go in the url, query parameters are values that go after the url to be used - like in calculate
4. request.get_json() uses data given, and request.args.get() uses data from the url
5. it wont work