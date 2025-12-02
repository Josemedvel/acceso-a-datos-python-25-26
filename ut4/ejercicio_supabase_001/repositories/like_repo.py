import json
from peewee import *
from playhouse.postgres_ext import *
from models.like_model import LikeModel
from models.user_model import UserModel
from models.post_model import PostModel

class LikeRepo:
    @staticmethod
    def create(user, post):
        try:
            # Actualizar stats del post directamente
            post.stats["likes"] = post.stats.get("likes", 0) + 1
            post.save()
            
            return LikeModel.create(user=user, post=post)
        except Exception as e:
            print(f"Error dando like: {e}")
            return None
        
    @staticmethod
    def search_all():
        return list(LikeModel.select())
    
    @staticmethod
    def post_likes(post_id):
        return list(LikeModel.select().where(LikeModel.post == post_id))
    
    @staticmethod
    def users_who_liked(post_id):
        likes = LikeRepo.post_likes(post_id)
        users = [like.user for like in likes]
        return users

    @staticmethod
    def nerd_interest_likes():
        json_struct = {"interests": ["programación"]}
        
        likes = (
            LikeModel.select()
            .join(UserModel, on=(UserModel.id == LikeModel.user))
            .where(UserModel.profile.contains(json_struct))
        )
        return list(likes)
    
    @staticmethod
    def like_count_list():
        likes = list(
            LikeModel.select(UserModel.username, fn.COUNT(LikeModel.id).alias("num_likes"))
            .join(UserModel, on=(LikeModel.user == UserModel.id))
            .group_by(UserModel.id)
            .order_by(fn.COUNT(LikeModel.id).desc())
            .dicts()
        )
            
        return likes
