# Generated by Django 2.0.7 on 2019-05-07 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20190429_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=10000)),
            ],
        ),
    ]
