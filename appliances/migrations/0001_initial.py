# Generated by Django 2.1.1 on 2018-09-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appliance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('age', models.IntegerField()),
                ('country', models.TextField()),
                ('way_of_known', models.IntegerField()),
                ('discord_handle', models.TextField()),
                ('minecraft_username', models.TextField()),
                ('have_you', models.TextField()),
                ('gamemodes', models.TextField()),
                ('expectations', models.TextField()),
                ('appliance', models.TextField()),
            ],
        ),
    ]