# Generated by Django 4.0.3 on 2022-05-03 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0006_alter_film_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult', models.FloatField(default=5.0)),
                ('student', models.FloatField(default=4.0)),
                ('child', models.FloatField(default=3.0)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to=''),
        ),
    ]
