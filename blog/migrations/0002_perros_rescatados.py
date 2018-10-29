# Generated by Django 2.1.2 on 2018-10-28 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perros_Rescatados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='', max_length=30)),
                ('fotografia_perro', models.FileField(blank=True, null=True, upload_to='')),
                ('nombre_perro', models.CharField(max_length=200)),
                ('raza_predominante', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('adoptantes', 'Adoptantes'),),
            },
        ),
    ]
