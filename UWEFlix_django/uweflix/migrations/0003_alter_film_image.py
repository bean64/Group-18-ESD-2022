# Generated by Django 4.0.2 on 2022-05-02 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0002_film_image_alter_clubrep_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(default='images\\placeholder.png', upload_to='images'),
        ),
    ]