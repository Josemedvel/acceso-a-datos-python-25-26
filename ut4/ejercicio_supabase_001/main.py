from database import db, inicializar_base

from pprint import pprint
from playhouse.shortcuts import model_to_dict
from models.user_model import UserModel
from models.post_model import PostModel
from models.like_model import LikeModel

from repositories.user_repo import UserRepo
from repositories.post_repo import PostRepo
from repositories.like_repo import LikeRepo

inicializar_base([UserModel, PostModel, LikeModel])

trump = UserRepo.create(
    username = "DonaldTheTrump",
    email = "potus@hotmail.com"
)
putin = UserRepo.create(
    username = "LadaLover",
    email = "putin@kremlin.ru"
)
UserRepo.add_interest(trump, "programación")
UserRepo.add_interest(trump, "programación")
UserRepo.add_interest(trump, "patinaje")
UserRepo.add_interest(putin, "patinaje")
UserRepo.change_theme(trump)
usuario = UserRepo.search_all()[0]
if usuario:
    pprint(usuario.__dict__["__data__"])

post_fake_news = PostRepo.create(trump, "Venezuelan dictator will burn in hell")

for post in usuario.posts.dicts():
    pprint(post)

like_trump = LikeRepo.create(user=usuario, post=post_fake_news)
print(LikeRepo.like_count_list())
for post in usuario.posts.dicts():
    pprint(post)

# usuarios con tema oscuro
usuarios = UserRepo.dark_theme_users()
for usuario in usuarios:
    pprint(model_to_dict(usuario))

# amigos
posibles_amigos = UserRepo.get_recommendations(trump)
for p_amigo in posibles_amigos:
    print(p_amigo.__dict__["__data__"])