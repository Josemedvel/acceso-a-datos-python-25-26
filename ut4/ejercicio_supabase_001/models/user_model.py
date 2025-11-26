from models.basemodel import BaseModel
from peewee import *
from playhouse.postgres_ext import *

class UserModel(BaseModel):
    username = CharField(unique=True)
    email = CharField()
    profile = BinaryJSONField(null=True, default={
        "bio" : "",
        "interests" : [],
        "settings" : {
            "theme" : "dark",
            "privacy" : "public",
            "notifications" : {
                "likes" : True,
                "comments" : True
            }
        }
    })