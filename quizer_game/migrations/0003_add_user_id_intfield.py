# Generated by Django 2.2.6 on 2019-11-30 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizer_game', '0002_upvote_downvote_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]