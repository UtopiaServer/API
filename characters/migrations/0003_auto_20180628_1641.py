# Generated by Django 2.0.6 on 2018-06-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20180628_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]