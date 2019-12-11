# Generated by Django 3.0 on 2019-12-11 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackerspace', '0007_auto_20191211_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='consensus',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='guilde',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='machine',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='person',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='photo',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='project',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AddField(
            model_name='wish',
            name='text_description_he_IL',
            field=models.TextField(blank=True, null=True, verbose_name='Description he-IL'),
        ),
        migrations.AlterField(
            model_name='consensus',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='guilde',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='person',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
        migrations.AlterField(
            model_name='wish',
            name='text_description_en_US',
            field=models.TextField(blank=True, null=True, verbose_name='Description en-US'),
        ),
    ]
