from __future__ import unicode_literals
from django.db import models


# Create your models here.
# class Status(models.Model):
#     text = models.CharField(max_length=200)
#     date_added = models.DateTimeField(auto_now_add=True)
#     author = models.CharField(default="Eau de Web", max_length=50)

#     def __unicode__(self):
#         return '{} by {}'.format(self.text, self.author)


class Sport(models.Model):
    nume = models.CharField(max_length=20)

    def __str__(self):
        return self.nume


class Echipa(models.Model):
    nume = models.CharField(max_length=20)

    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    # meciuri = models.ManyToManyField(Meci)

    def __str__(self):
        return self.nume

class Meci(models.Model):
    data = models.DateField()
    echipa1 = models.ForeignKey(Echipa, on_delete=models.CASCADE, related_name='ech1')
    echipa2 = models.ForeignKey(Echipa, on_delete=models.CASCADE, related_name='ech2')
    

class Jucator(models.Model):
    prenume = models.CharField(max_length=20)
    nume = models.CharField(max_length=20)
    varsta = models.IntegerField()


    echipa = models.ManyToManyField(Echipa)

    def __str__(self):
        return self.prenume + " " + self.nume



