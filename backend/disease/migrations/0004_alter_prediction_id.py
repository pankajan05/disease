# Generated by Django 3.2 on 2021-04-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0003_auto_20210414_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]