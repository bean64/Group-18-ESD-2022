# Generated by Django 4.0.2 on 2022-03-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uweflix', '0002_customer_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(max_length=7)),
                ('transaction', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='uweflix.transaction')),
            ],
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
    ]