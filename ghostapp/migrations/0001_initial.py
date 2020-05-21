# Generated by Django 3.0.6 on 2020-05-20 02:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoteChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=280)),
                ('time', models.DateTimeField(verbose_name=django.utils.timezone.now)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
            ],
        ),
    ]