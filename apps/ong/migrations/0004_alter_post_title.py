# Generated by Django 4.2.3 on 2023-08-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ong', '0003_newsletteruser_date_post_autor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64, verbose_name='title'),
        ),
    ]
