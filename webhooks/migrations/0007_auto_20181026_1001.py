# Generated by Django 2.0.7 on 2018-10-26 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0006_remove_song_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song1Win', models.BooleanField()),
                ('song2Win', models.BooleanField()),
                ('song1', models.CharField(max_length=200)),
                ('artist1', models.CharField(max_length=200)),
                ('song2', models.CharField(max_length=200)),
                ('artist2', models.CharField(max_length=200)),
                ('votes1', models.IntegerField(default=0)),
                ('votes2', models.IntegerField(default=0)),
                ('totalVotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
