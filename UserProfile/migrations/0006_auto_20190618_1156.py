# Generated by Django 2.2 on 2019-06-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfile', '0005_profile_other_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='education_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='entertainment_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='financial_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='food_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_coordinate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hotel_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='medical_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='natural_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='shopping_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sport_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tourism_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='transportation_detail',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_coordinate',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_location',
            field=models.TextField(),
        ),
    ]
