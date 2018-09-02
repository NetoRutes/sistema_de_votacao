from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    party = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Election(models.Model):
    label = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    candidates = models.ManyToManyField('election.Candidate')

    def __str__(self):
        return self.label