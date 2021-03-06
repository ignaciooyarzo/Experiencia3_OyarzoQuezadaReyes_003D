# Generated by Django 3.2.3 on 2021-06-04 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('gmail', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='gmail')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=20, verbose_name='Apellido')),
                ('numero', models.CharField(max_length=20, verbose_name='Apellido')),
                ('comentario', models.CharField(max_length=20, verbose_name='Comentario')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AllStars.categoria')),
            ],
        ),
    ]
