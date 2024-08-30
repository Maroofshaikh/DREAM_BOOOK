# Generated by Django 5.0.6 on 2024-08-29 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_book_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='address',
            field=models.TextField(default='Default Address'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='purchase',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
        migrations.AddField(
            model_name='purchase',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
    ]