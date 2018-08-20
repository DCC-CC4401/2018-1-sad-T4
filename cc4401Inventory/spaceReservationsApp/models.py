from mainApp.models import Action
from spacesApp.models import Space
from django.db import models


class SpaceReservation(Action):
    space = models.ForeignKey(Space, on_delete=models.CASCADE)

    def get_item(self):
        return self.space

    def get_item_name(self):
        return self.space.name

    def get_item_type(self):
        return 'space'
