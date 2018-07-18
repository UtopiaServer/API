# Generated by Django 2.0.6 on 2018-06-26 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot', models.CharField(max_length=20)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventories.Inventory')),
            ],
        ),
    ]
