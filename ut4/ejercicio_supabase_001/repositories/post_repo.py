from peewee import *
from playhouse.postgres_ext import *
from models.post_model import PostModel


class PostRepo:
    @staticmethod
    def create(author,text):
        try:
            return PostModel.create(author=author, text=text)
        except Exception as e:
            print(f"Error insertando post: {e}")
            return None
    
    @staticmethod
    def search_by_id(id):
        try:
            return PostModel.get(PostModel.id == id)
        except Exception as e:
            print(f"Error buscando post con id {id}: {e}")
            return None
    
    @staticmethod
    def search_all():
        return list(PostModel.select())
    
    @staticmethod
    def like(post_id):
        post = PostRepo.search_by_id(post_id)
        if post:
            post.stats["likes"] += 1
            post.save()
            return post
        return None
    
    @staticmethod
    def user_posts(user_id):
        return list(PostModel.select().where(PostModel.author == user_id))
    
    @staticmethod
    def twenty_plus_likes():
        from models.like_model import LikeModel
        from peewee import fn
        posts_20_plus_likes = {}
        
        posts = (PostModel.select(PostModel, fn.COUNT(LikeModel.id).alias("likes"))
            .join(LikeModel, on=(PostModel.id == LikeModel.post))
            .group_by(PostModel.id)
            .having(fn.COUNT(LikeModel.id) >= 20)
            .dicts())
        
        for post in posts:
            posts_20_plus_likes[post["id"]] = post["likes"]
        return posts_20_plus_likes
        '''
        # con backrefs (menos eficiente claro)
        posts = PostModel.select()
        for post in posts:
            likes = list(post.likes)
            if len(likes) >= 20:
                posts_20_plus_likes[post] = len(likes)
        return posts_20_plus_likes
        '''

    
        