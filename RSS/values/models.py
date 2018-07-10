from django.db import models


class Currency(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    USD = models.FloatField()
    JPY = models.FloatField()
    BGN = models.FloatField()
    CZK = models.FloatField()

    def __str__(self):
        return str(self.date)
