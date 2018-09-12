# Generated by Django 2.1.1 on 2018-09-06 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=32)),
                ('url', models.URLField()),
                ('md5', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Namespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='RevisionMod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launcher.Mod')),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='launcher.Revision')),
            ],
        ),
        migrations.AddField(
            model_name='revision',
            name='mods',
            field=models.ManyToManyField(through='launcher.RevisionMod', to='launcher.Mod'),
        ),
        migrations.AddField(
            model_name='mod',
            name='namespace',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='launcher.Namespace'),
        ),
    ]