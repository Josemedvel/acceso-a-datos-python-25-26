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