from peewee import *
from playhouse.postgres_ext import *
from models.basemodel import BaseModel
from models.user_model import UserModel
from models.post_model import PostModel

class LikeModel(BaseModel):
    user = ForeignKeyField(UserModel, backref="likes")
    post = ForeignKeyField(PostModel, backref="likes")
    class Meta:
        indexes = (
            (("user", "post"), True),
        )