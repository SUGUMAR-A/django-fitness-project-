# Generated by Django 4.1.7 on 2023-04-02 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_user_details_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_details',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
