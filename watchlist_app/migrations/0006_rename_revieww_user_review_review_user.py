# Generated by Django 4.1.5 on 2023-02-07 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_review_revieww_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='revieww_user',
            new_name='review_user',
        ),
    ]
