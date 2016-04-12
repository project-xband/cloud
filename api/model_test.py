from google.appengine.ext import ndb


class Post(ndb.Model):
  content = ndb.TextProperty()
  author  = ndb.KeyProperty()

  def get_author(self):
    return self.author.get()


class User(ndb.Model):
  username        = ndb.StringProperty()
  password        = ndb.StringProperty()
  age             = ndb.IntegerProperty()
  favorite_things = ndb.StringProperty(repeated=True)
  
  def get_posts(self):
    return Post.query(Post.author == self.key)


# all posts by author
user = User.query().get()
Post.query(Post.author == user.key)

# query examples
users = User.query(User.favorite_things.IN(['raspberries']))
users = User.query(User.age > 18)

# create a post
user = User.query().get()

post = Post()
post.content = 'Hello World!'
post.author = user.key
post.put()


"""
user = User()
user.username = 'PythonicWeb'
user.password = 'i<3python'
user.age = 20
user.put()
"""

"""
user = ndb.Key(urlsafe='ahFkZXZ-YXBwbGljYXRpb25pZHIRCxIEVXNlchiAgICAgOCXCgw').get()
print user
"""

"""
users = User.query(User.username != 'PythonicWeb')
print list(users.order(-User.username))
print list(users.order(-User.age))
"""

"""
key = ndb.Key(urlsafe='ahFkZXZ-YXBwbGljYXRpb25pZHIRCxIEVXNlchiAgICAgOCXCgw')
print key

user = key.get()
print user.key.id()

user = User.get_by_id(5733953138851840)
print user
"""

