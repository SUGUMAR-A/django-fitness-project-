# Generated by Django 4.1.2 on 2023-04-04 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_feedback_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='img',
            field=models.ForeignKey(default='images/coder.jpj', on_delete=django.db.models.deletion.CASCADE, to='mainapp.user_details'),
        ),
    ]