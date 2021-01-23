
class Foo():

   def __init__(self):
      print("Foo init")
      self.baz = "BAZ"

   def bar(self):
   	  print(f"Foo bar() called {self.baz}")