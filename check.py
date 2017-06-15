from neomodel import *
from django.contrib.auth.models import User
class Check(StructuredNode):
  uid=UniqueIdProperty()
a=Check(uid=User.objects.all()[0])
print(Check.nodes.get(User.objects.all()[0]))
