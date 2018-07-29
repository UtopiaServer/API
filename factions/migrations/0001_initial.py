# Generated by Django 2.0.7 on 2018-07-29 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0003_auto_20180628_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factions.Faction')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invitations', to='characters.Character')),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='members',
            field=models.ManyToManyField(through='factions.Membership', to='characters.Character'),
        ),
    ]
