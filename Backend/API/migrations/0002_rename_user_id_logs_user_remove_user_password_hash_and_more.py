# Generated by Django 5.1.1 on 2024-09-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logs',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password_hash',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=192, max_length=256, unique=True),
            preserve_default=False,
        ),
    ]
