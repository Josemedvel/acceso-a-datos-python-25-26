from peewee import *
from playhouse.postgres_ext import *
from models.like_model import LikeModel
from repositories.post_repo import PostRepo
class LikeRepo:
    @staticmethod
    def create(user, post):
        try:
            PostRepo.like(post.id)
            return LikeModel.create(user=user, post=post)
        except Exception as e:
            print(f"Error dando like: {e}")