# Generated by Django 2.2.24 on 2021-10-08 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ktiria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eidos', models.TextField()),
                ('tetragonika', models.BigIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diakstiria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eidos_dikastiriou', models.TextField(blank=True, null=True)),
                ('fk_ktirio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diakstiria_fk_ktirio', to='home.Ktiria')),
            ],
        ),
    ]