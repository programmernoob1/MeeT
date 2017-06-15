from datetime import datetime
from .models import UserProfile
import pytz
from neomodel import StructuredNode, UniqueIdProperty, Relationship, RelationshipFrom, RelationshipTo, StringProperty, \
    DateTimeProperty, StructuredRel, One
class Friendship(StructuredRel):
    since= DateTimeProperty(default=lambda: datetime.now(pytz.utc))





class PostMeta(StructuredRel):
    datetime = DateTimeProperty(default=lambda: datetime.now(pytz.utc))

class UserNode(StructuredNode):
    uid=UniqueIdProperty()
    friends=Relationship('UserNode','friends_with',model=Friendship)
    posts=RelationshipTo('PostNode','posted')
    requestsfrom=RelationshipFrom('UserNode','friendship_request')
    requeststo=RelationshipTo('UserNode','friendship_request')
    likes=RelationshipTo('PostNode','likes')
    def get_profile(self):
        return UserProfile.objects.get(id=self.uid)
    def __str__(self):
        return self.uid
class PostNode(StructuredNode):
    postedby=RelationshipFrom('UserNode','posted',cardinality=One)
    body=StringProperty()
    liked_by=RelationshipFrom('UserNode','likes')
    postdatetime=DateTimeProperty(default=lambda: datetime.now(pytz.utc))

class Friendship(StructuredRel):
    since= DateTimeProperty(default=lambda: datetime.now(pytz.utc))





