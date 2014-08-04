from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Score(models.Model):
    player = models.ForeignKey(User)
    score = models.PositiveSmallIntegerField()
    datetime = models.DateTimeField(auto_now_add=True)

    choices = (
        ('Snake', 'Snake'),
        ("Memory", 'Memory')
    )
    game = models.CharField(max_length=40, choices=choices, default='Snake')


    def __unicode__(self):
        return "{} {} {}".format(self.player, self.score, self.game)


    # def get_high_score(self):

