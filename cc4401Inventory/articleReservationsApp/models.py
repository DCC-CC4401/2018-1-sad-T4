from mainApp.models import Action
from articlesApp.models import Article
from django.db import models


class ArticleReservation(Action):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
