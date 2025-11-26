from datetime import datetime
from peewee import *
from playhouse.postgres_ext import *
from models.basemodel import BaseModel
from models.user_model import UserModel

class PostModel(BaseModel):
    author = ForeignKeyField(UserModel, backref="posts")
    text = CharField(max_length=280)
    media = BinaryJSONField(default={
        "images" : [],
        "videos" : [],
        "links" : []
    })
    stats = BinaryJSONField(default={
        "likes" : 0,
        "tags" : []
    })
    created_at = DateTimeField(default=datetime.now)