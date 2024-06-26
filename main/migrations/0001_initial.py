# Generated by Django 4.2 on 2024-05-13 00:31

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MushroomSpot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]
