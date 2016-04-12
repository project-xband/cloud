import webapp2


from google.appengine.ext import ndb


class User(ndb.Model):
  username = ndb.StringProperty()
  password = ndb.StringProperty()
  age      = ndb.IntegerProperty()



user = User()
user.username = 'PythonicWeb'
user.password = 'i<3python'
user.age = 20
user.put()


# users = [User...]
# ndb.put_multi(users)


class DefaultHandler(webapp2.RequestHandler):
  def get(self):
    self.response.write('IT WORKS')


app = webapp2.WSGIApplication([
  ('.*', DefaultHandler)
])