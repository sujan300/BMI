from django.db import models
from account.models import Account

# Create your models here.


class BMIMODEL(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    result = models.FloatField()
    status = models.CharField(max_length=20)
    suggest = models.TextField()
    show = models.BooleanField(default=False)
    user = models.ForeignKey(Account, on_delete=models.CASCADE,default=None)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"BMI Result of ({self.user.first_name})"


class SuggestionModel(models.Model):
    status_suggestion = models.CharField(max_length=20)
    suggest_message = models.TextField()