# Generated by Django 2.1 on 2018-09-02 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0002_election'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='candidates',
        ),
        migrations.AddField(
            model_name='election',
            name='candidates',
            field=models.ManyToManyField(to='election.Candidate'),
        ),
    ]
