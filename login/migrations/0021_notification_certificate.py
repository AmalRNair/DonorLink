# Generated by Django 3.0.5 on 2023-06-28 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_notification_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='certificate',
            field=models.CharField(default=None, max_length=100),
        ),
    ]