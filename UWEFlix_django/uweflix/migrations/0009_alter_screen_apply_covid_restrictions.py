# Generated by Django 4.0.2 on 2022-05-04 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0008_alter_film_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screen',
            name='apply_covid_restrictions',
            field=models.BooleanField(null=True),
        ),
    ]