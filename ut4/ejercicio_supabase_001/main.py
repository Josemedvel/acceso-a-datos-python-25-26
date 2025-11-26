from database import db, inicializar_base

from pprint import pprint

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



usuario = UserRepo.search_all()[0]
if usuario:
    pprint(usuario.__dict__["__data__"])

post_fake_news = PostRepo.create(usuario, "Venezuelan dictator will burn in hell")

for post in usuario.posts.dicts():
    pprint(post)

like_trump = LikeRepo.create(user=usuario, post=post_fake_news)

for post in usuario.posts.dicts():
    pprint(post)

