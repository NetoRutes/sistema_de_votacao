from django.db import models

class Candidate(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    party = models.CharField(max_length=5)

    def __str__(self):
        return self.name