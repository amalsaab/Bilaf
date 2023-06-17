# Generated by Django 4.2.2 on 2023-06-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0007_delete_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='commercial_registration',
        ),
        migrations.AlterField(
            model_name='store',
            name='instagram_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='snapchat_link',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='twitter_link',
            field=models.URLField(null=True),
        ),
    ]