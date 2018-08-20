from mainApp.models import Action
from articlesApp.models import Article
from django.db import models


class ArticleReservation(Action):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def get_item(self):
        return self.article

    def get_item_name(self):
        return self.article.name

    def get_item_type(self):
        return 'article'
