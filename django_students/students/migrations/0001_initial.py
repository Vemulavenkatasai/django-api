# Generated by Django 5.2.4 on 2025-07-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('student_class', models.CharField(max_length=50)),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
