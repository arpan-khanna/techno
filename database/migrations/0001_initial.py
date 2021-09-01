# Generated by Django 3.2.5 on 2021-09-01 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=200)),
                ('blocks1', models.IntegerField()),
                ('code1', models.TextField()),
                ('blocks2', models.IntegerField()),
                ('code2', models.TextField()),
                ('blocks3', models.IntegerField()),
                ('code3', models.TextField()),
            ],
        ),
    ]