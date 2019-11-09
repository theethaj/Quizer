# Generated by Django 2.2.6 on 2019-11-07 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizer_game', '0002_edit_quiz_attribute_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='is_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quizer_game.Quiz'),
        ),
    ]