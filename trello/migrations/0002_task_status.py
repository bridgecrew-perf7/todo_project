# Generated by Django 3.2.5 on 2021-07-09 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('P', 'PENDING'), ('C', 'COMPLETED'), ('IP', 'IN_PROGRESS'), ('D', 'DROPPED')], default=('IP', 'IN_PROGRESS'), max_length=2),
        ),
    ]