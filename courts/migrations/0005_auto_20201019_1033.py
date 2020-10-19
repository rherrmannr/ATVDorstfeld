# Generated by Django 3.1.2 on 2020-10-19 10:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courts', '0004_reservation_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
