# Generated by Django 3.2.5 on 2021-08-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_list', models.DateTimeField(auto_created=True)),
                ('first_Name', models.CharField(max_length=100)),
                ('last_Name', models.CharField(max_length=100)),
                ('phone_Number', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]