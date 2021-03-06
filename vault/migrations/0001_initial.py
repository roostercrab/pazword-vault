# Generated by Django 2.1 on 2019-04-23 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved_password', models.CharField(db_column='SavedPassword', max_length=256, unique=True)),
                ('website', models.CharField(db_column='Website', max_length=256, unique=True)),
                ('description', models.CharField(blank=True, db_column='Description', max_length=8000, null=True)),
            ],
        ),
    ]
