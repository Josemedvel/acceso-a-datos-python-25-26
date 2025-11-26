from peewee import *
from playhouse.postgres_ext import *
from models.user_model import UserModel

class UserRepo:
    @staticmethod
    def create(username, email, profile=None):
        
        try:
            if profile:
                return UserModel.create(username=username, email=email, profile=profile)
            else:
                return UserModel.create(username=username, email=email)
        except Exception as e:
            print(f"Error insertando al usuario: {e}")
            return None
        
    @staticmethod
    def search_by_id(id):
        try:
            return UserModel.get(UserModel.id == id)
        except Exception as e:
            print(f"Error buscando usuario con id {id}: {e}")
            return None
    
    @staticmethod
    def search_all():
        return list(UserModel.select())
        