# Generated by Django 4.2.3 on 2023-08-15 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ong', '0002_newsletteruser_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletteruser',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AddField(
            model_name='post',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='amount_expected',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='amount spent'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='date')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
