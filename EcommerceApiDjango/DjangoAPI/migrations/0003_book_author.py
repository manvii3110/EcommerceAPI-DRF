# Generated by Django 3.2.6 on 2021-08-28 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAPI', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='John Doe', max_length=100),
        ),
    ]
