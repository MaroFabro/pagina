# Generated by Django 4.1 on 2022-08-30 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripción',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_de_banda_o_artista', models.CharField(max_length=30)),
                ('Cantidad_de_integrantes', models.IntegerField(max_length=2)),
                ('Infromación_artística_o_reseña', models.CharField(max_length=255)),
                ('Rubro_o_género_de_música', models.CharField(max_length=100)),
                ('Localidad', models.CharField(max_length=100)),
                ('Contacto_telefónico', models.CharField(max_length=15)),
                ('Contacto_Mail', models.EmailField(max_length=254)),
                ('Link_o_sitios_de_material_discográfico', models.CharField(max_length=1000)),
                ('Razón_social', models.CharField(max_length=255)),
            ],
        ),
    ]