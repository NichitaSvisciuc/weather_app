# Generated by Django 4.0.5 on 2022-06-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubscribeprofile',
            name='sub_expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usersubscribeprofile',
            name='sub_start_date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
