import json
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
        
    @staticmethod
    def dark_theme_users():
        json_struct = {"settings":{"theme" : "dark"}}
        users = list(
            UserModel.select().where(SQL("profile @> %s", (json.dumps(json_struct),)))
        )
        return users
    
    @staticmethod
    def add_interest(user_id, interest):
        user = UserRepo.search_by_id(user_id)
        if not user:
            return
        current_interests = user.profile["interests"]
        if interest not in current_interests:
            current_interests.append(interest)
            user.profile["interests"] = current_interests
            user.save()
        return user

    @staticmethod
    def change_theme(user_id):
        user = UserRepo.search_by_id(user_id)
        if not user:
            return
        current_profile = user.profile
        if current_profile["settings"]["theme"] == "dark":
            current_profile["settings"]["theme"] = "bright"
        else:
            current_profile["settings"]["theme"] = "dark"
        user.profile = current_profile
        user.save()
        return user

    @staticmethod
    def get_recommendations(user_id):

        user = UserRepo.search_by_id(user_id)
        if not user:
            return []
        current_interests = user.profile["interests"]
        if not current_interests:
            return []
        
        recommended_users = set()
        
        for interest in current_interests:
            json_struct = {"interests": [interest]}
            users = UserModel.select().where(
                (UserModel.id != user_id) &
                SQL("profile @> %s", (json.dumps(json_struct),))
            )
            for u in users:
                recommended_users.add(u)
        
        return list(recommended_users)