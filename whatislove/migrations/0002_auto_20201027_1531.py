# Generated by Django 3.1.2 on 2020-10-27 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatislove', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='film',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
