def test_middleware(get_response):
   # One-time configuration and initialization.

   def middleware(request):
       # Code to be executed for each request before
       # the view (and later middleware) are called.
       print("This is our test middleware, request level", request)
       response = get_response(request)
       print("this our test middleware, response level", response)
       # Code to be executed for each request/response after
       # the view is called.

       return response

   return middleware