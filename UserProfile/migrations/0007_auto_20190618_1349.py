# Generated by Django 2.2 on 2019-06-18 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0006_auto_20190618_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='entertainment_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='financial_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='food_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hotel_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='medical_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='natural_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shopping_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tourism_nums',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='transportation_nums',
            field=models.CharField(max_length=50),
        ),
    ]