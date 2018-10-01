from django.conf import settings
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


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             verbose_name='Eleitor', on_delete=models.PROTECT)
    election = models.ForeignKey(
        'election.Election', verbose_name='Eleição', on_delete=models.PROTECT)
    candidate = models.ForeignKey(
        'election.Candidate', verbose_name='Candidato', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('user', 'election')

    def __str__(self):
        return 'Usuário: {} | Eleição: {} | Candidato: {}'.format(self.user, self.election, self.candidate)
