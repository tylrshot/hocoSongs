# Generated by Django 2.0.7 on 2018-12-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0014_auto_20181026_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(choices=[('Fast', 'Fast'), ('Slow', 'Slow'), ('Dance', 'Dance'), ('Other', 'Other'), ('Christmas', 'Christmas')], default='Fast', max_length=25),
        ),
    ]
