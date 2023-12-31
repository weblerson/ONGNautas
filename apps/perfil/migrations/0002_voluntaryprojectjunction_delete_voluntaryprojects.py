# Generated by Django 4.2.3 on 2023-08-09 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_cpf'),
        ('ong', '0001_initial'),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoluntaryProjectJunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='hours worked')),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ong.project', verbose_name='project')),
                ('voluntary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.voluntary', verbose_name='voluntary')),
            ],
        ),
        migrations.DeleteModel(
            name='VoluntaryProjects',
        ),
    ]
